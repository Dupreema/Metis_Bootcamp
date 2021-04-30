import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from sqlalchemy import create_engine


st.title('Alaskan Oil Production Application')
st.markdown('By Matthew Dupree')
#These are the selectboxes the user interacts with
engine = create_engine("sqlite:///alaska_oil_data.db")
df_map = pd.read_sql('''SELECT Distinct p.Wellname, l.WellHeadLat, l.WellHeadLong
                                        FROM production p 
                                        LEFT JOIN location l ON p.API = l.APINumber
                                        WHERE lower(p.ProductionMethod) NOT LIKE '%shut%' ''', engine)
df_map.columns=['Well','lat','lon']
df_map.dropna(axis = 0, inplace= True)
client_response_1  = st.selectbox( 'Select Alaskan Oil Pool', pd.read_sql('''SELECT DISTINCT Pool FROM Production WHERE lower(Pool) NOT LIKE '%und%' ''', engine))
client_response_2  = st.selectbox( 'Select Alaskan Pad', pd.concat([pd.DataFrame(data = ['All'],columns=['Pad']), pd.read_sql(f''' SELECT DISTINCT Pad FROM Production WHERE Pool = '{client_response_1}' ''', engine)]).reset_index(drop=True))
client_response_3  = st.selectbox( 'Select Alaskan Well', pd.concat([pd.DataFrame(data = ['All'],columns=['WellName']), pd.read_sql(f'''SELECT DISTINCT WellName FROM Production Where Pool = '{client_response_1}' AND Pad = '{client_response_2}' ''', engine)]).reset_index(drop=True))

#Query based on user input
if (client_response_2 == 'All') & (client_response_3 == 'All'):
    query1 = '''SELECT Distinct p.Wellname, l.WellHeadLat, l.WellHeadLong FROM production p LEFT JOIN location l ON p.API = l.APINumber WHERE lower(p.ProductionMethod) NOT LIKE '%shut%'AND p.Pool = '{}' '''.format(client_response_1)
    query2 = '''SELECT p.* , l.WellHeadLat, l.WellHeadLong FROM production p LEFT JOIN location l ON p.API = l.APINumber WHERE p.pool = '{}' AND lower(p.ProductionMethod) NOT LIKE '%shut%' '''.format(client_response_1)
    query3 = '''SELECT * From injection where pool = '{}' AND lower(InjectionType) NOT LIKE '%disposal%' AND lower(InjectionType) NOT LIKE '%storage%' AND lower(InjectionType) NOT LIKE '%shut%' AND lower(InjectionMethod) NOT LIKE '%shut%' AND lower(WellStatus) NOT LIKE '%abandon%' '''.format(client_response_1)
elif (client_response_2 != 'All') & (client_response_3 == 'All'):
    query1 = '''SELECT Distinct p.Wellname, l.WellHeadLat, l.WellHeadLong FROM production p LEFT JOIN location l ON p.API = l.APINumber WHERE lower(p.ProductionMethod) NOT LIKE '%shut%'AND p.Pool = '{}' AND p.Pad = '{}' '''.format(client_response_1, client_response_2)
    query2 = '''SELECT p* , l.WellHeadLat, l.WellHeadLong FROM production p LEFT JOIN location l ON p.API = l.APINumber WHERE p.pool = '{}' AND p.Pad = '{}' AND lower(p.ProductionMethod) NOT LIKE '%shut%' '''.format(client_response_1, client_response_2)
    query3 = '''SELECT * From injection where Pool = '{}' AND Pad = '{}' lower(InjectionType) NOT LIKE '%disposal%' AND lower(InjectionType) NOT LIKE '%storage%' AND lower(InjectionType) NOT LIKE '%shut%' AND lower(InjectionMethod) NOT LIKE '%shut%' AND lower(WellStatus) NOT LIKE '%abandon%' '''.format(client_response_1, client_response_2)
else:
    query1 = '''SELECT Distinct p.Wellname, l.WellHeadLat, l.WellHeadLong FROM production p LEFT JOIN location l ON p.API = l.APINumber WHERE lower(p.ProductionMethod) NOT LIKE '%shut%'AND p.WellName = '{}' '''.format(client_response_3)
    query2 ='''SELECT p.* , l.WellHeadLat, l.WellHeadLong FROM production p LEFT JOIN location l ON p.API = l.APINumber WHERE p.WellName = '{}'  AND lower(p.ProductionMethod) NOT LIKE '%shut%' '''.format(client_response_3)
    query3 = '''SELECT * From injection where WellName = '{}' lower(InjectionType) NOT LIKE '%disposal%' AND lower(InjectionType) NOT LIKE '%storage%' AND lower(InjectionType) NOT LIKE '%shut%' AND lower(InjectionMethod) NOT LIKE '%shut%' AND lower(WellStatus) NOT LIKE '%abandon%' '''.format(client_response_3)

#Create Map based on query 
df_map = pd.read_sql(query1, engine)
df_map.columns=['Well','lat','lon']
df_map.dropna(axis = 0, inplace= True)
st.map(df_map)
st.markdown(' #### You picked {} pad(s) from the {} pool.'.format(client_response_2,client_response_1))
button = st.button('Click here to see Production Charts')
if button:
    #Production Query
    df_prod = pd.read_sql(query2, engine)
    st.markdown(' #### This data represents {} Wells'.format(df_prod['WellName'].nunique()))
    df_prod['Month'] = pd.to_datetime(df_prod['Date'], format= '%m/%Y', utc=False)
    df_prod.drop('Date', axis = 1, inplace = True)
    df_prod['Field_start'] = df_prod['Month'].min()
    if df_prod['Oil'].dtype == 'object':
        df_prod['Oil'] = df_prod['Oil'].str.replace(',','').fillna(0)
        df_prod['Oil'] = pd.to_numeric(df_prod['Oil'])
    if df_prod['Gas'].dtype == 'object':
        df_prod['Gas'] = df_prod['Gas'].str.replace(',','').fillna(0)
        df_prod['Gas'] = pd.to_numeric(df_prod['Gas'])
    if df_prod['Water'].dtype == 'object':
        df_prod['Water'] = df_prod['Water'].str.replace(',','').fillna(0)
        df_prod['Water'] = pd.to_numeric(df_prod['Water'])
    df_prod['Oil_avg'] = df_prod['Oil']/df_prod['Days']
    df_prod['Gas_avg'] = df_prod['Gas']/df_prod['Days']
    df_prod['Water_avg'] = df_prod['Water']/df_prod['Days']
    df_prod['Normalized_months'] = (df_prod['Month'].dt.year - df_prod['Field_start'].dt.year)*12 + (df_prod['Month'].dt.month - df_prod['Field_start'].dt.month)
    df_prod_avg=df_prod.groupby('Normalized_months')[["Oil_avg", "Gas_avg", "Water_avg"]].sum().reset_index()
    df_prod_avg.drop(df_prod_avg[df_prod_avg['Normalized_months']<0].index, inplace = True)
    df_prod_avg = df_prod_avg.reset_index()
    df_prod_avg.drop('index', axis = 1, inplace = True)

    #Production Chart
    fig,ax = plt.subplots()
    ax.plot(df_prod_avg['Normalized_months'], df_prod_avg['Oil_avg'], color="green")
    ax.plot(df_prod_avg['Normalized_months'], df_prod_avg['Water_avg'], color = "blue")
    ax.set_xlabel("Months Since First Production",fontsize=20)
    ax.set_ylabel("Liquid Production, Stb/day",color="green",fontsize=20)
    ax2=ax.twinx()
    ax2.plot(df_prod_avg['Normalized_months'], df_prod_avg['Gas_avg'],color="red")
    ax2.set_ylabel("Gas Production, Mscf/day",color="red",fontsize=20)
    fig.set_size_inches(20, 8)

    st.pyplot(fig, figsize=(20, 8))

    #Watercut/GOR
    df_prod_avg['Watercut'] = df_prod_avg['Water_avg']/(df_prod_avg['Water_avg']+ df_prod_avg['Oil_avg'])
    df_prod_avg['GOR'] = df_prod_avg['Gas_avg']*1000 / df_prod_avg['Oil_avg']

    fig,ax = plt.subplots()
    ax.plot(df_prod_avg['Normalized_months'], df_prod_avg['Watercut'], color = "blue")
    ax.set_xlabel("Months Since First Production",fontsize=20)
    ax.set_ylabel("Watercut, %",color="blue",fontsize=20)
    ax2=ax.twinx()
    ax2.plot(df_prod_avg['Normalized_months'], df_prod_avg['GOR'],color="red")
    ax2.set_ylabel("GOR, scf/stb",color="red",fontsize=20)
    fig.set_size_inches(20, 8)

    st.pyplot(fig, figsize=(20, 8))

    #Cumulative Productions
    df_prod_cum = df_prod_avg[['Normalized_months']]
    df_prod_cum['Oil_cum']= (df_prod_avg['Oil_avg']/1000000).cumsum()
    df_prod_cum['Gas_cum']= (df_prod_avg['Gas_avg']/1000000).cumsum()
    df_prod_cum['Water_cum']= (df_prod_avg['Water_avg']/1000000).cumsum()

    fig,ax = plt.subplots()
    ax.plot(df_prod_cum['Normalized_months'], df_prod_cum['Oil_cum']*30.44, color="green")
    ax.plot(df_prod_cum['Normalized_months'], df_prod_cum['Water_cum']*30.44, color = "blue")
    ax.set_xlabel("Months Since First Production",fontsize=20)
    ax.set_ylabel("Cumulative Liquid Production, MMStb",color="green",fontsize=20)
    ax2=ax.twinx()
    ax2.plot(df_prod_cum['Normalized_months'], df_prod_cum['Gas_cum']*30.44,color="red")
    ax2.set_ylabel("Cumulative Gas Production, Bscf",color="red",fontsize=20)
    fig.set_size_inches(20, 8)

    st.pyplot(fig, figsize=(20, 8))

    st.markdown(' ##### Cum Oil : {:.2f} Million STB, Cum Gas : {:.2f} Billion scf, Cum Water : {:.2f} Million STB '.format(df_prod_cum.Oil_cum.max()*30.44,df_prod_cum.Gas_cum.max()*30.44, df_prod_cum.Water_cum.max()*30.44))
    
    def get_max_for_decline (df):
        split_size = round(len(df_prod_avg)/20)
        split_list = []
        split1 = df.loc[0:split_size-1]
        split_list.append(split1[split1['Oil_avg'] == split1.Oil_avg.max()][['Normalized_months','Oil_avg']])
        split2 =df.loc[split_size:2*split_size-1]
        split_list.append(split2[split2['Oil_avg'] == split2.Oil_avg.max()][['Normalized_months','Oil_avg']])
        split3 =df.loc[2*split_size:3*split_size-1]
        split_list.append(split3[split3['Oil_avg'] == split3.Oil_avg.max()][['Normalized_months','Oil_avg']])
        split4 =df.loc[3*split_size:4*split_size-1]
        split_list.append(split4[split4['Oil_avg'] == split4.Oil_avg.max()][['Normalized_months','Oil_avg']])
        split5 =df.loc[4*split_size:5*split_size-1]
        split_list.append(split5[split5['Oil_avg'] == split5.Oil_avg.max()][['Normalized_months','Oil_avg']])
        split6 =df.loc[5*split_size:6*split_size-1]
        split_list.append(split6[split6['Oil_avg'] == split6.Oil_avg.max()][['Normalized_months','Oil_avg']])
        split7 =df.loc[6*split_size:7*split_size-1]
        split_list.append(split7[split7['Oil_avg'] == split7.Oil_avg.max()][['Normalized_months','Oil_avg']])
        split8 =df.loc[7*split_size:8*split_size-1]
        split_list.append(split8[split8['Oil_avg'] == split8.Oil_avg.max()][['Normalized_months','Oil_avg']])
        split9 =df.loc[8*split_size:9*split_size-1]
        split_list.append(split9[split9['Oil_avg'] == split9.Oil_avg.max()][['Normalized_months','Oil_avg']])
        splitend =df.loc[9*split_size:]
        split_list.append(splitend[splitend['Oil_avg'] == splitend.Oil_avg.max()][['Normalized_months','Oil_avg']])
    
        diff_list = list([float(j['Oil_avg']) - float(i['Oil_avg']) for i, j in zip(split_list, split_list[1:])])
        neg_indices = [i for i, val in enumerate(diff_list) if val < 0]
        for i in range(len(neg_indices)):
            if neg_indices[i+1]-neg_indices[i] == 1 and neg_indices [i+2]- neg_indices[i+1] == 1:
              return int(split_list[neg_indices[i+2]]['Normalized_months']), float(split_list[neg_indices[i+2]]['Oil_avg'])

    qi_month, qi=get_max_for_decline(df_prod_avg)
    fig,ax = plt.subplots()
    ax.plot(df_prod_avg['Normalized_months'], df_prod_avg['Oil_avg'], color="green")
    ax.axvline(x=qi_month, ymin=-1, ymax=0.95, color = 'black',ls = ':')
    ax.set_xlabel("Months Since First Production",fontsize=20)
    ax.set_ylabel("Liquid Production, Stb/day",color="green",fontsize=20)
    fig.set_size_inches(20, 8)

    st.pyplot(fig, figsize=(20, 8))



button = st.button('Click here to see Injection Charts')
if button:
    #Injection Query
    df_inj = pd.read_sql(query3, engine)
    st.markdown(' #### This data represents {} Wells'.format(df_inj['WellName'].nunique()))
    df_inj['Month'] = pd.to_datetime(df_inj['Date'], format= '%m/%Y', utc=False)
    df_inj.drop('Date', axis = 1, inplace = True)
    df_inj['Field_start'] = df_inj['Month'].min()
    if df_inj['Gas'].dtype == 'object':
        df_inj['Gas'] = df_inj['Gas'].str.replace(',','').fillna(0)
        df_inj['Gas'] = pd.to_numeric(df_inj['Gas'])
    if df_inj['Liquid'].dtype == 'object':
        df_inj['Liquid'] = df_inj['Liquid'].str.replace(',','').fillna(0)
        df_inj['Liquid'] = pd.to_numeric(df_inj['Liquid'])
    df_inj['Gas_avg'] = df_inj['Gas']/df_inj['Days']
    df_inj['Liquid_avg'] = df_inj['Liquid']/df_inj['Days']
    df_inj['Normalized_months'] = (df_inj['Month'].dt.year - df_inj['Field_start'].dt.year)*12 + (df_inj['Month'].dt.month - df_inj['Field_start'].dt.month)
    df_inj_avg=df_inj.groupby('Normalized_months')[["Gas_avg", "Liquid_avg"]].sum().reset_index()
    df_inj_avg.drop(df_inj_avg[df_inj_avg['Normalized_months']<0].index, inplace = True)
    df_inj_avg = df_inj_avg.reset_index()
    df_inj_avg.drop('index', axis = 1, inplace = True)

    #Injection Chart
    fig,ax = plt.subplots()
    ax.plot(df_inj_avg['Normalized_months'], df_inj_avg['Liquid_avg'], color = "blue")
    ax.set_xlabel("Months Since First Production",fontsize=20)
    ax.set_ylabel("Liquid Injection, Stb/day",color="blue",fontsize=20)
    ax2=ax.twinx()
    ax2.plot(df_inj_avg['Normalized_months'], df_inj_avg['Gas_avg'],color="red")
    ax2.set_ylabel("Gas Injection, Mscf/day",color="red",fontsize=20)
    fig.set_size_inches(20, 8)

    st.pyplot(fig, figsize=(20, 8))

    #Cumulative Injection
    df_inj_cum = df_inj_avg[['Normalized_months']]
    df_inj_cum['Gas_cum']= (df_inj_avg['Gas_avg']/1000000).cumsum()
    df_inj_cum['Liquid_cum']= (df_inj_avg['Liquid_avg']/1000000).cumsum()

    fig,ax = plt.subplots()
    ax.plot(df_inj_cum['Normalized_months'], df_inj_cum['Liquid_cum']*30.44, color = "blue")
    ax.set_xlabel("Months Since First Production",fontsize=20)
    ax.set_ylabel("Cumulative Liquid Injection, MMStb",color="blue",fontsize=20)
    ax2=ax.twinx()
    ax2.plot(df_inj_cum['Normalized_months'], df_inj_cum['Gas_cum']*30.44,color="red")
    ax2.set_ylabel("Cumulative Gas Injection, Bscf",color="red",fontsize=20)
    fig.set_size_inches(20, 8)

    st.pyplot(fig, figsize=(20, 8))
    st.markdown(' ##### Cum Gas Injected : {:.2f} Billion scf, Cum Liquid Injected : {:.2f} Million STB '.format(df_inj_cum.Gas_cum.max()*30.44, df_inj_cum.Liquid_cum.max()*30.44))
#Create graphs and whatever else you want to show.

#streamlit run Alaskan_oil_app.py

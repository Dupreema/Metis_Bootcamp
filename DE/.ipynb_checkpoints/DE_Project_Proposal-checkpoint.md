<center> 
    
# DE Project Proposal 
##### - Matthew Dupree
## Question/Need:
### *1. What is the framing question of your analysis, or the purpose of the model/system you plan to build?*

#### Petroleum engineers (specifically reservoir and production engineers) often use the same 3-4 charts for preliminary investigation into a producing facies of rock in a specific basin/pool of oil.  These charts can be applied on individual wells, or a group of wells that produce in the same region (and thus are linked).  

#### Specifically, the charts that are used to investigate a producing facies/pool of oil are: oil, water, and gas production over time; cumulative oil, water and gas production; water and gas injection over time; cumulative water and gas injection over time; and a decline curve to predict future oil production.  

#### The purpose of this data pipeline is to provide oil companies with a free and easy visualization of these charts, along with other relevant information for the wells they are investigating.

### *2. Who benefits from exploring this question or building this model/system?*

#### The database used in this pipeline is conventional production/injection from Alaska. This pipeline will primarily be useful for Alaska-based companies but will be easily adjusted to be used on confidential company production/injection data.  Thus, any oil and gas company can benefit from this data pipeline. In fact, a company named Q Engineering built something similar and sold it to a oil and gas production website named Enverus.

## Data Description:
### *3. What dataset(s) do you plan to use, and how will you obtain the data?*
#### In order to perform this analysis, I will use [Alaskan public oil and gas data](http://aogweb.state.ak.us/DataMiner3/Forms/Default.aspx). More specifically, the production and injection time-series data by well.

### *4. What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?*
#### The data that is provided for this analysis (oil, water and gas production; water and gas injection; and days of production/injection in the prior month). The production and injection volumes are in stb or bbl (42 gal at standard temperature and pressure). The other information that will be used includes: the specific pool of oil, area, and well identifiers.

### *5. If modeling, what will you predict as your target?*
#### One of the visualizations I will be using is a decline curve model which is commonly used in oil and gas using this general equation.

<center><img src="Standard_Arps.png"/>
    
##### di is the initial decline rate in %/year, q is current production, qi is initial production, and b is the arps b factor which will be fit to the data.
    
## Tools:
### *6. How do you intend to meet the tools requirement of the project?*
#### I will use a SQL Database to store the data and then move the data into Python via SQLAlchemy. I will attempt to make the database update monthly with the online Alaskan data source. Pandas, numpy, matplotlib and scipy wil be used to clean, analyze and create the visualizations.  Then streamlit and possibly plotly will be used to provide the user access of the analysis.

### 7. Are you planning in advance to need or use additional tools beyond those required?
#### I am planning to use plotly if possible to have an interactive display.

## MVP Goal:

### *8. What would a minimum viable product (MVP) look like for this project?*
#### The minimum viable product for this data pipeline would use a non-updating sql database for data ingestion. It would have all the plots besides the decline curve.  It would have a table of outputs for the user.  It would also be implemented on streamlit for user access.
# Project Proposal - Matthew Dupree


## Question/Need:
### 1. What is the framing question of your analysis, or the purpose of the model/system you plan to build?

#### A company in New York reached out to me with hopes of re-opening in the near future.  They would like to set up a flexible and safe program for re-opening that involves reducing employee exposure to covid on public transportation for employees that elect to return to in-office operations.  The purpose of this analytical investigation is to identify the best times for employees to travel on the New York Subway system to reduce risk of covid exposure.  The company would change the working hours of employees to fit

### 2. Who benefits from exploring this question or building this model/system?

#### The (non-disclosed) company that hired me to do the investigation and the employees of the company.

## Data Description:
### 3. What dataset(s) do you plan to use, and how will you obtain the data?
#### In order to perform this analysis, I will only be using the MTA data that was provided

### 4. What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?
#### The data that is provided for this analysis (C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS). The C/A, Unit, and SCP together identify a single turnstyle in a station.  I will ultimately use the total station entries and exits to identify key busy times for stations in the area.  Ideally, I would then be able to group locations of New York and identify a low risk route/time for a few locations this will use the linename, location, and traffic through the station.

### 5. If modeling, what will you predict as your target?
#### This project will involve no modeling.

## Tools:
### 6. How do you intend to meet the tools requirement of the project?
#### I will use a SQL Database to store the data and then move the data into Python via SQLAlchemy. Pandas, Matplotlib, and potentially numpy will be used to clean, analyze and display the data. If the project goes smoothly, I will try to use plotly to interactively display my analysis.  If I run into struggles I will contact an instructor, look through provided resources, and use google.

### 7. Are you planning in advance to need or use additional tools beyond those required?
#### I am planning to use plotly if possible to have an interactive display.

## MVP Goal:

### 8. What would a minimum viable product (MVP) look like for this project?
#### The minimum viable product for this project would involve a clearly defined backstory, using the MTA data, using in-class tools to clean, analyze and visualize the data,and an on-time delivery of a good presentation.
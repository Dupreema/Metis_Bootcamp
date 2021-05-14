# EDA on New York MTA Data (12/2020 - 3/20/21)
#### By Matthew Dupree

## Abstract

The goal of this project was to provide recommendations to a New York company by using exploratory data analysis to identify key times and key stations for employees to travel on to reduce covid-19 exposure risk when re-opening the office. 

The concluding recommendation of this analysis is to implement an optional return to in-office work with travel times between noon and 2:00 PM, and between 8:00 PM and 10:00 PM.  The HR company should implement the Station activity rank tool to recommend stations and routes to employees.


## Design
A company in New York reached out to me with the hope of reopening their office on the back end of the covid-19 pandemic.  In considering their options, they asked me for recommendations for employee travel to reduce exposure risk from covid-19. All decisions in my analysis were built toward answering this question for the client: How can employees travel on public transit in the safest way possible?


## Data
The data set that I used in this analysis was the [MTA Turnstile](http://web.mta.info/developers/turnstile.html) data.  I decided to used the most recent 3-month period of MTA data because I believe it is the most representative of current travel conditions in New York. 

## Algorithms

1. Cleaning the data consisted of compiling columns into more useful columns for the analysis and dropping columns that were redundant and rows that were null. I also chose to exclude the recover audit because it did not contribute to my analysis.
2. Aggregation and formatting of the data took place throughout the analysis when necessary.  The main dataframes that I needed for this analysis were the 4-hour activity for each station on each weekday, and daily activity for each station on each weekday.
3. The data was then shown through a number of seaborn visualisations that were targetted to help answer the project goal.


## Tools

- SQL for data storage
- SQLAlchemy for extraction into python
- Pandas for cleaning and analyzing the data
- Seaborn for visualization

## Communication
The key points of the project are stated clearly, and the project goal is answered through the presentation.

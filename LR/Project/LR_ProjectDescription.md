# Regression on Nonprofit: Form 990 Tax Filings (12/2020 - 3/20/21)
#### By Matthew Dupree

## Abstract

The goal of this project is to provide recommendations to small and medium sized nonprofit organizations on executive team pay.  To perform this analysis, tax forms were scraped for relevant information such as nonprofit revenues and number of voting members.  A regression was performed on relevant features to attempt to provide this reccommendation.

The concluding recommendation of this analysis is to use a polynomial regression for current predictions.  The model has a train R2 value of 0.44 and a test R2 value of 0.38.  Future recommendations should come from a random forest model.


## Design
Nonprofit executive salaries are a topic that is likely to impact support of the public.  By performing an analysis and reccommendations to nonprofit organizations, outlier organizations can be identified and investigated, and smaller nonprofits can remain in the favor of the public.


## Data
The data set that I used in this analysis was form 990 tax filing information from [propublica.org](https://projects.propublica.org/nonprofits).  The features that seemed important to me when I started scraping were: number of voting members, number of employees, total revenues, total expenses, total assets, total liabilities, amount paid in salaries, whether the organization had an independent or biased audit, and the where the revenues came from (public support, investments, or services). Many of these features ended up being collinear as proxies for organization size. 


## Algorithms

1. Cleaning the data consisted of some data engineering like aggregating a few features.  I also did a number of drops on my data for data that was either not relevant, or extreme outliers.  I found that hospitals, universities, and government funds were often outliers.  
2. The data was eventually narrowed down to: number of voting members, total revenues, total assets, binary for independent audit, and the percent revenues. 
3. The analyses used for this regression problem were: a simple linear regression, a polynomial regression, a lasso regression, and a random forest regression.
4. The visualizations include plots of actual vs predicted, and residual plots.

## Tools

- Selenium & BeautifulSoup for webscraping
- Pandas for cleaning and analyzing the data
- Seaborn & Matplotlib for visualization
- Sklearn & Statsmodels for regression

## Communication
The key points of the project are stated clearly, and the project goal is answered through the presentation.

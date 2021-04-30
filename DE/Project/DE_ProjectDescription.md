# **Alaska Oilfield Pipeline Application**
#### By Matthew Dupree

## Abstract

The goal of this project is to provide an application to petroleum engineers looking to perform simple investigstion into Alaskan oil fields.  To create this application, a data pipeline was formed from the public oilfield data of Alaska.   Simple visualizations were performed in the application

The final application for this pipeline includes visualizations of production rates, cumulative production, production ratios, a foundation for decline curve analysis, injection rates, and cumulative injection volumes.

## Design
All petroleum engineers perform the same initial analysis into reservoirs/pools of oil for a basic understanding of the reservoirs. A number of expensive applications such as OFM (Oil Field Manager) are built off of these fundamental visualizations.  By streamlining the visualization process, petroleum engineers will be able to perform a simple investigation very quickly and will be able to dedicate more time to other investigations.  Although, currently, these visualizations are limited to Alaskan data, the application can be easily expanded to accomodate other sources of production data.


## Data
The data set that I used in this analysis was Alaskan production, injection, and location data from [The Alaskan public database](https://www.commerce.alaska.gov/web/aogcc/Data.aspx).  The most important features of this data were the production volumes per month, injection volumes per month, and relevant data such as the well, field, pool of oil, and dates.


## Algorithms

1. Cleaning the data consisted of some data engineering such as aggregating a features. It also involved adjustment of rate and date data to perform my analysis and visualizations.
2. The visualizations for this analysis included: production and injection rates/cumulatives, production ratios, and the first steps towards decline curve analysis.

## Tools

- SQL for Data storage
- Sqlalchemy for queries
- Pandas for cleaning temporary storage of data
- Matplotlib for visualizations
- Scipy for decline parameter optimization (future)

## Communication
The key points of the project are stated clearly, and the project goal is answered through this project description and the presentation.

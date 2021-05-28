# **Investment diversification using NLP**
#### By Matthew Dupree

## Abstract

Companies are often involved in several sectors, for example, Amazon is involved in the retail sector (product sales), the services sector (package delivery) and the tech services sector (cloud computing).  The major stock exchanges define sector definitions for the market. The goal of this project is to rethink market sectors to encourange an unbiased investment for true risk reduction through investment diversification.  

We live in a time where growth stocks are king- and the premium one pays for the cash flows of growth stocks and certain sectors can be outrageous. For example, Tesla is trading at a upwards of a 500 price/earnings ratio while oil and gas stocks are trading at an average price/earnings ratio of about 17.

By redefining sectors based on company and investor priorities, I believe that more reasonable sector separations can be established.  For example, Tesla is formally defined as a car manufacturer, but by my model it was classified as an energy stock due to its priorities of emission reduction and sustainable energy production.

## Design
In order to redefine market sectors, I used recent earnings call transcripts from each company. Earnings call transcripts include pre-recorded statements on the quarterly results of the company.  This often includes discussion of the company goals and struggles.  After the pre-recorded statements, investors ask questions to company management- this is where the investor priorities are shown.  My hope was that, through the company and investor discussions about the company, NLP could be used to determine more clear sector distinction.  With these new sector distinctions, I provided four investment strategies including: sector weighted diversification, 2x tech weighted diversification, an income-based strategy (which maximize dividend yields), and an inflation-hedge strategy.


## Data
The earnings call transcripts that I scraped can be found at [seekingalpha.com]  (https://seekingalpha.com).  Each of the 4,000 available transcripts consisted of ~10,000 words.  After Natural language processing, there were about 8500 words that were used for modeling.

Supplemental data was collected from [stockanalysis.com](https://stockanalysis.com/stocks/) including company market capitalizations, earnings per share, P/E ratios, and dividend yields.  This data was used post-sector separation to provide diversification advice to potential investors.

## Algorithms

1. Cleaning the data consisted of regex and nltk to set the text up for the document-term matrix
2. tf-idf and NMF were used to perform the dimensionality reduction and hard topic classification.
3. The visualizations and insights from this analysis were established with simple data manipulations.

## Tools

- Selenium and beautifulsoup for webscraping
- regex and nltk for text cleaning
- tf-idf vectorizer for creation of document-term matrix
- NMF for dimensionality reduction into topics
- numpy and matplotlib for visualizations and data manipulation

## Communication
The key points of the project are stated clearly, and the project goal is answered through this project description and the presentation.

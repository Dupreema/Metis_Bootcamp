# Exxon Stock Price Project Proposal - Matthew Dupree


## Question/Need:
### 1. What is the framing question of your analysis, or the purpose of the model/system you plan to build?
#### I would like to identify the key factors that affect Exxon stock price to create an idea of what to expect in different market conditions.

### 2. Who benefits from exploring this question or building this model/system?
#### Investment firms and other investors of Exxon stock.  This analysis could also be an indicator for other energy stock owners.

## Data Description:
### 3. What dataset(s) do you plan to use, and how will you obtain the data?
#### In order to perform this analysis, I will be scraping pricing (Exxon, Oil, Gold, Dow, 10-year treasuries, Exxon dividends, and XLE) data off of yahoo finance tables and more broad data from multpl tables (GDP, P/E).

### 4. What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?
#### The data that is provided for this analysis will be (Oil Price,Gold Price, 10 year Treasury yields, Dow Jones price, Market P/E,US GDP, and potentially the XLE). Oil price is expected to be the strongest influencer of Exxon stock price. Oil price will reflect for different global conditions such as terrorist acts in the Middle East, exiting the Paris Climate accord, and global supply/demand.  Gold price will act as a proxy for non-oil commodities. Exxon functions with a large amount of debt, and the cost of this debt will be reflected by the 10-year treasury yields.  Dow Jones will give an idea of US market sentiment that may affect Exxon price. Market P/E ratio will reflect the premium of the stock market (how many market participators and at what scale). The US GDP growth rate will reflect real growth in global value. I expect exxon to perform better with higher global growth.  XLE (energy index) should allow us to see if Exxon outperforms or underperforms other oil-based stocks.

### 5. If modeling, what will you predict as your target?
#### I will be predicting exxon stock price, or more accurately, determining the impact of these features on Exxon stock price.

## Tools:
### 6. How do you intend to meet the tools requirement of the project?
#### I will use both BeautifulSoup and Selenium to scrape the data off of yahoo finance and multpl.  I will use pandas to store data in a useable format/perform EDA and sklearn to perform my regression analysis.

### 7. Are you planning in advance to need or use additional tools beyond those required?
#### Right now, I am not planning on using any tools or packages that haven't been touched on in class.

## MVP Goal:

### 8. What would a minimum viable product (MVP) look like for this project?
#### The minimum viable product for this project would include a clear intention, successful scraping of the data from the web, simple EDA, and a basic regression on all of my data.
<center> 
    
# **NLP Project Proposal**
##### **- Matthew Dupree**
## Question/Need:
### **1. What is the framing question of your analysis, or the purpose of the model/system you plan to build?**

#### For investors, diversification is a key concept that allows them to minimize risk exposure.  We live in a time where growth stocks are king- and the premium one pays for the cash flows of growth stocks and certain sectors can be outrageous. For example, Tesla is trading at a 903 price/earnings ratio while oil and gas stocks are trading at about a 3 price/earnings ratio. This means that for a given earnings of the company, an investor is paying 903 X those earnings for a tesla and 3X those earnings for an energy company. The historical average P/E is around 20x earnings (shocking, I know). The 2021 P/E average is almost 44.

#### Right now, the markets are heavily weighted towards technology and healthcare, which tend to be the favored assets by this generation.  Unfortunately, though, by investing in these assets, an investor is paying a significant premium for their bias.  Warren Buffett, one of this generation's greatest investors, once said "Price is what you pay. Value is what you get."  I happen to believe there is great value in many assets that investors don't think twice about because it isn't in their preference or what they frequently hear about.  
    
#### I think it is time the investors re-think their diversification strategy and risk exposure to reflect the true value of stocks.  My hope is to create a model that, looking at earnings-call transcripts, can distinguish between sectors based on sector priorities and jargon, which will then allow an investor to diversify among these (newly defined) sectors in an unbiased manner.

### **2. Who benefits from exploring this question or building this model/system?**

#### Entry-level investors who are easily lead by broad public opinion and need help with a diversification strategy. This method of sector separation may also allow practiced investors to identify particular groups of stocks that are being overlooked in their investing strategies.

## Data Description:
    
### **3. What dataset(s) do you plan to use, and how will you obtain the data?**
    
#### In order to perform this analysis, I plan to use earnings-call transcripts from Q1 2021 to identify different groups of stocks based on jargon, priorities, and investor questions.
    
#### I believe that the language used on earnings-calls will be able to distinguish different company types based on the jargon and language that is used.

### **4. What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?**
#### The data that is provided for this analysis includes a discussion of the quarterly earnings of the company as well as investor analyst questions regarding the actions/trajectory/hopes of the company.
    
    
### **5. If modeling, what will you predict as your target?**

#### Ideally, the underlying structure of the earnings calls will reveal sectors based on the language used. If not, my hope is that the underlying structure of the language will reveal the company priorities such as whether its investment interest relies on growth/earnings/commodity exposure, etc.

    
## Tools:
### **6. How do you intend to meet the tools requirement of the project?**
#### I will scrape the data off of seeking-alpha.  I will then perform NLP using regex and nltk.  I will adjust the 'english' stop-words list to include non-sector specific jargon.  I will then reduce the dimensions of the text and attempt different forms of clustering to identify groups of companies.

### **7. Are you planning in advance to need or use additional tools beyond those required?**
#### I am not planning to use additional tools at this point.

## MVP Goal:

### **8. What would a minimum viable product (MVP) look like for this project?**
#### An MVP would include: acquiring the data, cleaning the data, dimensional reduction, and a baseline clustering method.
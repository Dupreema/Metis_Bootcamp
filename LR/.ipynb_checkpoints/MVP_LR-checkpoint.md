
### <center> **Analysis of Non-Profit Executive Pay** 
#### <center>The goal of my project is to identify salary recommendations for non-profit organizations looking to offer executives pay.<center>



<center><img src="YvsPred.png"/>
 
##### <center> Above, my first attempt at a regression is shown.  On the X-axis, Y is shown, on the Y-axis, the model prediction is shown.
    
<center><img src="OLSModel1.png"/>
    
##### <center> Above, the statsmodel summary is shown for the model that I used.  The R-squared is ~0.3 as a baseline for the model.
    
<center><img src="PredictvsResiduals.png"/>
    
     
##### <center> Above, the residuals for the model prediction are shown. The X-axis is the model prediction and the Y-axis shows the residuals of these predictions.  The predictive accuracy of the model seems to decrease at executive compensation values that are very large.  Right now, this model has ~390 points of data. The scraping is interrupted about every 40 new points so I am going through and adding about 40 at a time.   
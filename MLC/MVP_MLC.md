
### <center> **Rock Type Classification using Well Logs** 
#### <center> The goal of this project is to perform Lithological classification on wells in the Vovle field. Lithological classification is always done in wells to understand the geologic properties of the near-wellbore region.  This model will serve to perform this analysis in a simplified manner for free. <center>

<center><img src="Lithological_Classification.png" width="400"/>
     
#### <center> Above, is a visual representation of how different logging properties can indicate the presence of distinct rock-types near a well.  
    
<center><img src="Model_classification.png"/>
 
#### <center> Above, my first attempt at rock-type classification is shown.  A random-forest classification model was used, prioritizing the f1 score.  The right-most column represents the model's rock-type predictions and the column next to it represents the actual rock-type that is represented for this well at this depth.  The model currently has an accuracy of 0.72 and a confusion matrix as shown below. (0 is shale, shown in gray laminations, 1 is limestone shown in teal blocks, and 2 is sandstone shown in granular yellow)
   
<center><img src="Model_confusion_matrix.png" width="400"/>
 
#### <center> This model currently seems to struggle with distinguishing between limestone and sandstone.  This is a reasonable struggle for the model to have, as the RHOB (density) is the strongest distinguisher between the two.
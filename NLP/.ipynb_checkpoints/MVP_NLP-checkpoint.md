
### <center> **Investment diversification using NLP** 
#### <center> The goal of this project is to rethink market sectors to encourange an unbiased investment for true risk reduction through investment diversification.  <center>

<center><img src="Document_topic_mat.png" width="600"/> <center>
     
#### <center> Above, the document-topic matrix is shown. My analysis started with text pre-processing, stop-word-additions, tf-idf vectorization, and NMF for the dimensionality reduction from ~8500 unique words to 5 topics. Further cleaning, such as stemming is needed using nltk. Investigations into models and topic numbers have just started. 
    
<center><img src="Top_words.png" width="400"/> <center>
 
#### <center> Above, the top 6 words are shown for each topic.  The sector separations thus far are as follows: Tech/IT, Pharma/med, finance/banking, Energy/oil, Retail/apparel.  I believe the sectors can be further split and refined.  There seem to be clear sector separations.
 
#### <center> What needs to be done now: stemming/further language preprocessing (although I have already processed 32,000,000 words down to 8490), model/topic number selection, and application of data to perform recommendations to investors by model-defined sector.
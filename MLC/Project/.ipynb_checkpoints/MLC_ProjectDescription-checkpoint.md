# **Rock Type Classification using Well Logs**
#### By Matthew Dupree

## Abstract

The goal of this project is to perform Lithological classification on wells in the Vovle field. Lithological classification is always done in wells to understand the geologic properties of the near-wellbore region.

Because of the cost of data collection, the quantity of the data decreases as the data collection technique moves from higher areal coverage to lower areal coverage.  For this project, I used well logs to create a classification model for near-wellbore rock type.  The classification will consist of 3 classes: Limestone, shale, and sandstone.

The resulting recommendation/model is an XGBoost model with an F1-score of 0.825. This model will serve to perform lithological analysis in a simplified manner for free. Geologists, reservoir engineers, and small oil companies can benefit from this analysis.

## Design
In order to understand the geologic and fluid properties of the near-wellbore region, petroleum geologists perform the same initial analyses of log data. These analysis include lithological and fluid classifications.  The lithological properties are important to understand because they can have a large impact on the productivity of the producing regions and provide insight into different geologic layers you may be interacting with. By modeling the rock-type visualization, geologists and petroleum engineers can move on more quickly to in depth analysis of the reservoir.  Although, currently, these visualizations are limited to a few wells in the North Sea, the application of this classification model can be easily expanded to accomodate other sources of data.


## Data
The data set that I used in this analysis was the Volve field logging data from Equinor. [Found Here](https://www.equinor.com/en/what-we-do/digitalisation-in-our-dna/volve-field-data-village-download.html).  The most important log measurements for rock-type classification are: Gamma Ray response (GR), Neutron Porosity (NPHI), Bulk density (RHOB), Photoelectric absorption factor (PEF), Rate of penetration through the rock while drilling (ROP), Delta time of sound waves through the rock (DT), and resistivity of the formation (RT).  Resistivity is more often used for fluid-type classification than rock type classification, so it was excluded from the later models.

The target, rock-type, is determined by detailed analysis the rock fragments that are circulated to the surface from drilling through the rock .

## Algorithms

1. Cleaning the data consisted of dropping many of the unneccessary features in the data that don't pertain to rock-type classification. 
2. KNN, Random Forest, and XGBoost models were used.
3. The visualizations for this analysis are standard lithological visualizations used in the petroleum industry.

## Tools

- Microsoft Azure storage explorer for accessing the data
- Lasio for reading the .LAS files into python
- Pandas for cleaning and formatting the data
- Sklearn and xgboost for modeling
- Matplotlib and seaborn for visualizations

## Communication
The key points of the project are stated clearly, and the project goal is answered through this project description and the presentation.

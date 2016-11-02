# predict-wine-quality
Using Linear Regression to predict wine quality

#Analysis
When calculating the correlations for each wine type separately, I noticed the correlations between the columns and quality is not the same for red and white wine. This is the result of the correlation analysis
CORRELATIONS IN RED WINE DATE
fixed acidity           0.124052
volatile acidity       -0.390558
citric acid             0.226373
residual sugar          0.013732
chlorides              -0.128907
free sulfur dioxide    -0.050656
total sulfur dioxide   -0.185100
density                -0.174919
pH                     -0.057731
sulphates               0.251397
alcohol                 0.476166
quality                 1.000000

CORRELATIONS IN WHITE WINE DATE
fixed acidity          -0.113663
volatile acidity       -0.194723
citric acid            -0.009209
residual sugar         -0.097577
chlorides              -0.209934
free sulfur dioxide     0.008158
total sulfur dioxide   -0.174737
density                -0.307123
pH                      0.099427
sulphates               0.053678
alcohol                 0.435575
quality                 1.000000

the columns with somewhat close correlations are total sulfur dioxid and alcohol. For this reason I'm going to create a different linear regression model for each wine type first then will create a model for the combined data set

#Usage
python predict_wine_quality.py

# Data 
http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/

Attributes:
1. fixed acidity
2. volatile acidity
3. citric acid
4. residual sugar
5. chlorides
6. free sulfur dioxide
7. total sulfur dioxide
8. density
9. pH
10. sulphates
11. alcohol Output variable (based on sensory data): 
12. quality (score between 0 and 10)



#Citation
This dataset is public available for research. The details are described in [Cortez et al., 2009]. 
  
  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
  Modeling wine preferences by data mining from physicochemical properties.
  In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

  Available at: [@Elsevier] http://dx.doi.org/10.1016/j.dss.2009.05.016
                [Pre-press (pdf)] http://www3.dsi.uminho.pt/pcortez/winequality09.pdf
                [bib] http://www3.dsi.uminho.pt/pcortez/dss09.bib
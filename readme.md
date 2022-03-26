# **AryaAI - Assignment**

The problem statement is a binary classification one with 57 features and data points belonging to one of the two classes - 0 or 1. After loading the the training set in the notebook, the data was explored and following observations were made:

 1. The data had no null values.
 2. All the features consisted of numerical data. 
 3. Several features had more than three-fourths of all data points' values equal to the lower limit of the feature ranges indicating a skewed distribution of data in features.

Link to the  [Google collab Notebook](https://colab.research.google.com/drive/1kigZ7otC8XWrI-S0EuJoO5gqwpRtFcN-?usp=sharing)

**Pre-processing Step followed:**
1. Training data was split into feature and target sets. 
2. The features were scaled as a part of preprocessing.
3. Train/Test split was done to the training set to further split into training and testing sets in the ratio of 4:1.

**Model**
1. A total of four classfication models were trained using default parameters on the training set:
	1. XGBoost, 
	2. Random Forest Classifier,
	3. Logistic Regression and,
	4. Support Vector Machines,

2. The classification reports were generated for all the models and ***Random Forest*** was observed to provide best scores for the training set. Consequently, it was selected for hyperparameter tuning to further optimise the model performance.

**Model optimization:**
GridSearch, along with ***5-fold cross-validation*** was used to find out the optimum hyperparameters and model was trained on the training set to get the predicted results of the test set. 
A good score on the testing set eliminated the possibility of model being overfit.

**Feature Engineering**
After this, `feature_importance_` attribute was used to identify the features with least impact on the final target. These features were dropped to *reduce dimensionality* of the model and the model was again trained on the new training set with reduced features. 

**Model Interpretability**
Finally, SHAP values and LIME were used to interpret the feature contribution to final target variables. 

**Results on Test Data**
On loading the test set, the model predicted 268 instances belonging to class '1' and rest to class '0'.

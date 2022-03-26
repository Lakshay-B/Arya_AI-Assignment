The problem statement is a binary classification one with 57 features and data points belonging to one of the two classes - 0 or 1. After loading the the training set in the notebook, the data was explored and following observations were made:
1. The data had no null values.
2. All the features consisted of numerical data.
3. Several features had more than three-fourths of all data points' values equal to the lower limit of the feature ranges indicating a skewed distribution of data in features. 

Validation data was split into feature and target sets. The features were scaled as a part of preprocessing. 
Train/Test split was done to the training set to further split into training and testing sets in the ratio of 4:1.
A total of four classfication models, i.e, XGBoost, Random Forest Classifier, Logistic Regression and Support Vector Machines, were trained using default parameters on the training set. 
The classification reports were generated for all the models and Random Forest was observed to provide best scores for the training set. Consequently, it was selected for hyperparameter tuning to further optimise the model performance.
GridSearch, along with 5-fold cross-validation was used to find out the optimum hyperparameters and model was trained on the training set to get the predicted results of the test set. A good score on the testing set eliminated the possibility of model being overfit. 
After this, 'feature_importance_' attribute was used to identify the features with least impact on the final target. These features were dropped to reduce dimensionality of the model and the model was again trained on the new training set with reduced features. 
Finally, SHAP values and LIME were used to interpret the feature contribution to final target variables.
On loading the test set, the model predicted 266 instances belonging to class '1' and rest to class '0'.     

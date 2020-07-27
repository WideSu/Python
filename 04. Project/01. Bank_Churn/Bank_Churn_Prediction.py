#problem description and goal:
##use supervised learning models to identify customers who are likely to churn in the future
##analyze features that affects user retention
--------------------------------------------------------------------------------------------------------------------------------------------------------------------  
#load data:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('bank.data.csv')
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#part1: data information
##what the data looks like:
df.head(5)
  '''
  -> 	RowNumber	CustomerId	Surname	CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Exited
    0	        1	  15634602	Hargrave	  619	  France	Female	42	  2	0.00	         1	        1	            1	  101348.88	      1
    1	        2	  15647311	Hill	          608	  Spain	        Female	41	  1	83807.86	 1	        0	            1	  112542.58	      0
    2	        3	  15619304	Onio	          502	  France	Female	42	  8	159660.80	 3	        1	            0	  113931.57	      1
    3	        4	  15701354	Boni	          699	  France	Female	39	  1     0.00	         2	        0	            0	  93826.63	      0
    4	        5	  15737888	Mitchell	  850	  Spain         Female	43	  2	125510.82	 1	        1	            1	  79084.10	      0
  '''

##number of row and column:
print('Number of row: {}'.format(df.shape[0]))
print('Number of column: {}'.format(df.shape[1]))
  '''
  ->Number of rows: 10000
    Number of columns: 16
  '''
	
##check basic information:
df.info()
 '''
  -><class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10000 entries, 0 to 9999
    Data columns (total 14 columns):
     #   Column           Non-Null Count  Dtype  
    ---  ------           --------------  -----  
     0   RowNumber        10000 non-null  int64  
     1   CustomerId       10000 non-null  int64  
     2   Surname          10000 non-null  object 
     3   CreditScore      10000 non-null  int64  
     4   Geography        10000 non-null  object 
     5   Gender           10000 non-null  object 
     6   Age              10000 non-null  int64  
     7   Tenure           10000 non-null  int64   
     8   Balance          10000 non-null  float64
     9   NumOfProducts    10000 non-null  int64  
     10  HasCrCard        10000 non-null  int64  
     11  IsActiveMember   10000 non-null  int64  
     12  EstimatedSalary  10000 non-null  float64
     13  Exited           10000 non-null  int64  
     dtypes: float64(2), int64(9), object(3)
     memory usage: 1.1+ MB
  '''
	
##check if the values in each column are unique:
df.nunique()
  '''
  ->RowNumber          10000
    CustomerId         10000
    Surname             2932
    CreditScore          460
    Geography              3
    Gender                 2
    Age                   70
    Tenure                11
    Balance             6382
    NumOfProducts          4
    HasCrCard              2
    IsActiveMember         2
    EstimatedSalary     9999
    Exited                 2
    dtype: int64
##those numbers mean how many unique number each column has
    '''
	
##check missing value:
df.isnull().sum()
  '''
  ->RowNumber          0
    CustomerId         0
    Surname            0
    CreditScore        0
    Geography          0
    Gender             0
    Age                0
    Tenure             0
    Balance            0
    NumOfProducts      0
    HasCrCard          0
    IsActiveMember     0
    EstimatedSalary    0
    Exited             0
    dtype: int64
##also, we can check the missing value using df.info()
  '''

##statistical information:
###for those data, only 'CreditScore', 'Age', 'Tenure', 'NumOfProducts','Balance', 'EstimatedSalary' are the data that we care about statistical data
df[['CreditScore', 'Age', 'Tenure', 'NumOfProducts','Balance', 'EstimatedSalary']].describe()
  '''
  ->	    CreditScore	  Age	          Tenure	    NumOfProducts   Balance	        EstimatedSalary
    count 10000.000000	  10000.000000	  10000.000000	    10000.000000    10000.000000	10000.000000
    mean  650.528800	  38.921800	  5.012800	    1.530200	    76485.889288	100090.239881
    std	  96.653299	  10.487806	  2.892174	    0.581654	    62397.405202	57510.492818
    min	  350.000000	  18.000000       0.000000	    1.000000	    0.000000	        11.580000
    25%	  584.000000	  32.000000	  3.000000	    1.000000	    0.000000	        51002.110000
    50%	  652.000000	  37.000000	  5.000000	    1.000000	    97198.540000	100193.915000
    75%	  718.000000	  44.000000	  7.000000	    2.000000	    127644.240000	149388.247500
    max	  850.000000	  92.000000	  10.000000	    4.000000	    250898.090000	199992.480000
  '''

##boxplot for numerical feature:
_,axss = plt.subplots(2,3, figsize=[20,10]) #this means that the following boxplot will generate 6 graphs (in two rows and three columns), and each graph is 20*10 in size
sns.boxplot(x='Exited', y ='CreditScore', data=df, ax=axss[0][0])
sns.boxplot(x='Exited', y ='Age', data=df, ax=axss[0][1])
sns.boxplot(x='Exited', y ='Tenure', data=df, ax=axss[0][2])
sns.boxplot(x='Exited', y ='NumOfProducts', data=df, ax=axss[1][0])
sns.boxplot(x='Exited', y ='Balance', data=df, ax=axss[1][1])
sns.boxplot(x='Exited', y ='EstimatedSalary', data=df, ax=axss[1][2])
  '''
  ->image.1
  '''

##understand categorical feature:
_,axss = plt.subplots(2,2, figsize=[20,10])
sns.countplot(x='Exited', hue='Geography', data=df, ax=axss[0][0])
sns.countplot(x='Exited', hue='Gender', data=df, ax=axss[0][1])
sns.countplot(x='Exited', hue='HasCrCard', data=df, ax=axss[1][0])
sns.countplot(x='Exited', hue='IsActiveMember', data=df, ax=axss[1][1])
  '''
  ->image.2
  '''

##feature correlation:
corr_score = df[['CreditScore', 'Age', 'Tenure', 'NumOfProducts','Balance', 'EstimatedSalary']].corr()
print(corr_score)
  '''
  ->                 CreditScore       Age  ...   Balance  EstimatedSalary
    CreditScore         1.000000 -0.003965  ...  0.006268        -0.001384
    Age                -0.003965  1.000000  ...  0.028308        -0.007201
    Tenure              0.000842 -0.009997  ... -0.012254         0.007784
    NumOfProducts       0.012238 -0.030680  ... -0.304180         0.014204
    Balance             0.006268  0.028308  ...  1.000000         0.012797
    EstimatedSalary    -0.001384 -0.007201  ...  0.012797         1.000000
  '''
sns.heatmap(corr_score)
  '''
  ->image.3
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#part2: feature prepossessing 
##ordinal encoding:
###a classical ordinal feature is gender
df['Gender'] = df['Gender'] == 'Female'
  '''
  ->  Gender
	True	
	True	
	True	
	True	
	True	
	False	
	False	
	True	
	False	
	False
  '''

##one hot encoding:
df = pd.get_dummies(df, columns=['Geography'], drop_first=False)
df.head(10)
  '''
  ->    RowNumber	CustomerId	Surname	CreditScore  Gender	 Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Exited	Geography_France	Geography_Germany	Geography_Spain
    0	  1	        15634602	 Hargrave   619	      True	  42	  2	0.00	    1	          1	        1	              101348.88	      1	      1	                0	                0
    1	  2	        15647311	 Hill	    608	      True	  41	  1	83807.86    1	          0	        1	              112542.58	      0	      0	                0	                1
    2	  3	        15619304         Onio	    502	      True	  42	  8	159660.80   3	          1	        0	              113931.57	      1	      1	                0	                0
    3     4	        15701354	 Boni	    699	      True	  39	  1	0.00	    2	          0	        0	              93826.63	      0	      1	                0	                0
    4	  5	        15737888	 Mitchell   850	      True	  43	  2	125510.82   1	          1	        1	              79084.10	      0	      0	                0	                1
    5	  6	        15574012	 Chu	    645	      False	  44	  8	113755.78   2	          1	        0	              149756.71	      1	      0	                0	                1
    6	  7	        15592531	 Bartlett   822	      False	  50	  7	0.00	    2	          1	        1	              10062.80	      0	      1	                0	                0
    7	  8	        15656148	 Obinna	    376	      True	  29	  4	115046.74   4	          1	        0	              119346.88	      1	      0	                1	                0
    8	  9	        15792365	 He	    501	      False	  44	  4	142051.07   2	          0	        1	              74940.50	      0	      1	                0	                0
    9	  10	        15592389	 H?	    684	      False	  27	  2	134603.88   1	          1	        1	              71725.73	      0	      1	                0	                0
  '''

##drop useless column:
y = df['Exited'] #get target column at first
column_drop = ['RowNumber','CustomerId','Surname','Exited']
X = df.drop(column_drop, axis=1)
X.head()
  '''
  ->CreditScore	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Geography_France	Geography_Germany	Geography_Spain
  0	619	        True	  42	2	      0.00	    1	            1	        1	            101348.88	      1	                0	                0
  1	608	        True	  41	1	      83807.86	    1	            0	        1	            112542.58	      0	                0	                1
  2	502	        True	  42	8	      159660.80	    3	            1	        0	            113931.57	      1	                0	                0
  3	699	        True	  39	1	      0.00	    2	            0	        0	            93826.63	      1	                0	                0
  4	850	        True	  43	2	      125510.82	    1	            1	        1	            79084.10	      0	                0	                1
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#model training and data scaling:
##splite data into training and testing:
from sklearn import model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25, stratify = y, random_state=1)

##data scaling:
###standardization (x-mean)/std
###normalization (x-x_min)/(x_max-x_min) ->[0,1]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
##model training and selection:
###build models
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.linear_model import LogisticRegression
###Logistic Regression
classifier_logistic = LogisticRegression()
classifier_logistic.fit(X_train, y_train)
classifier_logistic.predict(X_test) #make prediction
classifier_logistic.score(X_test, y_test) #accuracy of test data
  '''
  ->0.808
  '''
###K Nearest Neighbors
classifier_KNN = KNeighborsClassifier()
classifier_KNN.fit(X_train, y_train)
classifier_KNN.predict(X_test)
classifier_KNN.score(X_test, y_test)
  '''
  ->0.8268  
  '''
###Random Forest
classifier_RF = RandomForestClassifier()
classifier_RF.fit(X_train, y_train)
classifier_RF.predict(X_test)
classifier_RF.score(X_test, y_test)
  '''
  ->0.8588
  '''

##5-fold cross validation:
model_names = ['Logistic Regression','KNN','Random Forest']
model_list = [classifier_logistic, classifier_KNN, classifier_RF]
count = 0
for classifier in model_list:
    cv_score = model_selection.cross_val_score(classifier, X_train, y_train, cv=5)
    print(cv_score)
    print('Model accuracy of ' + model_names[count] + ' is ' + str(cv_score.mean()))
    count += 1
  '''
  ->[0.81933333 0.80666667 0.80666667 0.80933333 0.82      ]
    Model accuracy of Logistic Regression is 0.8124
    [0.82533333 0.836      0.814      0.824      0.832     ]
    Model accuracy of KNN is 0.8262666666666666
    [0.878      0.86066667 0.85266667 0.86333333 0.86133333]
    Model accuracy of Random Forest is 0.8632
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#grid search to find optimal hyperparameters:
##think this method as traversing all possible hyperparameters and find the best one
from sklearn.model_selection import GridSearchCV

##logistic regression case:
###for logistic regression, we care about penalty and C
###penalty are choosen from l1 and l2, C can be choosen from multiple numbers
parameters = {'penalty':('l1', 'l2'),'C':(0.01, 1, 5, 10)}
Grid_LR = GridSearchCV(LogisticRegression(solver='liblinear'),parameters, cv=5) #cv means crossvalidation, 5 means 5-fold
Grid_LR.fit(X_train, y_train)
best_LR_model = Grid_LR.best_estimator_
print(best_LR_model)
  '''
  ->LogisticRegression(C=1, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=None, solver='liblinear', tol=0.0001, verbose=0,
                   warm_start=False)
  '''
	
##KNN case:
parameters = {'n_neighbors':[1,3,5,7,9]}
Grid_KNN = GridSearchCV(KNeighborsClassifier(),parameters, cv=5)
Grid_KNN.fit(X_train, y_train)
best_KNN_model = Grid_KNN.best_estimator_
print(best_KNN_model)
  '''
	->KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                     metric_params=None, n_jobs=None, n_neighbors=9, p=2,
                     weights='uniform')
  '''

##RF case:
parameters = {'n_estimators' : [40,60,80]}
Grid_RF = GridSearchCV(RandomForestClassifier(),parameters, cv=5)
Grid_RF.fit(X_train, y_train)
best_RF_model = Grid_RF.best_estimator_
print(best_RF_model)
  '''
	->RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=None, max_features='auto',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=60,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#confusion matrix:
from sklearn.metrics import confusion_matrix
##calculate accuracy, precision and recall, [[tn, fp],[]]
def cal_evaluation(classifier, cm):
    tn = cm[0][0]
    fp = cm[0][1]
    fn = cm[1][0]
    tp = cm[1][1]
    accuracy  = (tp + tn) / (tp + fp + fn + tn + 0.0)
    precision = tp / (tp + fp + 0.0)
    recall = tp / (tp + fn + 0.0)
    print (classifier)
    print ("Accuracy is: " + str(accuracy))
    print ("precision is: " + str(precision))
    print ("recall is: " + str(recall))
##print out confusion matrices
def draw_confusion_matrices(confusion_matricies):
    class_names = ['Not','Churn']
    for cm in confusion_matrices: #confusion_matrices is a list that contains classifier name and confusion matrix calculated using function in tuple type
        classifier, cm = cm[0], cm[1] #cm[0] is classifier name, cm[1] is the calculated confusion matrix
        cal_evaluation(classifier, cm)
        fig = plt.figure() #plt.figure plays a role as setup, it set how the figure looks like
        ax = fig.add_subplot(111) #this means the figure will be shown in 1 row and 1 column
        cax = ax.matshow(cm, interpolation='nearest',cmap=plt.get_cmap('Reds')) #matshow is a function that transform matrix into graph
        plt.title('Confusion matrix for ' + classifier) #set up the title of graph
        fig.colorbar(cax)
        ax.set_xticklabels([''] + class_names)
        ax.set_yticklabels([''] + class_names)
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.show()

##print 
confusion_matrices = [("Random Forest", confusion_matrix(y_test,best_RF_model.predict(X_test))),("Logistic Regression", confusion_matrix(y_test,best_LR_model.predict(X_test))),("K nearest neighbor", confusion_matrix(y_test, best_KNN_model.predict(X_test)))]
draw_confusion_matrices(confusion_matrices)
  '''
	->image.4
	->image.5
	->image.6
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------	
#ROC AUC:
##ROC x aixs is false positive rate, y axix is true positive rate
from sklearn.metrics import roc_curve
from sklearn import metrics
##ROC of RF:
###Use predict_proba to get the probability results of Random Forest
y_pred_rf = best_RF_model.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_pred_rf)
###make roc curve
plt.figure(1)
plt.plot([0, 1], [0, 1], 'k--') #draw diagonal
plt.plot(fpr_rf, tpr_rf, label='RF')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve - RF model')
plt.legend(loc='best')
plt.show()
  '''
  ->image.7
  '''
###calculate auc
from sklearn import metrics
metrics.auc(fpr_rf,tpr_rf)
  '''
  ->0.8306771434125471
  '''

##ROC of LR:
y_pred_lr = best_LR_model.predict_proba(X_test)[:, 1]
fpr_lr, tpr_lr, thres = roc_curve(y_test, y_pred_lr)
plt.figure(1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_lr, tpr_lr, label='LR')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve - LR Model')
plt.legend(loc='best')
plt.show()
  '''
  ->image.8
  '''
metrics.auc(fpr_lr,tpr_lr)
  '''
  ->0.7722314264879581
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#LR with feature selection:
X_with_corr = X.copy()
X_with_corr['SalaryInRMB'] = X['EstimatedSalary'] * 6.91 #this will cause SalaryInRMB correlate with EstimatedSalary
X_with_corr.head()
  '''
	->CreditScore	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	Geography_France Geography_Germany Geography_Spain SalaryInRMB
	0	619	True	42	2	0.00		1	1		1		101348.88	1			0	   0		   700320.7608
	1	608	True	41	1	83807.86	1	0		1		112542.58	0			0	   1		   777669.2278
	2	502	True	42	8	159660.80	3	1		0		113931.57	1			0	   0		   787267.1487
	3	699	True	39	1	0.00		2	0		0		93826.63	1			0	   0		   648342.0133
	4	850	True	43	2	125510.82	1	1		1		79084.10	0			0	   1		   546471.1310
  '''
	
##add L1 regularization to logistic regression
###L1 will randomly make one of those correlated features' coefficient small 
###check the coef for feature selection
scaler = StandardScaler()
X_l1 = scaler.fit_transform(X_with_corr)
LRmodel_l1 = LogisticRegression(penalty="l1", C = 0.1, solver='liblinear')
LRmodel_l1.fit(X_l1, y)
indices = np.argsort(abs(LRmodel_l1.coef_[0]))[::-1] #np.argsort will sort the array and return the original index
print ("Logistic Regression (L1) Coefficients")
for ind in range(X_with_corr.shape[1]):
	print ("{0} : {1}".format(X_with_corr.columns[indices[ind]],round(LRmodel_l1.coef_[0][indices[ind]], 4)))
	'''
	->Logistic Regression (L1) Coefficients
		Age : 0.7495
		IsActiveMember : -0.524
		Geography_Germany : 0.3171
		Gender : 0.2541
		Balance : 0.159
		CreditScore : -0.0569
		NumOfProducts : -0.0529
		Tenure : -0.0384
		EstimatedSalary : 0.0165
		HasCrCard : -0.013
		Geography_France : -0.0122
		SalaryInRMB : 0.0037 
		Geography_Spain : 0.0
		#salaryinrmb has a reletaive samll coefficient
	'''

##add L2 regularization to logistic regression
###L2 will make the correlated features same coefficient
###check the coef for feature selection
np.random.seed()
scaler = StandardScaler()
X_l2 = scaler.fit_transform(X_with_corr)
LRmodel_l2 = LogisticRegression(penalty="l2", C = 0.1, solver='liblinear', random_state=42)
LRmodel_l2.fit(X_l2, y)
LRmodel_l2.coef_[0]
indices = np.argsort(abs(LRmodel_l2.coef_[0]))[::-1]
print ("Logistic Regression (L2) Coefficients")
for ind in range(X_with_corr.shape[1]):
  print ("{0} : {1}".format(X_with_corr.columns[indices[ind]],round(LRmodel_l2.coef_[0][indices[ind]], 4)))
	'''
	->Logistic Regression (L2) Coefficients
		Age : 0.751
		IsActiveMember : -0.5272
		Gender : 0.2591
		Geography_Germany : 0.2279
		Balance : 0.162
		Geography_France : -0.1207
		Geography_Spain : -0.089
		CreditScore : -0.0637
		NumOfProducts : -0.0586
		Tenure : -0.0452
		HasCrCard : -0.0199
		EstimatedSalary : 0.0137
		SalaryInRMB : 0.0137
		#salaryinrmb and estimatedsalary have same coefficient
	'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#RF with feature importance:
###check feature importance of random forest for feature selection
forest = RandomForestClassifier()
forest.fit(X, y)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
print("Feature importance ranking by Random Forest Model:")
for ind in range(X.shape[1]):
  print ("{0} : {1}".format(X.columns[indices[ind]],round(importances[indices[ind]], 4)))
	'''
	->Feature importance ranking by Random Forest Model:
		Age : 0.2393
		EstimatedSalary : 0.1462
		CreditScore : 0.1441
		Balance : 0.1412
		NumOfProducts : 0.1295
		Tenure : 0.0829
		IsActiveMember : 0.0404
		Geography_Germany : 0.021
		HasCrCard : 0.0184
		Gender : 0.0184
		Geography_France : 0.0098
		Geography_Spain : 0.0089
	'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

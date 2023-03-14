import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, KFold, RandomizedSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from tqdm import tqdm
import numpy as np

data=pd.read_csv('Cleaned-Data.csv')

data = data.drop(['Country'], axis = 1)
data = data.drop(['Gender_Transgender'],axis = 1)
data = data.drop(['Severity_Mild'],axis = 1)
data = data.drop(['Severity_Moderate'],axis = 1)
#data = data.drop(['Severity_None'],axis = 1)
data = data.drop(['Severity_Severe'],axis = 1)

print(data.info())
#print(data.head())

#print(data.nunique())

X=data.drop('Severity_None', axis=1)
y=data['Severity_None']

#print(y)

RAND=0
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=RAND,test_size=0.2)

classifier=RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=RAND)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)

print(sklearn.metrics.confusion_matrix(y_test,y_pred))
print(sklearn.metrics.accuracy_score(y_test,y_pred))
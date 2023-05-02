import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv('diabetes_data_upload.csv')

RAND=0

#sns.displot(data['Age'])
#plt.show()
data.columns=['Age','Gender','Polyuria','Polydipsia','swl','weakness','Polyphagia', 'Genital thrush','visual blurring','Itching','Irritability','delayed healing','partial paresis','muscle stiffness','Alopecia','Obesity','class']
data['Gender'].replace('Female',0, inplace=True)
data['Gender'].replace('Male',1, inplace=True)
data['Polyuria'].replace('No',0, inplace=True)
data['Polyuria'].replace('Yes',1, inplace=True)
data['Polydipsia'].replace('No',0, inplace=True)
data['Polydipsia'].replace('Yes',1, inplace=True)
data['swl'].replace('No',0, inplace=True)
data['swl'].replace('Yes',1, inplace=True)
data['weakness'].replace('No',0, inplace=True)
data['weakness'].replace('Yes',1, inplace=True)
data['Polyphagia'].replace('Yes',1, inplace=True)
data['Polyphagia'].replace('No',0, inplace=True)
data['Genital thrush'].replace('Yes',1, inplace=True)
data['Genital thrush'].replace('No',0, inplace=True)
data['visual blurring'].replace('No',0, inplace=True)
data['visual blurring'].replace('Yes',1, inplace=True)
data['Itching'].replace('No',0, inplace=True)
data['Itching'].replace('Yes',1, inplace=True)
data['Irritability'].replace('Yes',1, inplace=True)
data['Irritability'].replace('No',0, inplace=True)
data['delayed healing'].replace('Yes',1, inplace=True)
data['delayed healing'].replace('No',0, inplace=True)
data['partial paresis'].replace('Yes',1, inplace=True)
data['partial paresis'].replace('No',0, inplace=True)
data['muscle stiffness'].replace('Yes',1, inplace=True)
data['muscle stiffness'].replace('No',0, inplace=True)
data['Alopecia'].replace('Yes',1, inplace=True)
data['Alopecia'].replace('No',0, inplace=True)
data['Obesity'].replace('Yes',1, inplace=True)
data['Obesity'].replace('No',0, inplace=True)

#print(data.info())

X=data.iloc[:,0:16].values
Y=data.iloc[:,16].values

X_train,X_test,y_train,y_test=train_test_split(X,Y,random_state=RAND,test_size=0.2)

# modesl=[]
# modesl.append(['LogisticRegression',LogisticRegression(random_state=RAND,solver='liblinear')])
# modesl.append(['RandomForestClassifier',RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=RAND)])
# modesl.append(['DecisionTreeClassifier',DecisionTreeClassifier(criterion='entropy',random_state=RAND)])
# modesl.append(['KNeighborsClassifier',KNeighborsClassifier(n_neighbors=30,metric='minkowski',p=1)])
# modesl.append(['gaus_classifier',GaussianNB()])
# modesl.append(['SVC',SVC(kernel='linear',random_state=RAND)])
#
# names=[]
# results=[]
# for name,model in modesl:
#     kfold=StratifiedKFold(n_splits=10,random_state=0,shuffle=True)
#     cv_cross=cross_val_score(model,X_train,y_train,cv=kfold,scoring='accuracy')
#     results.append(cv_cross)
#     names.append(name)
#     print(name,cv_cross.mean(),cv_cross.std())

def predict(data_list):
    classifier=RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=RAND)
    classifier.fit(X_train,y_train)
    #y_pred=classifier.predict(X_test)
    y_pred=classifier.predict([data_list])
    return y_pred


#print(sklearn.metrics.confusion_matrix(y_test,y_pred))
#print(sklearn.metrics.accuracy_score(y_test,y_pred))


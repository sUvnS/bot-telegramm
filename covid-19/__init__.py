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

data=pd.read_csv('covid_data.csv')
data2=pd.read_csv('Cleaned-Data.csv')

print(data.info())
#https://www.kaggle.com/datasets/meirnizri/covid19-dataset

data.pop('DATE_DIED')
#print(data.head())

#sns.displot(data['AGE'])
#plt.show()

data.columns=['USMER','MEDICAL_UNIT','SEX','PATIENT_TYPE','INTUBED','PNEUMONIA','AGE','PREGNANT','DIABETES','COPD','ASTHMA','INMSUPR','HIPERTENSION','OTHER_DISEASE','CARDIOVASCULAR','OBESITY','RENAL_CHRONIC','TOBACCO','CLASIFFICATION_FINAL','ICU',]
data['INTUBED'].replace(97,0,inplace=True)
data['INTUBED'].replace(99,0,inplace=True)
data['PREGNANT'].replace(97,0,inplace=True)
data['PREGNANT'].replace(99,0,inplace=True)
data['ICU'].replace(97,0,inplace=True)
data['ICU'].replace(99,0,inplace=True)
data['CLASIFFICATION_FINAL'].replace(2,1,inplace=True)
data['CLASIFFICATION_FINAL'].replace(3,1,inplace=True)
data['CLASIFFICATION_FINAL'].replace(4,2,inplace=True)
data['CLASIFFICATION_FINAL'].replace(5,2,inplace=True)
data['CLASIFFICATION_FINAL'].replace(6,2,inplace=True)
data['CLASIFFICATION_FINAL'].replace(7,2,inplace=True)

#print(data.info())

X=data.drop('CLASIFFICATION_FINAL', axis=1)
y=data['CLASIFFICATION_FINAL']

#print(X)
RAND=0
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=RAND,test_size=0.2)

#model=RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=RAND)


#modesl=[]
#modesl.append(['RandomForestClassifier',RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=RAND)])
#modesl.append(['DecisionTreeClassifier',DecisionTreeClassifier(criterion='entropy',random_state=RAND)])
#modesl.append(['KNeighborsClassifier',KNeighborsClassifier(n_neighbors=30,metric='minkowski',p=1)])
#modesl.append(['gaus_classifier',GaussianNB()])
#modesl.append(['SVC',SVC(kernel='linear',random_state=RAND)])

#names=[]
#results=[]
#for name,model in modesl:
#    kfold=StratifiedKFold(n_splits=10,random_state=0,shuffle=True)
#    cv_cross=cross_val_score(model,X_train,y_train,cv=kfold,scoring='accuracy')
#    results.append(cv_cross)
#    names.append(name)
#    print(name,cv_cross.mean(),cv_cross.std())

def predict(data,list):
    classifier=RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=RAND)
    classifier.fit(X_train,y_train)
    y_pred=classifier.predict(X_test)
    return y_pred

classifier=DecisionTreeClassifier(min_samples_split=60,max_depth=28,criterion='entropy')
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)

#print(sklearn.metrics.confusion_matrix(y_test,y_pred))
#print(sklearn.metrics.accuracy_score(y_test,y_pred))


df_final = pd.get_dummies(data, columns = ['USMER', 'MEDICAL_UNIT', 'SEX', 'PATIENT_TYPE', 'INTUBED', 'PNEUMONIA',
       'PREGNANT', 'DIABETES', 'COPD', 'ASTHMA', 'INMSUPR',
       'HIPERTENSION', 'OTHER_DISEASE', 'CARDIOVASCULAR', 'OBESITY',
       'RENAL_CHRONIC', 'TOBACCO', 'ICU'])
def model_eval(model, param, df_final, y):
    outer_cv = KFold(n_splits = 5, shuffle = True, random_state = 0)
    inner_cv = KFold(n_splits = 5, shuffle = True, random_state = 0)
    random = RandomizedSearchCV(model, param, scoring = 'accuracy', n_jobs = -1, cv = inner_cv, random_state = 0, n_iter =1)
    scores = []
    n_iter = random.n_iter
    with tqdm(total = n_iter) as pbar:
        for i in range(n_iter):
            random.set_params(n_iter = 1)
            for train_index, test_index in outer_cv.split(df_final, y):
                trainx, testx = df_final.iloc[train_index], df_final.iloc[test_index]
                trainy, testy = y[train_index], y[test_index]
                random.fit(trainx, trainy)
                scores.append(random.best_estimator_.score(testx, testy))
            pbar.update()
    print(random.best_params_)
    print('Average score', np.mean(scores))

model = ExtraTreesClassifier()
criterion = ['gini', 'entropy']
max_depth = np.array(range(50, 150))
min_samples_split = np.array(range(1, 100))
n_estimators = np.array(range(100,300, 2))
param = {'criterion': criterion, 'max_depth': max_depth, 'min_samples_split': min_samples_split, 'n_estimators': n_estimators}
print(model_eval(model, param, df_final, y))


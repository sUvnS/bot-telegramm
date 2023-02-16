import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('covid_data.csv')

data.pop('DATE_DIED')
print(data.head())

#sns.displot(data['AGE'])
#plt.show()

data.columns=['USMER','MEDICAL_UNIT','SEX','PATIENT_TYPE','INTUBED','PNEUMONIA','AGE','DIABETES','PREGNANT']
data['INTUBED'].replace(97,0,inplace=True)
data['INTUBED'].replace(99,0,inplace=True)
data['PREGNANT'].replace(97,0,inplace=True)
data['PREGNANT'].replace(99,0,inplace=True)

print(data.head())
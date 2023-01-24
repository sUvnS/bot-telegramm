import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('diabetes_data_upload.csv')

#sns.displot(data['Age'])
#plt.show()
data.columns=['Age','Gender','','','','','']
data['Gender']=data.label.map({'Male':0,'Female':1})
print(data.head())
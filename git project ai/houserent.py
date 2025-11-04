import pandas as pd
from PIL.GimpGradientFile import linear
from sklearn import preprocessing,model_selection,linear_model,metrics
import numpy as np
import matplotlib.pyplot as plt
#load data
print('-'*30);print('importing data');print('-'*30)
data=pd.read_csv('brazilianhouses.csv',sep=',')
data=data[['city','rooms','bathroom','parking.spaces','fire.insurance',
           'furniture','rent.amount']]
print(data.head())

#process data
data['rent.amount']=data['rent.amount'].map(lambda i:int(i[2:].replace(',','')))
data['fire.insurance']=data['fire.insurance'].map(lambda i:int(i[2:].replace(',','')))
le=preprocessing.LabelEncoder()
data['furniture']=le.fit_transform(data['furniture'])
print(data.head())
print('-'*30);print('checking null data');print('-'*30)
print(data.isnull().sum ())
#data=data.dropna()
#split data
x=np.array(data.drop(['rent.amount'],axis=1))
y=np.array(data[['rent.amount']])
print(x.shape)
print(y.shape)
xtrain,xtest,ytrain,ytest=model_selection.train_test_split(x,y,test_size=0.2)
print(xtrain.shape)
print(xtest.shape)

#trainning
print('-'*30);print('trainning data');print('-'*30)
model= linear_model.LinearRegression()
model.fit(xtrain,ytrain)
accuracy=model.score(xtest,ytest)
print("coefficients:",model.coef_)
print("intercept:",model.intercept_)
print('accuracy:',round(accuracy*100,2),'%')

##evaluation
print('-'*30);print('evaluation');print('-'*30)
ypred=model.predict(xtest)
print(ypred.shape)
error=[]
for i,test in enumerate(ypred):
    error.append(ytest[i]-test)
    print('actual:',ytest[i],' predicion:',int(test),' error:',int(error[i]))

# Mean Squared Error
mse = metrics.mean_squared_error(ytest, ypred)
print("Mean Squared Error:", round(mse, 2))

# -----------------------------
# Plot results
# -----------------------------
plt.figure(figsize=(8,6))
plt.scatter(ytest, ypred, color='blue', alpha=0.6, label='Predicted vs Actual')
plt.plot([ytest.min(), ytest.max()], [ytest.min(), ytest.max()], color='red', linewidth=2, label='Ideal Fit (y=x)')
plt.title('Actual vs Predicted Rent Amounts')
plt.xlabel('Actual Rent Amount')
plt.ylabel('Predicted Rent Amount')
plt.legend()
plt.grid(True)
plt.show()
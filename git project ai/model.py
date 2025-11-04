from sklearn import model_selection
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import random
#model F=1.8*C+32
#=1.8X+32 Y=MX+C
x=list(range(0,10))
y=[f*1.8+32+random.randint(-1,1) for f in x]
print('X:',x)
print('Y:',y)
plt.plot(x,y,'-*r')
plt.show()
x=np.array(x).reshape(-1,1)
y=np.array(y).reshape(-1,1)
#model
xtrain, xtest, ytrain,ytest =model_selection.train_test_split(x,y,test_size=0.2)
model=linear_model.LinearRegression()
model.fit(xtrain,ytrain)
accuracy=model.score(xtest,ytest)
print('accuracy:',round(accuracy*100,2))
print('m:',model.coef_)
print('c:',model.intercept_)
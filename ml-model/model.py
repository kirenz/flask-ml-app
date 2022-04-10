from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

df = pd.read_csv('prices.csv')

y = df['Value'] # dependent variable
X = df[['Rooms', 'Distance']] # independent variables

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lm = linear_model.LinearRegression()
lm.fit(X_train, y_train) # fitting the model
pickle.dump(lm, open('model.pkl','wb')) # save the model

print(lm.predict([[15, 61]]))  # format of input
print(f'score: {lm.score(X, y)}')

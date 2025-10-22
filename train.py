import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import joblib

from sklearn.ensemble import RandomForestRegressor

calories_file_path = 'data/calories.csv'
calories_data = pd.read_csv(calories_file_path)

calories_data = calories_data.dropna(axis=0)


y = calories_data.Calories

features = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
X = calories_data[features].copy()
X['Gender'] = X['Gender'].str.strip().str.lower().map({'male':1, 'female':0})



train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

model = RandomForestRegressor(random_state=1)
model.fit(train_X, train_y)
model_predictions = model.predict(val_X)
model_mae = mean_absolute_error(val_y, model_predictions)



print(f"Validation MAE for Random Forest Model: {model_mae:,.0f}")

from sklearn.metrics import r2_score
from sklearn.dummy import DummyRegressor


r2 = r2_score(val_y, model_predictions)
print(f"R²: {r2:.3f}")


dummy = DummyRegressor(strategy="mean")
dummy.fit(train_X, train_y)
dummy_preds = dummy.predict(val_X)
dummy_mae = mean_absolute_error(val_y, dummy_preds)
print(f"Baseline (mean) MAE: {dummy_mae:,.0f}")


joblib.dump(model, 'trained/calories_model.joblib')

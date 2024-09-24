# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset (assuming you have a CSV file generated from Excel or earlier steps)
df = pd.read_csv('user_calories_data.csv')

# Check the first few rows of the dataset
print(df.head())

# Define features and target variable
X = df[['Age', 'Activity_Level', 'Weight']]  # Features: Age, Activity_Level, and Weight
y = df['Calories_Intake']  # Target: Calories_Intake

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the models to evaluate
models = {
    'LinearRegression': LinearRegression(),
    'RandomForestRegressor': RandomForestRegressor(),
    'GradientBoostingRegressor': GradientBoostingRegressor()
}

# Initialize a dictionary to store the mean squared errors for each model
mse_scores = {}

# Train each model and evaluate performance
for model_name, model in models.items():
    # Fit the model
    model.fit(X_train, y_train)
    
    # Predict on the test set
    predictions = model.predict(X_test)
    
    # Calculate mean squared error
    mse = mean_squared_error(y_test, predictions)
    
    # Store the MSE score
    mse_scores[model_name] = mse
    
    # Print results
    print(f'{model_name} MSE: {mse}')

# Determine the best model based on the lowest MSE
best_model_name = min(mse_scores, key=mse_scores.get)
print(f'The best model is: {best_model_name} with an MSE of {mse_scores[best_model_name]}')

# -*- coding: utf-8 -*-
"""employee.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r3xpbk_HJhsw3bvIyqXTysjz7qsaIS6r
"""

!pip install pandas scikit-learn streamlit pyngrok --quiet

import pandas as pd

# Load the uploaded CSV
data = pd.read_csv("/content/employee_data.csv")  # use uploaded path
data.head()

data.columns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Rename columns to consistent format (if not already)
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "-")

# Encode categorical columns
le_workclass = LabelEncoder()
le_country = LabelEncoder()
le_income = LabelEncoder()

data['workclass'] = le_workclass.fit_transform(data['workclass'])
data['native-country'] = le_country.fit_transform(data['native-country'])
data['income'] = le_income.fit_transform(data['income'])

# Features and target
X = data[['age', 'hours-per-week', 'workclass', 'native-country']]
y = data['income']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, 'salary_model.pkl')
joblib.dump(le_workclass, 'workclass_encoder.pkl')
joblib.dump(le_country, 'country_encoder.pkl')
joblib.dump(le_income, 'salary_encoder.pkl')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import joblib
# 
# # Load saved model and encoders
# model = joblib.load('salary_model.pkl')
# le_workclass = joblib.load('workclass_encoder.pkl')
# le_country = joblib.load('country_encoder.pkl')
# le_salary = joblib.load('salary_encoder.pkl')
# 
# st.markdown(
#     "<h1 style='text-align: center;'>Salary Prediction</h1>",
#     unsafe_allow_html=True
# )
# 
# # User inputs
# age = st.text_input("Age:", "24")
# hours = st.text_input("Working Hours Per Week:", "8")
# 
# work_class = st.selectbox("Work Class", le_workclass.classes_)
# country = st.selectbox("Country", le_country.classes_)
# 
# if st.button("Predict Salary"):
#     try:
#         age = int(age)
#         hours = int(hours)
#         work_encoded = le_workclass.transform([work_class])[0]
#         country_encoded = le_country.transform([country])[0]
# 
#         X = [[age, hours, work_encoded, country_encoded]]
#         prediction = model.predict(X)
#         predicted_class = le_salary.inverse_transform(prediction)[0]
# 
#         st.success(f"Predicted Salary Class: {predicted_class}")
#     except Exception as e:
#         st.error(f"Error: {e}")
#

!pip install pandas scikit-learn streamlit pyngrok --quiet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import joblib
# 
# st.set_page_config(page_title="Employees Salary Prediction", layout="centered")
# 
# # Load model and encoders
# model = joblib.load('salary_model.pkl')
# le_workclass = joblib.load('workclass_encoder.pkl')
# le_country = joblib.load('country_encoder.pkl')
# le_salary = joblib.load('salary_encoder.pkl')
# 
# st.markdown("<h1 style='text-align: center; color: green;'>Employees Salary Prediction</h1>", unsafe_allow_html=True)
# st.markdown("---")
# 
# # Input form
# age = st.text_input("Enter Age", "30")
# hours = st.text_input("Enter Hours Worked Per Week", "40")
# 
# work_class = st.selectbox("Select Workclass", le_workclass.classes_)
# country = st.selectbox("Select Native Country", le_country.classes_)
# 
# if st.button("Predict Salary"):
#     try:
#         age = int(age)
#         hours = int(hours)
#         work_encoded = le_workclass.transform([work_class])[0]
#         country_encoded = le_country.transform([country])[0]
# 
#         # Predict
#         prediction = model.predict([[age, hours, work_encoded, country_encoded]])
#         salary_class = le_salary.inverse_transform(prediction)[0]
# 
#         st.success(f"Predicted Salary Class: {salary_class}")
#     except Exception as e:
#         st.error(f"Invalid input or error: {e}")
#

!ngrok config add-authtoken 2zaGa3VhZGCY77S6RxlObwldAY9_ygJz9FDMN8cVm5yAegXr

"""To use `pyngrok`, you need to provide your ngrok authtoken. You can obtain your authtoken from your ngrok dashboard and add it to the Colab Secrets Manager."""

from pyngrok import ngrok

# Start the streamlit app
!streamlit run app.py &>/content/log.txt &

# Open public URL
public_url = ngrok.connect(addr=8501, proto="http")
print(f"🎯 App is live at: {public_url}")


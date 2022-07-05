import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import plotly.io as pio

pio.renderers.default = "browser"

st.title("A Waiter's Tip Prediction")
st.header("""
This Web App predicts the tip given by a customer. 
""")
st.write('\n')
st.write('\n')
st.write('\n')


st.subheader("""
Machine Learning model = Multilinear Regression. 
""")


total_bill = st.sidebar.slider("Total bill (in dollars)", 1,300)
sex = st.sidebar.selectbox("Sex of the bill payer", ("Male", "Female"))
smoker = st.sidebar.selectbox("Where there smokers in the party?", ("Yes", "No"))
day = st.sidebar.selectbox("Day of the week", ("Thursday", "Friday","Saturday","Sunday"))
time = st.sidebar.selectbox("Time of day", ("Lunch", "Dinner"))
size = st.sidebar.slider("Size of the party", 1, 15)

data = pd.read_csv("tips.csv")
#print(data.head())

figure = px.scatter(data, x="total_bill", y="tip", size="size", color="day", trendline="ols")
figure_2 = px.scatter(data_frame = data, x="total_bill",
                    y="tip", size="size", color= "time", trendline="ols")
figure_3 = px.pie(data,
             values='tip',
             names='day',hole = 0.5)
#figure.show()


# data transformed from categorical values to numerical values
data["sex"] = data["sex"].map({"Female": 0, "Male": 1})
data["smoker"] = data["smoker"].map({"No": 0, "Yes": 1})
data["day"] = data["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
data["time"] = data["time"].map({"Lunch": 0, "Dinner": 1})
#data.head()

# split data into training and test
x = np.array(data[["total_bill", "sex", "smoker", "day",
                   "time", "size"]])
y = np.array(data["tip"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.2,
                                                random_state=42)

#train model
model = LinearRegression()
model.fit(xtrain, ytrain)

#test model

#############################################################
if sex == "Male":
    sex = 1
else:
    sex = 0
####################
if smoker == "Yes":
    smoker = 1
else:
    smoker = 0
####################
if day == "Thursday":
    day = 0
elif day == "Friday":
    day = 1
elif day == "Saturday":
    day = 2
elif day == "Sunday":
    day = 3
#####################
if time == "Lunch":
    time = 0
else:
    time = 1
##############################################################

# features = [[total_bill, "sex", "smoker", "day", "time", "size"]]
features = np.array([[total_bill, sex, smoker, day, time, size]])
model_value =model.predict(features)
st.markdown("***")
st.subheader('Tip Prediction (in dollars):')
st.subheader(model_value)
st.markdown("***")
st.subheader('Exploratory Data Analysis (EDA):')
st.write("Click on the interactive graph below to select a specific day of the week")
st.plotly_chart(figure)
st.plotly_chart(figure_3)
st.plotly_chart(figure_2)

st.write("""
Dataset courtesy of https://www.kaggle.com/datasets/jsphyg/tipping .
""")

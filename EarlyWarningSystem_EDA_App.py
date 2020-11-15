# -*- coding: utf-8 -*-
"""EarlyWarning_App.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1clE1MtsDREik-QvSZUsiRH1GFfJehOxz
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance
import warnings
import plotly
import plotly.express as px
import plotly.graph_objects as go

warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Title and Subheader
st.title("Early Warning System for Small Business Dataset EDA App")
st.subheader("EDA Web App with Streamlit ")

# EDA
my_dataset = "Final_Data_11_11_4.csv"

# To Improve speed and cache data
@st.cache(persist=True)
def explore_data(dataset):
    df = pd.read_csv('D://Job/UBS竞赛项目/决赛2/Final_Data_11_11_4.csv')
    return df 

# Show Dataset
if st.checkbox("Preview DataFrame"):
    data = explore_data(my_dataset)
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())
    else:
        st.write(data.head(2))
        
# Show Entire Dataframe
if st.checkbox("Show All DataFrame"):
    data = explore_data(my_dataset)
    st.dataframe(data)
    
# Show Description
if st.checkbox("Show All Column Name"):
    data = explore_data(my_dataset)
    st.text("Columns:")
    st.write(data.columns)
    
# Dimensions
data_dim = st.radio('What Dimension Do You Want to Show',('Rows','Columns'))
if data_dim == 'Rows':
    data = explore_data(my_dataset)
    st.text("Showing Length of Rows")
    st.write(len(data))
if data_dim == 'Columns':
    data = explore_data(my_dataset)
    st.text("Showing Length of Columns")
    st.write(data.shape[1])

# Summary of the Dataframe
if st.checkbox("Show Summary of Dataset"):
    data = explore_data(my_dataset)
    st.write(data.describe())
    
# Selection
species_option = st.selectbox('Select Columns',('Company Name','Address','Sales_Change','Employee_Change','City','State',
                         'Grocery_within_Zip','County','Civilian_labor_force_2019','Median_Household_Income_2018',
                         'Metro Area','Location Employee Size Actual','Location Sales Volume Actual','Years In Database',
                         'Credit Score Alpha','Supermarket_within_5_miles','Square Footage','Google_Scores','Google_Reviews'))
data = explore_data(my_dataset)
# Numerical Features
if species_option == 'Sales_Change':
    st.write(data['Sales_Change'])
elif species_option == 'Google_Reviews':
    st.write(data['Google_Reviews'])
elif species_option == 'Google_Scores':
    st.write(data['Google_Scores'])
elif species_option == 'Grocery_within_Zip':
    st.write(data['Grocery_within_Zip'])
elif species_option == 'Civilian_labor_force_2019':
    st.write(data['Civilian_labor_force_2019'])
elif species_option == 'Median_Household_Income_2018':
    st.write(data['Median_Household_Income_2018'])    
elif species_option == 'Location Employee Size Actual':
    st.write(data['Location Employee Size Actual']) 
elif species_option == 'County':
    st.write(data['County']) 
elif species_option == 'Years In Database':
    st.write(data['Years In Database']) 
elif species_option == 'Location Sales Volume Actual':
    st.write(data['Location Sales Volume Actual']) 
elif species_option == 'Square Footage':
    st.write(data['Square Footage'])
elif species_option == 'Supermarket_within_5_miles':
    st.write(data['Supermarket_within_5_miles'])
elif species_option == 'Credit Score Alpha':
    st.write(data['Credit Score Alpha'])
# Categorical Features
elif species_option == 'Company Name':
    st.write(data['Company Name'])
elif species_option == 'Address':
    st.write(data['Address'])
elif species_option == 'City':
    st.write(data['City'])
else:
    st.write("Select A Column")
    
# Show Plots
# if st.checkbox("Simple Bar Plot with Matplotlib"):
#     data = explore_data(my_dataset)
#     data.plot(kind='bar')
#     st.pyplot()
    
# Show Plots
if st.checkbox("Simple Correlation Plot with Seaborn "):
    data = explore_data(my_dataset)
    plt.figure(figsize=(15,10))
    st.write(sns.heatmap(data.corr(),vmax=0.9,linewidths=.2,cmap='Set2_r',square=True,annot=True))
    # Use Matplotlib to render seaborn
    st.pyplot()

# Show Plots
if st.checkbox("Median_Household_Income_2018 of Different Counties"):
    data = explore_data(my_dataset)
    st.write(sns.barplot(x="Median_Household_Income_2018",y="County",data = data))
    st.pyplot()

# Show Plots
if st.checkbox("Sales Volume & Employee Size"):
    data = explore_data(my_dataset)
    st.write(px.scatter(data,x='Location Employee Size Actual',y='Location Sales Volume Actual',color='Record Type',template='ggplot2'))
    st.pyplot()


# Show Plots
if st.checkbox("Sales_Change & Employee_Change"):
    data = explore_data(my_dataset)
    st.write(px.scatter(data, x='Employee_Change', y='Sales_Change', color='Record Type', template='ggplot2'))
    st.pyplot()


# Show Plots
if st.checkbox("Sales_Change & Employee_Size & Google_Review"):
    data = explore_data(my_dataset)
    st.write(px.scatter_3d(data, x='Google_Reviews', y='Location Employee Size Actual', z='Sales_Change', color='Record Type', template='ggplot2', size='Google_Scores'))
    st.pyplot()


# About
if st.button("About App"):
    st.subheader("Early Warning System for Small Business Dataset EDA App")
    st.text("Built with LMWGY Team")
    st.text("Thanks for Watching")

if st.checkbox("By"):
    st.text("LMWGY Team")


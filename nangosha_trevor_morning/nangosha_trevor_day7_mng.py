"""
python for Datascience
summary
1. NumPy - Numerical python, helps 1 work with arrays efficiently
2. Pandas - functionlity, data cleaning, transformation, mergeing,filtering

Data Visualization
Plotting - use library called matplotlib or seaborn - helps create line, scatter, bar, histogram, heatmap

Key concepts in Data science
1. Data -  (text, images, videos) or semi structured data(JSON, XML)
2. Data Mining
3. Statistical Analysis
4. Machine Learning
5. Data Visualization
6. Big Data
7. Predictive Analysis
"""
"""
Understanding data science work flow
1. Problem definition
2. Data Acquisition data.gov, kaggle, database, external datasets
Ensure data quality, data validation, cleaning and processing
EDA Data Eploratory Analysis

# Data Preparation and Preprocessing
-Missing data
-Wrong Format
-Null values
-Wrong Formats
-Duplicates
"""
# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Control Display of seaborn data
pd.options.display.max_columns=50
sns.set(style="darkgrid", rc={"axes.facecolor":"#CAF1DE"})

# loading the data
df = pd.read_csv('bse_dataset.csv')
print(df)

print(df.columns)

df.shape
print(df.shape)
print("finished shape")
df.info
print(df.info())
print("finished info")

# df.isnull().sum().s
# data Analysis work flow
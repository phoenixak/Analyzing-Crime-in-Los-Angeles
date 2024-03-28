# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("dataset\crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes.head()

# Extract the first two characters from 'TIME OCC' and convert to integer
crimes['Hour'] = crimes['TIME OCC'].str[:2].astype(int)

# Count the frequency of crimes by hour
crime_hour_counts = crimes['Hour'].value_counts().sort_index()

# Find the hour with the highest frequency and store it as an integer
peak_crime_hour = int(crime_hour_counts.idxmax())

# Filter for night crimes
night_crimes = crimes[(crimes['TIME OCC'].astype(int) >= 22) | (crimes['TIME OCC'].astype(int) < 4)]

# Count the frequency of night crimes by area
night_crime_counts = night_crimes['AREA NAME'].value_counts()

# Find the area with the most night crimes
peak_night_crime_location = night_crime_counts.idxmax()

# Define age groups
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ['0-17', '18-25', '26-34', '35-44', '45-54', '55-64', '65+']

# Categorize 'Vict Age' into age groups
crimes['Vict Age Group'] = pd.cut(crimes['Vict Age'], bins=age_bins, labels=age_labels)

# Count the number of crimes for each age group
victim_ages = crimes['Vict Age Group'].value_counts()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

# DATA GATHERING AND PREPROCESSING
# Read data into dataframe and specifiy seperator to be tab
data = pd.read_csv('Events_Points_Analysis/FSG24/FSG24_Endurance_Lap_Times.txt', sep="\t")

# Get values of analyzed teams
analyzed_teams = ['Zürich ETH', 'Amberg OTH', 'Bern UAS', 'Aachen RWTH', 'Eindhoven TU']
mask = data['City_University'].isin(analyzed_teams)
data_filtered_teams = data[mask]

# Filter columns which should be melted
columns_to_melt = [col for col in data_filtered_teams.columns if re.match(r'[A-Za-z]+\d+_D\d+', col)]

# Melt dataframe
data_melted = data_filtered_teams.melt(
    id_vars=['City_University'],
    value_vars=columns_to_melt,
    var_name='Lap_Number',
    value_name='Lap_Time'
)
# Map Lap-Time to floats
data_melted['Lap_Time'] = data_melted['Lap_Time'].str.replace(',', '.').astype(float)

# VISUALIZE DATA
# Draw boxplot
sns.boxenplot(
    x='City_University', 
    y='Lap_Time', 
    data=data_melted,
    order=['Zürich ETH', 'Amberg OTH', 'Bern UAS', 'Aachen RWTH', 'Eindhoven TU',],
    palette='viridis'
)

# Improve readability
plt.title("Lap Times per Team")
plt.xlabel("University")
plt.ylabel("Lap Time (seconds)")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)

# Show plot
plt.show()

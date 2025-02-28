import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# DATA GATHERING AND PREPROCESSING
# Read data into dataframe and specifiy seperator to be tab
data = pd.read_csv('Events_Points_Analysis/FSG24/FSG24_Endurance_Scoring_Results.txt', sep="\t")

# Get values of analiyzed teams
analyzed_teams = ['Zürich ETH', 'Amberg OTH', 'Bern UAS', 'Aachen RWTH', 'Eindhoven TU']
scores = data[data['City_University'].isin(analyzed_teams)]['Scores'].tolist()

# Prepare dataframe which is used for visualization
data_analyzed_teams = pd.DataFrame({
    'University': analyzed_teams,
    'Score': list(map(lambda x: float(x.replace(',', '.')), scores))
})

# VISUALIZATION
# Set theme and draw barplot
sns.set_theme()
sns.barplot(
    data_analyzed_teams, 
    x='University', 
    y='Score',
    palette='viridis',
)

# Set labels and title
plt.xlabel("University")
plt.ylabel("Score")
plt.title("Endurance Scores")

# Display plot 
plt.show()

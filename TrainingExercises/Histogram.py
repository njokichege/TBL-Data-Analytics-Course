import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Generate sample data
np.random.seed(0)
numUsers = 1000
#Assuming negative feedback scores on a scale of 1 to 10
negativeFeedback = np.random.randint(1,11,size=numUsers)
#Binary attrition indicator (0: stay, 1: leave)
attrition = np.random.choice([0,1],size=numUsers,p=[0.8,0.2])

#Create a dataframe
data = pd.DataFrame({"Negative Feedback":negativeFeedback,"Attrition":attrition})

#Calculate mean, median and mode of negative feedback
maenFeedback = data['Negative Feedback'].mean()
medianFeedback = data['Negative Feedback'].median()
modeFeedback = data['Negative Feedback'].mode().values[0]

#Plotting
plt.figure(figsize=(12,8))

#Histogram for negative feedback distribution
sns.histplot(data['Negative Feedback'], bins=10, kde=True, color='skyblue', edgecolor='black', linewidth=1.2, label='Distribution')

#Highlight mean, median and mode
plt.axvline(maenFeedback, color='red', linestyle='--', label='Mean')
plt.axvline(medianFeedback, color='green', linestyle='--', label='Median')
plt.axvline(modeFeedback, color='orange', linestyle='--', label='Mode')

print("Mean: ",maenFeedback)
print("Median: ",medianFeedback)
print("Mode: ",modeFeedback)
print("Skewness:",data['Negative Feedback'].skew())

#Add legend and labels
plt.legend()
plt.title('Negative Feedback Distribution and Attrition')
plt.xlabel('Negative Feedback Score')
plt.ylabel('Frequency')

#Show plot
plt.show()
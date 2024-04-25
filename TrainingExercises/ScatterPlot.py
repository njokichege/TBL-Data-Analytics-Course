import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Generate sample data
np.random.seed(0)
numEmployees = 500
#Asume a normal distribution of salaries
salaries = np.random.normal(loc=50000,scale=15000,size=numEmployees)
#Assume attrition rates follow a beta distribution
attritionRates = np.random.beta(a=2,b=5,size=numEmployees)

#Create a dataframe
data = pd.DataFrame({'Salaries':salaries,'Attrition Rate':attritionRates})

#Visualize the distribution
plt.figure(figsize=(10,6))
sns.scatterplot(x="Salaries",y="Attrition Rate",data=data,alpha=0.6)
plt.title("Attrition Rate vs Salary")
plt.xlabel("Salary")
plt.ylabel("Attrition Rate")
plt.grid(True)
plt.show()

#Calculate skewness
skewness = data["Attrition Rate"].skew()
print("Skewness:",skewness)

#We generate a sample dataset where salaries follow a normal 
    #distribution and attrition rates follow a beta distribution.
#We create a scatter plot to visualize the relationship between 
    #salary and attrition rate.
#We calculate the skewness of the attrition rate distribution.
#The skewness value will indicate whether the distribution of 
    #attrition rates is skewed towards higher or lower salary levels. 
    #Positive skewness suggests a longer tail on the right side 
    #(higher salaries), while negative skewness suggests a longer 
    #tail on the left side (lower salaries). 
#This can provide insights into whether salary plays a role in 
    #attrition rates.
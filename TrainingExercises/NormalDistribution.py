import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

#Generate sample data (normal distribution)
np.random.seed(0)
data = np.random.normal(loc=0,scale=1,size=1000)

#Calculate mean
mean = np.mean(data)

#Calculate variance
variance = np.var(data)

#Calculate skewness
skewness = stats.skew(data)

#Calculate kurtosis
kurtosis = stats.kurtosis(data)

print("Mean:",mean)
print("Variance",variance)
print("Skewness",skewness)
print("Kurtosis",kurtosis)

#plot histogram 
plt.hist(data, bins=30,density=True,alpha=0.7,color='b',edgecolor='black')

#plot a vertical line at the mean
plt.axvline(mean,color="r",linestyle="dashed",linewidth=1,label="Mean")
plt.axvline(variance,color="g",linestyle="dashed",linewidth=1,label="Variance")

plt.title("Histogram of sample data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
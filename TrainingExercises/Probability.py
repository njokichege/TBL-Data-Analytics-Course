from scipy.stats import binom, poisson, norm
import matplotlib.pyplot as plt
import numpy as np

#Binomial Distribution
#It is the discrete probability distribution that gives only two 
    #possible results in an experiment, either Success or Failure.
#There are two parameters n and p used here in a binomial distribution. 
    #The variable ‘n’ states the number of times the experiment runs 
    #and the variable ‘p’ tells the probability of any one outcome. 
n = 10 #number of trials
p = 0.5 #probability of success
binomialDistribution = binom(n,p)
x = range(n+1)
plt.bar(x,binomialDistribution.pmf(x))
plt.title("Binomial Distribution")
plt.xlabel("Number of successes")
plt.ylabel("Probability")
plt.show()

#Poisson Distribution
#It gives the probability of an event happening a certain number of 
    #times (k) within a given interval of time or space.
#The Poisson distribution has only one parameter, λ (lambda), 
    #which is the mean number of events. 
mu = 3 #mean rate
poissonDistribuiton = poisson(mu)
x = range(10)
plt.bar(x,poissonDistribuiton.pmf(x))
plt.title("Poisson Distributions")
plt.xlabel("Number of events")
plt.ylabel("Probability")
plt.show()

#Normal Distribution
#In a normal distribution, data is symmetrically distributed with 
    #no skew. When plotted on a graph, the data follows a bell shape, 
    #with most values clustering around a central region and tapering 
    #off as they go further away from the center.
mean = 0 #mean
stDev = 1 #standard deviation
normalDistribution = norm(mean,stDev)
x = np.linspace(-4,4,100)
plt.plot(x,normalDistribution.pdf(x))
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.show()
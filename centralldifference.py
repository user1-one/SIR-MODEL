import numpy as np
import matplotlib.pyplot as plt

# Defining parameters
h = .5      # Step size for central difference method
tMax = 300  # Maximum time

beta = 0.12
gamma= 0.03

# Initializing lists to store t and y values
tValues = np.arange(0, tMax + h, h)
sValues = [0.999]  # Initial value of 'population'
iValues = [0.001]  # Initial value of 'population'
rValues = [0.000]  # Initial value of 'population'

# Using central difference method requires one forward step first
sValues.append(sValues[0] + h*(-beta*sValues[0]*iValues[0]))
iValues.append(iValues[0] + h*(beta*sValues[0]*iValues[0] - gamma*iValues[0]))
rValues.append(rValues[0] + h*(gamma*iValues[0]))

# Using central difference method to plot approximate solution
for i in range(1, len(tValues) - 1):
    sNext = sValues[i] + h*(-beta*(sValues[i]+sValues[i-1])/2 * (iValues[i]+iValues[i-1])/2)
    sValues.append(sNext)

    iNext = iValues[i] +h*(beta*(sValues[i]+sValues[i-1])/2 * (iValues[i]+iValues[i-1])/2 - gamma*iValues[i])
    iValues.append(iNext)

    rNext = rValues[i] + h*(gamma*iValues[i])
    rValues.append(rNext)

# Plotting
plt.plot(tValues, sValues, label='S(t)', color='blue')
plt.plot(tValues, iValues, label='I(t)', color='red')
plt.plot(tValues, rValues, label='R(t)', color='green')
plt.xlabel('t')
plt.ylabel('Percentage of the population')
plt.title('SIR Model using Central Difference Method')
plt.legend()
plt.show()

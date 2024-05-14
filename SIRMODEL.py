import numpy as np
import matplotlib.pyplot as plt

# Defining parameters
h = .5      # Step size for forward difference method
tMax = 200  # Maximum time

A = 0.12
B= 0.03
C= 0.01
D = 0.01
# Initializing lists to store t and y values
tValues = np.arange(0, tMax + h, h)
ignorant = [0.999]  # Initial value of 'ignorant'
HeardandSpreading = [0.001]  # Initial value of 'heard and spreading'
rValues = [0.000]  # Initial value of ' refuse population'


# Using forward difference method to plot approximate solution
for i in range(len(tValues) - 1):
    iNext = ignorant[-1] + h*(-A*ignorant[-1]*HeardandSpreading[-1] + C*ignorant[-1]*rValues[-1] - D*ignorant[-1]*rValues[-1])
    ignorant.append(iNext)

    hNext = HeardandSpreading[-1] +h*(A*ignorant[-1]*HeardandSpreading[-1] - B*HeardandSpreading[-1])
    HeardandSpreading.append(hNext)

    rNext = rValues[-1] + h*(B*HeardandSpreading[-1]- C*ignorant[-1]*rValues[-1] + D*ignorant[-1]*rValues[-1])
    rValues.append(rNext)


# Plotting
plt.plot(tValues, ignorant, label='I(t)', color='blue')
plt.plot(tValues, HeardandSpreading, label='H(t)', color='red')
plt.plot(tValues, rValues, label='R(t)', color='green')
plt.xlabel('t')
plt.ylabel('Percentage of the population')
plt.title('HIR Model')
plt.legend()
plt.show()

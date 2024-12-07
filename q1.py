import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

# Generate synthetic data
np.random.seed(42)
data = np.concatenate([np.random.normal(0, 1, 500), np.random.normal(5, 1, 500)])[:, np.newaxis]

# Define the bandwidth for KDE
bandwidth = 0.5

# Fit KDE
kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth)
kde.fit(data)

# Generate points for the plot
x_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
log_density = kde.score_samples(x_plot)  # Log of the probability density

# Plot the results
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True, alpha=0.5, color='gray', label='Histogram')
plt.plot(x_plot, np.exp(log_density), color='blue', lw=2, label='KDE Estimate')
plt.title('Kernel Density Estimation')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

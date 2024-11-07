import matplotlib.pyplot as plt

# Data from Table 2
mu_values = [0.50, 0.55, 0.60, 0.65, 0.70, 1.00]
K_values = [2, 3, 4]

# Miss rates for each combination of (mu, K) for different subsets
miss_rates = {
    'Reasonable': [
        [13.16, 10.89, 12.78],
        [12.89, 10.41, 12.64],
        [11.26,  9.34, 10.97],
        [12.74, 10.59, 11.20],
        [13.45, 12.14, 12.23],
        [13.71, 12.95, 13.11]
    ],
    'Small': [
        [17.71, 12.70, 16.55],
        [16.01, 12.51, 15.97],
        [15.17, 11.90, 13.24],
        [16.12, 12.68, 15.77],
        [17.90, 15.91, 16.40],
        [18.02, 16.58, 17.44]
    ],
    'Heavy': [
        [47.63, 43.12, 45.57],
        [45.70, 41.90, 43.06],
        [42.79, 38.27, 40.66],
        [43.40, 40.87, 41.15],
        [42.97, 40.79, 41.02],
        [43.61, 40.96, 41.88]
    ],
    'All': [
        [45.18, 38.45, 45.14],
        [43.77, 38.02, 42.40],
        [42.03, 36.43, 39.89],
        [42.16, 38.11, 40.97],
        [42.45, 40.70, 40.94],
        [43.15, 40.89, 41.13]
    ]
}

# Plotting the results
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Miss Rate vs Occlusion-Aware Threshold (μ) and Hierarchies (K)')

subsets = ['Reasonable', 'Small', 'Heavy', 'All']

for i, subset in enumerate(subsets):
    ax = axs[i // 2, i % 2]
    for j, K in enumerate(K_values):
        ax.plot(mu_values, [miss_rates[subset][k][j] for k in range(len(mu_values))], label=f'K={K}')
    ax.set_title(f'{subset} Subset')
    ax.set_xlabel('Occlusion-Aware Threshold (μ)')
    ax.set_ylabel('Miss Rate (MR-2)')
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.show()
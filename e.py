import matplotlib.pyplot as plt
import numpy as np

# Sample data for loss over epochs
epochs = np.arange(200)
base_loss = np.exp(-0.02 * epochs) + 0.1 * np.random.rand(200)
base_os_loss = np.exp(-0.025 * epochs) + 0.1 * np.random.rand(200)
base_os_hs_loss = np.exp(-0.03 * epochs) + 0.1 * np.random.rand(200)
base_os_hs_cn_loss = np.exp(-0.035 * epochs) + 0.1 * np.random.rand(200)

# Sample data for log loss over epochs
base_log_loss = np.log1p(base_loss)
base_os_log_loss = np.log1p(base_os_loss)
base_os_hs_log_loss = np.log1p(base_os_hs_loss)
base_os_hs_cn_log_loss = np.log1p(base_os_hs_cn_loss)

# Sample data for training time (hours)
methods = ['Base', 'Base+OS', 'Base+OS+HS', 'Base+OS+HS+CN']
training_time = [23.3, 17.4, 14.1, 13.8]

# Plot (a): Loss vs Epoch
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(epochs, base_loss, label='Base')
plt.plot(epochs, base_os_loss, label='Base+OS')
plt.plot(epochs, base_os_hs_loss, label='Base+OS+HS')
plt.plot(epochs, base_os_hs_cn_loss, label='Base+OS+HS+CN')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('(a)')
plt.legend()
plt.grid(True)

# Plot (b): Log loss vs Epoch
plt.subplot(1, 3, 2)
plt.plot(epochs, base_log_loss, label='Base')
plt.plot(epochs, base_os_log_loss, label='Base+OS')
plt.plot(epochs, base_os_hs_log_loss, label='Base+OS+HS')
plt.plot(epochs, base_os_hs_cn_log_loss, label='Base+OS+HS+CN')
plt.xlabel('Epoch')
plt.ylabel('log(Loss)')
plt.title('(b)')
plt.legend()
plt.grid(True)

# Plot (c): Training time
plt.subplot(1, 3, 3)
plt.bar(methods, training_time, color=['red', 'blue', 'orange', 'green'])
plt.xlabel('Method')
plt.ylabel('Training Time (h)')
plt.title('(c)')
plt.grid(True, axis='y')

plt.suptitle(' Comparison of training time and energy consumption.')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Synthetic time-series data
# -----------------------------
np.random.seed(42)
n = 200
time = np.arange(n)

# normal signal
data = np.random.normal(0, 1, n)

# inject anomalies
data[50] = 8
data[120] = -7
data[160] = 6

# -----------------------------
# 2. Sliding window anomaly detection
# -----------------------------
window_size = 20
threshold = 3

anomalies = []

for i in range(window_size, n):
    window = data[i-window_size:i]
    
    mean = np.mean(window)
    std = np.std(window)
    
    if std == 0:
        continue
    
    z_score = (data[i] - mean) / std
    
    if np.abs(z_score) > threshold:
        anomalies.append(i)

# -----------------------------
# 3. Visualization
# -----------------------------
plt.figure(figsize=(12,5))
plt.plot(time, data, label="Signal")

plt.scatter(anomalies, data[anomalies], 
             color='red', label="Detected Anomalies")

plt.title("Sliding Window Anomaly Detection")
plt.legend()
plt.show()
plt.savefig("results.png")
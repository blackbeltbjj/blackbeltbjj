import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulate 30 days of wave data for Bream Bay, Northland
np.random.seed(42)
timestamps = pd.date_range(start="2026-08-01", periods=720, freq="h")  # Hourly data
base_waves = 1.2 + 0.3 * np.sin(np.arange(720) / 24) + np.random.normal(0, 0.2, 720)

# Inject a massive 3-day winter storm event (Days 14 to 17)
base_waves[336:408] += np.random.uniform(1.8, 3.2, 72)

# Create DataFrame
df = pd.DataFrame({"Timestamp": timestamps, "Significant_Wave_Height_m": base_waves})
df.set_index("Timestamp", inplace=True)

# 2. Oceanographic Data Analytics
max_wave = df["Significant_Wave_Height_m"].max()
mean_wave = df["Significant_Wave_Height_m"].mean()
p95_wave = df["Significant_Wave_Height_m"].quantile(0.95)

print(f"--- Bream Bay Oceanographic Summary ---")
print(f"Mean Wave Height: {mean_wave:.2f} meters")
print(f"Maximum Storm Wave Record: {max_wave:.2f} meters")
print(f"95th Percentile Threshold (Extreme Design Limit): {p95_wave:.2f} meters\n")

# 3. Generate Engineering Visualization
plt.figure(figsize=(11, 5))
plt.plot(df.index, df["Significant_Wave_Height_m"], color='#1f77b4', alpha=0.8, label='Significant Wave Height ($H_s$)')
plt.axhline(y=p95_wave, color='#d62728', linestyle='--', linewidth=1.5, label=f'95th Percentile Design Limit ({p95_wave:.2f}m)')

plt.title('Significant Wave Height ($H_s$) Analysis - Bream Bay, Northland', fontsize=12, fontweight='bold', pad=15)
plt.ylabel('Wave Height (meters)', fontsize=10)
plt.xlabel('Date', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.ylim(0, 5.0)
plt.legend(loc='upper left')

# Save plot for GitHub markdown integration
plt.savefig('bream_bay_wave_analysis.png', dpi=150, bbox_inches='tight')
print("Success: 'bream_bay_wave_analysis.png' has been generated for your portfolio!")

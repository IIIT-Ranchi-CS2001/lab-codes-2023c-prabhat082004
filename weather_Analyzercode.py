
import numpy as np
import matplotlib.pyplot as plt

# Simulating temperature data (in Celsius) for a week
temperatures = np.random.randint(15, 35, size=7)  # Random temperatures between 15°C and 35°C
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Basic statistics
mean_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
min_temp = np.min(temperatures)
max_temp = np.max(temperatures)
std_temp = np.std(temperatures)

# Hottest and coldest days
hottest_day = days[np.argmax(temperatures)]
coldest_day = days[np.argmin(temperatures)]

# Display data in a detailed box representation
print("=" * 60)
print(f"{'Day':<12}{'Temperature (°C)':<20}{'Remarks':<28}")
print("=" * 60)
for day, temp in zip(days, temperatures):
    remark = ""
    if temp == max_temp:
        remark = "Hottest Day"
    elif temp == min_temp:
        remark = "Coldest Day"
    print(f"{day:<12}{temp:<20}{remark:<28}")
print("=" * 60)

# Summary
print(f"Mean Temperature: {mean_temp:.2f}°C")
print(f"Median Temperature: {median_temp:.2f}°C")
print(f"Temperature Std Deviation: {std_temp:.2f}°C")

# Enhanced visualization
plt.figure(figsize=(15, 10))

# Line chart for temperature trend
plt.subplot(2, 2, 1)
plt.plot(days, temperatures, marker='o', linestyle='-', color='#007ACC', linewidth=2, label='Temperature')
plt.axhline(mean_temp, color='#FF4C4C', linestyle='--', linewidth=1.5, label=f'Mean Temp: {mean_temp:.2f}°C')
plt.axhline(median_temp, color='#32CD32', linestyle='-.', linewidth=1.5, label=f'Median Temp: {median_temp:.2f}°C')
plt.scatter(hottest_day, max_temp, color='red', s=100, label=f'Hottest: {max_temp}°C ({hottest_day})', zorder=5)
plt.scatter(coldest_day, min_temp, color='blue', s=100, label=f'Coldest: {min_temp}°C ({coldest_day})', zorder=5)
plt.title("Weekly Temperature Trend", fontsize=14, fontweight='bold')
plt.xlabel("Day", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=10, loc='upper left', frameon=True, framealpha=0.9, edgecolor='gray')

# Pie chart for temperature distribution
plt.subplot(2, 2, 2)
plt.pie(
    temperatures,
    labels=days,
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.viridis(np.linspace(0, 1, 7)),
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)
plt.title("Temperature Distribution", fontsize=14, fontweight='bold')

plt.subplot(2, 1, 2)

# Sort temperatures and days together
sorted_indices = np.argsort(temperatures)  # Get indices that would sort temperatures
sorted_temperatures = temperatures[sorted_indices]  # Sort temperatures
sorted_days = [days[i] for i in sorted_indices]  # Sort days accordingly

temp_grid = np.array([sorted_temperatures]) 

plt.imshow(temp_grid, cmap='coolwarm', aspect='auto',vmin=15,vmax=40)
plt.colorbar(label="Temperature (°C)", orientation="vertical")

plt.yticks(range(1), ["Temperatures"]) 
plt.xticks(range(len(sorted_days)), sorted_days, fontsize=10)

plt.title("Daily Temperature Heatmap (Sorted)", fontsize=14, fontweight='bold')

for (i, temp) in enumerate(sorted_temperatures):
    plt.text(i, 0, f"{temp}°C", ha='center', va='center', color='black', fontsize=10, fontweight='bold')

# Adjust layout and show all plots
plt.tight_layout()
plt.show()

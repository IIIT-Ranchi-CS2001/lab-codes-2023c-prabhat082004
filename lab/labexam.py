import pandas as pd
import numpy as np
path="AQI_Data.csv"
df = pd.read_csv(path)

#Display the first eight rows
print("First eight rows of the datasheet:-")
print(df.head(8))
print("\n")

#Display the last five rows
print("Last five rows of the datasheet:-")
print(df.tail(5))
print("\n")

# Show the dtype and number of non null values in each column
print("\nData types and non-null values:")
print(df.info())
print("\n")

# # compute mean AQI
# AQI_mean = np.mean(df['AQI'])
# print(f"Mean of AQI is {AQI_mean}.")
# print("")

# # compute max PM2.5
# max = np.max(df['PM2.5'])
# print(f"max of PM2.5 is {max }.")
# print("")

# # compute min PM10
# PM10_min = np.min(df['PM10'])
# print(f"min of PM10 is {PM10_min }.")
# print("")


# Finding mean for AQI in each city
aqi_mean_aqi = []
for city in df["City"].unique():
    city_data = df[df['City'] == city]
    AQI = np.array(city_data['AQI'])
    mean_AQI = np.mean(AQI)
    aqi_mean_aqi.append((city, mean_AQI))

for city, mean_AQI in aqi_mean_aqi:
    print(f"City name is {city} and its Mean AQI: {mean_AQI}")
    


# Display the max PM2.5 for each city
    print('\n')
    max_Pm_array = []
for city in df["City"].unique():
    city_data = df[df['City'] == city]
    Array = city_data['PM2.5'].to_numpy()
    max_PM25 = np.max(Array)
    max_Pm_array.append((city, max_PM25))

for city, max_PM25 in max_Pm_array:
    print(f"City Name is {city} and its Max PM2.5: {max_PM25}")
print('\n')    



# Display the min PM10 for each city
print("\n")
min_Pm_array = []
print('\n')
for city in df["City"].unique():
    city_data = df[df['City'] == city]
    Array_PM10 = city_data['PM10'].to_numpy()
    min_PM10 = np.min(Array_PM10)
    min_Pm_array.append((city, min_PM10))

for city, min_PM10 in min_Pm_array:
    print(f"City Name is {city} and its Min PM10: {min_PM10}")
print('\n')    

# SET-4 :
# Using a pivot table
pivot_table = df.pivot_table(values='PM2.5', index='City', aggfunc=np.max)
print("\nPivot table:")
print(pivot_table)

# Save the pivot table to a CSV file
pivot_table.to_csv('pivot.csv')

  


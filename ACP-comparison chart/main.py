import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("FuelConsumption.csv")

print(df.head())

print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

print(df.info())
print(df.describe())

fuel_group = df.groupby('Fuel Type').mean(numeric_only=True)
print(fuel_group)

fuel_group = fuel_group.reset_index()

plt.figure()
plt.bar(fuel_group['Fuel Type'], fuel_group['CO2 Emissions'])
plt.title("Average CO2 Emissions by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("CO2 Emissions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

fuel_counts = df['Fuel Type'].value_counts()

plt.figure()
plt.bar(fuel_counts.index, fuel_counts.values)
plt.title("Number of Vehicles per Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

vehicle_counts = df['Vehicle Class'].value_counts()

plt.figure()
plt.bar(vehicle_counts.index, vehicle_counts.values)
plt.title("Number of Vehicles per Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

vehicle_group = df.groupby('Vehicle Class').mean(numeric_only=True)
vehicle_group = vehicle_group.reset_index()

print(vehicle_group)

plt.figure()
plt.bar(vehicle_group['Vehicle Class'], vehicle_group['CO2 Emissions'])
plt.title("Average CO2 Emissions by Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("CO2 Emissions")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

fuel_consumption = df.groupby('Vehicle Class')[
    ['Fuel Consumption City', 'Fuel Consumption Hwy', 'Fuel Consumption Comb']
].mean()

fuel_consumption.plot(kind='bar', stacked=True)

plt.title("Fuel Consumption (City, Highway, Combined)")
plt.xlabel("Vehicle Class")
plt.ylabel("Fuel Consumption")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
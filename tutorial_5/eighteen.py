import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.read_csv('weather.csv')

print(weather_data.head(10))

max_temp = weather_data['temperature'].max()
min_temp = weather_data['temperature'].min()
print(f"Maximum Temperature: {max_temp}")
print(f"Minimum Temperature: {min_temp}")

places_below_28 = weather_data[weather_data['temperature'] < 28]['place']
print("Places with temperature less than 28°C:")
print(places_below_28)

cloudy_places = weather_data[weather_data['weather'] == "Cloudy"]['place']
print("Places with weather = Cloudy:")
print(cloudy_places)

weather_frequency = weather_data['weather'].value_counts()
print("Weather Frequency:")
print(weather_frequency)

plt.figure(figsize=(10, 6))
plt.bar(weather_data['date'], weather_data['temperature'])
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature of Each Day')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

import pandas as bl
import matplotlib.pyplot as ds
weather=bl.read_csv("E:\DATA SCIENCE\week2\Bangalore_1990_2022_BangaloreCity.csv") 
print(weather.isnull().sum())
weather['tavg'] = weather['tavg'].fillna(weather['tavg'].mean())
weather['tmax'] = weather['tmax'].fillna(weather['tmax'].mean())
weather['tmin'] = weather['tmin'].fillna(weather['tmin'].mean())
weather['prcp'] = weather['prcp'].fillna(weather['prcp'].mean())
print(weather.isnull().sum())
weather['time'] = bl.to_datetime(weather['time'], format="%d-%m-%Y")
weather['year'] = weather['time'].dt.year
weather['month'] = weather['time'].dt.month
weather['day'] = weather['time'].dt.day
yearly = weather.groupby('year')['tavg'].mean().reset_index()
print(yearly)
ds.figure(figsize=(10, 5))
ds.plot(yearly['year'], yearly['tavg'], marker='o', color='purple')
ds.title('Average Annual Temperature (1990–2022)')
ds.xlabel('Year')
ds.ylabel('Average Temperature (°C)')
ds.show()
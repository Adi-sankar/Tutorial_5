import pandas as pd

auto_data = pd.read_csv('auto.csv')

auto_data.dropna(inplace=True)
auto_data['horsepower'] = pd.to_numeric(auto_data['horsepower'], errors='coerce')
auto_data.dropna(subset=['horsepower'], inplace=True)

most_expensive_car = auto_data.loc[auto_data['price'].idxmax()]
most_expensive_company = most_expensive_car['company']
print(f"Most expensive car company: {most_expensive_company}")

toyota_cars = auto_data[auto_data['company'] == 'toyota']
print("\nToyota cars details:")
print(toyota_cars)

total_cars_by_company = auto_data.groupby('company').size()
print("\nTotal cars of all companies:")
print(total_cars_by_company)

highest_priced_car = auto_data.loc[auto_data['price'].idxmax()]
print("\nHighest priced car details:")
print(highest_priced_car)

average_mileage_by_company = auto_data.groupby('company')['average-mileage'].mean()
print("\nAverage mileage of all companies:")
print(average_mileage_by_company)

sorted_cars_by_price = auto_data.sort_values(by='price', ascending=False)
print("\nCars sorted by price:")
print(sorted_cars_by_price)

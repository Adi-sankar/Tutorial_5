import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales_data.csv')

plt.scatter(sales_data['month_number'], sales_data['toothpaste'], color='green', label='Toothpaste Sales')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.title('Toothpaste Sales Data (Scatter Plot)')
plt.legend()
plt.show()

plt.bar(sales_data['month_number'] - 0.2, sales_data['facecream'], width=0.4, label='Facecream Sales', color='blue')
plt.bar(sales_data['month_number'] + 0.2, sales_data['facewash'], width=0.4, label='Facewash Sales', color='orange')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.title('Facecream and Facewash Sales Data (Bar Chart)')
plt.legend()
plt.show()

total_sales = sales_data[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales Data for the Last Year (Pie Chart)')
plt.show()

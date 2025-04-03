import pandas as pd

employee_data = pd.read_csv('employee.csv')

print("First 7 records:")
print(employee_data.head(7))

print("\nEmployee names in alphabetical order:")
print(employee_data['name'].sort_values())

highest_salary_employee = employee_data.loc[employee_data['salary'].idxmax()]
print("\nEmployee with highest salary:")
print(highest_salary_employee['name'])

male_employees = employee_data[employee_data['gender'] == 'Male']['name']
print("\nMale employees:")
print(male_employees)

teams = employee_data['team'].unique()
print("\nTeams employees belong to:")
print(teams)

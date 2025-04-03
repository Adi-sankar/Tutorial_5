import pandas as pd
import matplotlib.pyplot as plt

data = {
    'rollno': [101, 102, 103, 104, 105],
    'name': ['David', 'Emily', 'Sophia', 'Daniel', 'Olivia'],
    'place': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Hyderabad'],
    'mark': [90, 85, 88, 93, 92]
}

df = pd.DataFrame(data)
df.to_csv('stud.csv', index=False)

students = pd.read_csv('stud.csv')

print("File contents:")
print(students)

students.set_index('rollno', inplace=True)
print("\nData with rollno as index:")
print(students)

print("\nName and Mark:")
print(students[['name', 'mark']])

print("\nRollno, Name, and Mark in order of Name:")
print(students[['name', 'mark']].sort_values(by='name'))

print("\nRollno, Name, and Mark in descending order of Mark:")
print(students[['name', 'mark']].sort_values(by='mark', ascending=False))

average_mark = students['mark'].mean()
median_mark = students['mark'].median()
mode_mark = students['mark'].mode()[0]

print("\nAverage Mark:", average_mark)
print("Median Mark:", median_mark)
print("Mode Mark:", mode_mark)

min_mark = students['mark'].min()
max_mark = students['mark'].max()

print("\nMinimum Mark:", min_mark)
print("Maximum Mark:", max_mark)

variance_mark = students['mark'].var()
std_deviation_mark = students['mark'].std()

print("\nVariance of Marks:", variance_mark)
print("Standard Deviation of Marks:", std_deviation_mark)

students['mark'].hist(bins=5, edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()

students.drop(columns=['place'], inplace=True)
print("\nData after removing the place column:")
print(students)

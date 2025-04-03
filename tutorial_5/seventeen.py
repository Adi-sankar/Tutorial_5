import pandas as pd

student_data = pd.read_csv('student.csv')

avg_cgpa = student_data['CGPA'].mean()
print(f"Average CGPA of students: {avg_cgpa:.2f}")

students_above_9 = student_data[student_data['CGPA'] > 9]
print("Students with CGPA > 9:")
print(students_above_9)

cse_students_above_9 = student_data[(student_data['Branch'] == 'CSE') & (student_data['CGPA'] > 9)]
print("CSE Students with CGPA > 9:")
print(cse_students_above_9)

max_cgpa_student = student_data[student_data['CGPA'] == student_data['CGPA'].max()]
print("Student with Maximum CGPA:")
print(max_cgpa_student)

avg_cgpa_by_branch = student_data.groupby('Branch')['CGPA'].mean()
print("Average CGPA of each branch:")
print(avg_cgpa_by_branch)

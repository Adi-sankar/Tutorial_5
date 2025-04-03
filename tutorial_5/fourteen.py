import csv

data = [
    ['Reg_no', 'Name', 'Sub_Mark1', 'Sub_Mark2', 'Sub_Mark3'],
    [10001, 'Jack', 76, 88, 76],
    [10002, 'John', 77, 84, 79],
    [10003, 'Alex', 74, 79, 81]
]

with open('student_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data has been written to student_data.csv")

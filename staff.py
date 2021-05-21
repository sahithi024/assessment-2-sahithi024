#average salary

import csv
name = []
salaries = []
maxi = 0

with open("employees.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        salaries.append(float(row["salary"]))

print("Average salary: ", sum(salaries) / len(salaries))
print('The Highest Salary is: $',maxi,'Produced by: ',name)


employees = {
    "Rahul": 50000,
    "Amit": 60000,
    "Neha": 55000,
    "Priya": 70000
}

print("Highest Salary:", max(employees.values()))
print("Lowest Salary:", min(employees.values()))

for emp in employees:
    employees[emp] *= 1.10

print("Updated Salaries:")
for name, salary in employees.items():
    print(name, salary)

import pyexcel
from MoneyParser import *


book = pyexcel.get_book(file_name="result.xls")
sheet = book.sheet_by_index(0)
people = [row for row in list(sheet)[1:] if row[0] != ""]

poorestPerson = min(people, key=lambda item: get_value_of_money_string(item[-1]))
richestPerson = max(people, key=lambda item: get_value_of_money_string(item[-1]))
print(poorestPerson)
print(richestPerson)

departmentsSalaries = {}
for person in people:
    department = person[2]
    if(department not in departmentsSalaries.keys()):
        departmentsSalaries[department] = (get_value_of_money_string(person[-1]), 1)
    else:
        (salary, workersCount) = departmentsSalaries[department]
        salary += get_value_of_money_string(person[-1])
        departmentsSalaries[department] = (salary, workersCount + 1)

print("Average departments salaries:")
for department in departmentsSalaries:
    (salary, workersCount) = departmentsSalaries[department]
    departmentsSalaries[department] = get_money_string_from_value(salary / workersCount)
    print(f"{department}:\t{departmentsSalaries[department]}")

xIndex = 13
sheet[xIndex, 1] = "Person name"
sheet[xIndex, 2] = "Person salary"
xIndex += 1
for person in [richestPerson, poorestPerson]:
    sheet[xIndex, 1] = person[1]
    sheet[xIndex, 2] = person[-1]
    xIndex += 1

sheet[xIndex, 1] = "Department"
sheet[xIndex, 2] = "Department average salary"
xIndex += 1
for department in departmentsSalaries:
    sheet[xIndex, 1] = department
    sheet[xIndex, 2] = departmentsSalaries[department]
    xIndex += 1

book.save_as("result.xls")
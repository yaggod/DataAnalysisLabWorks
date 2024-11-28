import openpyxl
import openpyxl.chart as chart
from MoneyParser import *


book = openpyxl.load_workbook("result.xlsx")
sheet = book.active
dataRows = sheet["A1":"I12"]
departmentsTotalSalaries = [(row[2].value, get_value_of_money_string(row[-1].value)) for row in dataRows[1:] if row[2].value.endswith("Итог")][:-1]
for index, cell in enumerate(departmentsTotalSalaries):
    (department, salary) = cell
    sheet[f"J{index+1}"] = department
    sheet[f"K{index+1}"] = salary

pie = chart.PieChart()

labels = chart.Reference(sheet, min_col=10, max_col=10, min_row=1, max_row=len(departmentsTotalSalaries))
data = chart.Reference(sheet, min_col=11 , max_col=11, min_row=1, max_row=len(departmentsTotalSalaries))
pie.add_data(data)
pie.set_categories(labels)
pie.title = "Pies sold by category"
sheet.add_chart(pie, "J1")


book.save("result.xlsx")
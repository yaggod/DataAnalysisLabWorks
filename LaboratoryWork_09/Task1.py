import pyexcel
from MoneyParser import *


header = ["Таб. номер", "Фамилия", "Отдел", "Сумма по окладу, руб.", "Сумма по надбавкам, руб.", "Сумма зарплаты, руб.", "Сумма НФДЛ, руб.", "НДФЛ, %", "Сумма к выдаче, руб."]
data = {
    "Sheet1": 
    [
        ["0002", "Петров П.П.", "Бухгалтерия", "3913,04р.", "2608,70р.", None, "13%", None, None],
        ["0005", "Васин В.В.", "Бухгалтерия", "5934,78р.", "913,04р.", None, "13%", None, None],
        ["0001", "Иванов И.И.", "Отдел кадров", "6000,00р.", "4000,00р.", None, "13%", None, None],
        ["0003", "Сидоров С.С.", "Отдел кадров", "5000,00р.", "4500,00р.", None, "13%", None, None],
        ["0006", "Львов Л.Л.", "Отдел кадров", "4074,07р.", "2444,44р.", None, "13%", None, None],
        ["0007", "Волков В.В.", "Отдел кадров", "1434,78р.", "1434,78р.", None, "13%", None, None],
        ["0004", "Мишин М.М.", "Столовая", "5500,00р.", "3500,00р.", None, "13%", None, None],

    ]
}






items = data["Sheet1"]
for item in items:
    item[5] = get_money_string_from_value(get_value_of_money_string(item[3]) + get_value_of_money_string(item[4]))
    item[7] = get_money_string_from_value(get_value_of_money_string(item[5]) * get_value_of_percent_string(item[6]))
    item[8] = get_money_string_from_value(get_value_of_money_string(item[5]) - get_value_of_money_string(item[7]))


newRows = {}
totalSumm = [None, None, "Общий Итог", "0,00р.", "0,00р.", "0,00р.", None, "0,00р.", "0,00р."]


for item in items:
    if (item[2] not in newRows):
        newRows[item[2]] = [None, None, item[2] + " Итог", "0,00р.", "0,00р.", "0,00р.", None, "0,00р.", "0,00р."]

    for i in [3,4,5,7,8]:
        newRows[item[2]][i] = get_money_string_from_value(get_value_of_money_string(item[i]) + get_value_of_money_string(newRows[item[2]][i]))
        totalSumm[i] = get_money_string_from_value(get_value_of_money_string(item[i]) + get_value_of_money_string(totalSumm[i]))
    

data["Sheet1"].extend(newRows.values())
data["Sheet1"].sort(key=lambda item: item[2])
data["Sheet1"].append(totalSumm)
data["Sheet1"].insert(0, header)

pyexcel.save_book_as(bookdict=data, dest_file_name="result.xlsx")
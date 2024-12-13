import docx

document = docx.Document("result.docx")
table = document.tables[0]

dictionary = {"MCU name" : "ATmega328"}

columnToUse = 0
for columnIndex, cell in enumerate(table.rows[0].cells):
    if(cell.text == dictionary["MCU name"]):
        columnToUse = columnIndex

if(columnToUse == 0):
    raise Exception("mcu is not found in the table")

headersColumn = table.columns[0]
MCUColumn = table.columns[columnToUse]

for index in range(1, len(table.rows)):
    dictionary[headersColumn.cells[index].text] = MCUColumn.cells[index].text

print(dictionary)
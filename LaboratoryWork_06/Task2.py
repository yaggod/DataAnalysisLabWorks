from argparse import ArgumentParser
from xml.etree import ElementTree
from pathlib import Path


parser = ArgumentParser()
parser.add_argument("--file", type=str, default="LaboratoryWork_06/inputFiles/ex_2.xml", help="File to modify")
args = parser.parse_args()

XMLToModify = ElementTree.parse(args.file)
fileRoot = XMLToModify.getroot()
details = fileRoot.find("Detail")
summary = fileRoot.find("Summary")

newItem = ElementTree.Element("Item")
ElementTree.SubElement(newItem, "ArtName").text = "Сыр Пармезан"
ElementTree.SubElement(newItem, "Barcode").text = "2000000000100"
ElementTree.SubElement(newItem, "QNT").text = "220,17"
ElementTree.SubElement(newItem, "QNTPack").text = "220,17"
ElementTree.SubElement(newItem, "Unit").text = "шт"
ElementTree.SubElement(newItem, "SN1").text = "00000015"
ElementTree.SubElement(newItem, "SN2").text = "10.04.2020"
ElementTree.SubElement(newItem, "QNTRows").text = "10"
details.append(newItem)
ElementTree.indent(newItem)

totalQNT = 0 
totalQNTRows = 0
for item in details:
    totalQNT += float(item.find("QNT").text.replace(",", "."))
    totalQNTRows += int(item.find("QNTRows").text)

summary.find("Summ").text = str(totalQNT)
summary.find("SummRows").text = str(totalQNTRows)


filePath = Path(args.file)
newFilePath = Path.joinpath(filePath.parent, filePath.stem + "_new" + filePath.suffix)


XMLToModify.write(newFilePath, encoding="utf-8", xml_declaration=True)
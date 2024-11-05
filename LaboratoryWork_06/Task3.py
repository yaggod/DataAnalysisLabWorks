from argparse import ArgumentParser
from xml.etree import ElementTree


parser = ArgumentParser()
parser.add_argument("--file", type=str, default="inputFiles/ex_3.xml", help="File to read")
args = parser.parse_args()



xmlToRead = ElementTree.parse(args.file)
fileRoot = xmlToRead.getroot()

products = fileRoot.findall("Документ/ТаблСчФакт/СведТов")
for product in products:
    print(f"Name: {product.get("НаимТов")}")
    print(f"Count: {product.get("КолТов")}")
    print(f"Price: {product.get("ЦенаТов")}")
    print()
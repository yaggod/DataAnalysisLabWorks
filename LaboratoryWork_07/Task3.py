from argparse import ArgumentParser
from pathlib import Path
import json

parser = ArgumentParser()
parser.add_argument("--file", type=str, default="LaboratoryWork_07/inputFiles/ex_3.json", help="File to validate")
args = parser.parse_args()


newItem = {
      "id": 3,
      "total": 150.00,
      "items": [
        {
          "name": "item 4",
          "quantity": 9,
          "price": 7500
        },
        {
          "name": "item 5",
          "quantity": 6,
          "price": 75.00
        }
      ]
}

with open(args.file, "r") as jsonFile:
    jsonData = json.load(jsonFile)

jsonData["invoices"].append(newItem)


filePath = Path(args.file)
newFilePath = Path.joinpath(filePath.parent, filePath.stem + "_new" + filePath.suffix)

with open(newFilePath, "w") as outputJsonFile:
    json.dump(jsonData, outputJsonFile, indent=2)

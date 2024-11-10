from argparse import ArgumentParser
import json

parser = ArgumentParser()
parser.add_argument("--file", type=str, default="LaboratoryWork_07/inputFiles/ex_2.json", help="File to validate")
args = parser.parse_args()


with open(args.file, "r") as jsonFile:
    jsonData = json.load(jsonFile)

result = {}


for item in jsonData["items"]:
    result[item["name"]] = item["phoneNumber"]

print(result)
from argparse import ArgumentParser
import jsonschema
import json

parser = ArgumentParser()
parser.add_argument("--file", type=str, default="inputFiles/ex_1.json", help="File to validate")
parser.add_argument("--schema", type=str, default="task1Schema.json", help="Validation schema")
args = parser.parse_args()


with open(args.schema, "r") as schemaFile:
    validationSchemaJSON = json.load(schemaFile)

with open(args.file, "r") as inputFile:
    JSON = json.load(inputFile)


try:
    jsonschema.validate(JSON, validationSchemaJSON)
except:
    print("File is not valid")
else:
    print("File is valid")
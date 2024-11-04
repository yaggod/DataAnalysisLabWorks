from argparse import ArgumentParser
from xmlschema import XMLSchema

parser = ArgumentParser()
parser.add_argument("--file", type=str, default="inputFiles/ex_1.xml", help="File to validate")
parser.add_argument("--schema", type=str, default="task1Schema.xsd", help="Validation schema")
args = parser.parse_args()



validationSchema = XMLSchema(args.schema)
if validationSchema.is_valid(args.file):
    print("File is valid")
else:
    print("File is not valid")
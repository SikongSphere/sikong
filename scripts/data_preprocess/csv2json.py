import json
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm

"""
A scripts to convert csv file to json file.
Example
>>>
python .\scripts\csv2json.py --csv .\label_data\example.csv --json .\label_data\example.json
"""

def parse():

    parser = ArgumentParser()
    parser.add_argument("--csv", type=str, help="Path to your csv file.")
    parser.add_argument("--json", type=str, help="Path to your json file.")

    return parser.parse_args()

def converter(csv_file, json_file):

    default_dict = {
        "type": "text2text",
        "instances": []
    }

    data = pd.read_csv(csv_file, encoding="gbk")


    for idx, row in tqdm(data.iterrows()):
        instance_dict = {
            "input": row["Question"],
            "output": row["Answer"]
        }
        default_dict["instances"].append(instance_dict)

    with open(json_file, mode="w", encoding="utf-8") as f:
        js_obj = json.dumps(default_dict, ensure_ascii=False, indent=4)
        f.write(js_obj)


if __name__ == '__main__':
    parser = parse()
    converter(parser.csv, parser.json)

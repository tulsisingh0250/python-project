import json
import csv
input_file="api_data.json"
output_file="converted_data.csv"
with open(input_file,"r")as file:
    data=json.load(file)
headers = data[0].keys()
with open(output_file,"w",newline="")as file:
    writer=csv.DictWriter(file,fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
print("conservation complete successfuly")
print("Records converted:",len(data))
print("csv file converted:",output_file)
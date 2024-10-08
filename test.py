import csv
import json

# 讀取CSV文件
csv_file_path = 'a430efeb-98db-44bb-a758-0f98337cff3f.csv'
json_file_path = 'output.json'

data = []
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append(row)

# 將數據寫入JSON文件
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print(f"CSV文件已成功轉換為JSON文件，並保存至 {json_file_path}")
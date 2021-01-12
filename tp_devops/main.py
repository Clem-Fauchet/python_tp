#!/usr/bin/env python
import csv
import os

from csv import DictReader
from typing import List, Dict

# with open("departements-france.csv", newline="") as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
#     for row in spamreader:
#         print(", ".join(row))

file_handle = open("tp_devops/data/departements-france.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str, str]] = []

for row in csv_reader:
    str_row: Dict[str, str] = {}
    for column in row:
        str_row[column] = str(row[column])
    table.append(str_row)
print(table)


file_handle.close()
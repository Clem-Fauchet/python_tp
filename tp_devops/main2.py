#!/usr/bin/env python
import csv
import os
import pandas as pd


# with open("tp_devops/data/departements-france.csv", newline="") as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
#     for row in spamreader:
#         print(", ".join(row))


with open("tp_devops/data/departements-france.csv", "r", encoding="utf8") as f:
    # df = pd.read_csv("tp_devops/data/departements-france.csv")
    os.mkdir("tp_devops/cible")
    os.chdir("tp_devops/cible/")
    for row in f:
        os.mkdir(row.strip())

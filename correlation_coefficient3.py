import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    p_d = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            p_d.append(float(row["Days Present"]))
    return{"x": marks, "y": p_d}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("The correlation between marks in the percentage vs the days the student is present is ", + correlation[0,1])

def setup():
    data_path = "data3.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()
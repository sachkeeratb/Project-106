import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x": coffee, "y": sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("The correlation between amount of coffee people drink (ml) vs the amount of time people sleep (hours) is ", + correlation[0,1])

def setup():
    data_path = "data4.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()
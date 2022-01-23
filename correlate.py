import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    tvSize = []
    hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tvSize.append(float(row["Size of TV"]))
            hours.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
        return{
            "x":tvSize,"y":hours
        }
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("The correlation between tv size and hours watched are ","\n",correlation[0,1])
def setup():
    data_path = "tv_size.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
setup()


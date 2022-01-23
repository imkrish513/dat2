import plotly.express as px
import csv
import numpy as np 

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
        fig.show()
def getDataSource(data_path):
    daysPresent = []
    marks = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            daysPresent.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))
    return{
        "x":daysPresent,"y":marks
    }
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between days present and marks  ", "\n", correlation[0,1])

def setup():
    data_path = "attendence_marks.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)
setup()
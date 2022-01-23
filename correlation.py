import plotly.express as px
import csv
import numpy as np 

def getDataSource(data_path):
    iceCreamSales = []
    coldDrinkSales = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            iceCreamSales.append(float(row["Temperature"]))
            coldDrinkSales.append(float(row["Ice-cream Sales( ₹ )"]))
    return{
        "x":iceCreamSales,"y":coldDrinkSales
    }
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between ice cream and temperature sales  ", "\n", correlation[0,1])
def setup():
    data_path = "temp_icecream.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
setup()
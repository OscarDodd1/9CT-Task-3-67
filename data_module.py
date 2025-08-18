import pandas as pd
import matplotlib as plt

df = pd.read_csv("Data/Data1.csv")

def amount_of_titles():
    num_columns = len(df.columns)

    return num_columns

def get_name(place):
    data = None

    try:
        data = df.iloc[:,place]
    except:
        return False

    return data.name

def visualise_graph(num):
    graphToShow = df.iloc[:,num]
    
    print("\n===Select Type===")
    print("1 - Bar")
    print("2 - Pie")
    print("=================")

    typeOfGraph = input("Choice: ")

    if typeOfGraph == "1":
        try:
            print("print the graph")

def get_table(num):
    TableToShow = df.iloc[:,num]

    return TableToShow
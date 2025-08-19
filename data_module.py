import pandas as pd
import matplotlib.pyplot as plt

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

def visualise_graph(num1, num2):
    graph1 = get_name(num1)
    graph2 = get_name(num2)
    
    print("\n===Select Type===")
    print("1 - Bar")
    print("2 - Scatter")
    print("3 - Pie")
    print("=================")

    typeOfGraph = input("Choice: ")

    if typeOfGraph == "1": #bar
        try:
            df.plot(
                kind = 'bar',
                x = graph1,
                y = graph2,
                color = 'blue',
                alpha = 0.3,
                title = 'lol'
                )
            
            plt.show()
        except:
            print("Cant show graph")

def get_table(num):
    TableToShow = df.iloc[:,num]

    return TableToShow

def filter_table(num):
    TableToFilter = df.iloc[:,num]
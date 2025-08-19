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

def visualise_graph():
   
    
    print("\n===Select Type===")
    print("1 - Scatter")
    print("2 - Bar")
    print("3 - Pie")
    print("=================")

    #typeOfGraph = input("Choice: ")

    #if typeOfGraph == "1": #bar
    df.plot(
            kind ='bar',
            x = 'Do you study in public spaces? e.g. library, park, train',
            y = 'How close do you live to a public space?',
            color = 'blue',
            alpha = 0.3,
            title = 'lol'
        )

    plt.show()

def get_table(num):
    TableToShow = df.iloc[:,num]

    return TableToShow

visualise_graph()
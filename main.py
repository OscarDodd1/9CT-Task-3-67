import data_module
import time

def choose_table():
    table_chosen = 0

    page = 1
    pages = 0
    
    num = data_module.amount_of_titles() - 1 #-1 because the timestamp from the form doesnt need to be included

    while num > 0:
        pages += 1
        num -= 5
    
    while table_chosen == 0:
        print("\n===Tables===")
        if data_module.get_name((page * 5) - 4) != False:
            print(f"1 - {data_module.get_name((page * 5) - 4)}")
        else:
            print(f"1 - None")
        if data_module.get_name((page * 5) - 3) != False:
            print(f"2 - {data_module.get_name((page * 5) - 3)}")
        else:
            print(f"2 - None")
        if data_module.get_name((page * 5) - 2) != False:
            print(f"3 - {data_module.get_name((page * 5) - 2)}")
        else:
            print(f"3 - None")
        if data_module.get_name((page * 5) - 1) != False:
            print(f"4 - {data_module.get_name((page * 5) - 1)}")
        else:
            print(f"4 - None")
        if data_module.get_name(page * 5) != False:
            print(f"5 - {data_module.get_name(page * 5)}")
        else:
            print(f"5 - None")

        print("============")
        print(f"Page {page}/{pages} | < to go back | > to go forward | ~ to go to start |")

        choice1 = input("\nChoice: ")

        if choice1 == "1":
            table_chosen = (page * 5) - 4
        elif choice1 == "2":
            table_chosen = (page * 5) - 3
        elif choice1 == "3":
            table_chosen = (page * 5) - 2
        elif choice1 == "4":
            table_chosen = (page * 5) - 1
        elif choice1 == "5":
            table_chosen = page * 5
        elif choice1 == "<":
            if page > 1:
                page -= 1
            else:
                print("\nAlready at the first page")
                time.sleep(2)
        elif choice1 == ">":
            if page < pages:
                page += 1
            else:
                print("\nAlready at the last page")
                time.sleep(2)
        elif choice1 == "~":
            return False
        else:
            print("Choose from 1-5")
            time.sleep(2)
    
    return table_chosen

def select_option():
    print("\n===Select Option===")
    print("1 - View Table")
    print("2 - Filter Table")
    print("3 - Visualise")
    print("4 - Exit")
    print("===================")

    choice1 = input("\nChoice: ")

    if choice1 == "1":
        tableNum = choose_table()
        
        if tableNum != False:
            table = data_module.get_table(tableNum)

            print(f"\n====={table.name}=====")

            for i in table:
                print(i)

            #this bit is literaly jus for looks
            numlen = len(table.name)
            chars = ""

            while numlen > 0:
                chars += "="
                numlen -= 1

            print(f"====={chars}=====")

    elif choice1 == "2":
        print("Choose table and filter type")
    elif choice1 == "3":
        print("choose table to visualise")
    elif choice1 == "4":
        exit()
    else:
        print("What...")

while True:
    select_option()
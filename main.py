def choose_table():
    table_chosen = "table" #placeholder
    print("\n===Tables===")
    ##print first 5 tables
    return table_chosen

    #!!!! for table selection, make it so there is pages that you can flip through that displays the tables
    #make it so it shows 5 in a page
    #what itl look like:
    #|===Tables===|
    #1 - Table1
    #2 - Table2
    #3 - Table3
    #4 - Table4
    #5 - Table5
    #Page 1/2

    #|===Tables===|
    #1 - Table6
    #2 - Table7
    #3 - Table8
    #4 - None
    #5 - None
    #Page 2/2

def select_option():
    print("\n===Select Option===")
    print("1 - View Table")
    print("2 - Filter Table")
    print("3 - Visualise")
    print("4 - Exit")
    print("===================")

    choice1 = input("\nChoice: ")

    if choice1 == "1":
        print(choose_table())
    elif choice1 == "2":
        print("Choose table and filter type")
    elif choice1 == "3":
        print("choose table to visualise")
    elif choice1 == "4":
        print("Exit")
    else:
        print("What...")

select_option()
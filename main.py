def select_option():
    print("\n===Select Option===")
    print("1 - View Table")
    print("2 - Filter Table")
    print("3 - Visualise")
    print("4 - Exit")
    print("===================")

    choice1 = input("\nChoice: ")

    print("\n")

    if choice1 == "1":
        print("Choose table")
    elif choice1 == "2":
        print("Choose table and filter type")
    elif choice1 == "3":
        print("choose table to visualise")
    elif choice1 == "4":
        print("Exit")
    else:
        print("What...")

select_option()
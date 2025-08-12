def select_option():
    print("===Select Option===")
    print("1 - View Table")
    print("2 - Filter Table")
    print("3 - Visualise")
    print("4 - Exit")
    print("===================")

    choice1 = input("Choice: ")

    if choice1 == "1":
        print("a")
    elif choice1 == "2":
        print("b")
    elif choice1 == "3":
        print("c")
    elif choice1 == "4":
        print("Exit")
    else:
        print("What...")

select_option()
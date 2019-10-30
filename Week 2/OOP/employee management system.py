from Employee import Employee

command = ""
employee_dict = dict()

while command != "6":
    command = input("Select the program (1-5) to run:\n1. Search for an employee\n2. Add new employee\n3. Update employee details\n4. Delete an employee\n5. Show all employees\n6. Quit the program\nEnter your command (1-5): ")
    print()
    if command == "1":
        search_id = input("Enter ID of employee you want to search: ")
        while search_id not in employee_dict.keys() and search_id != "q":
            search_id = input("Invalid ID. Try again or enter 'q' to exit: ").lower()
        if search_id != "q":
            employee = employee_dict[search_id]
            print(employee)
    elif command == "2":
        name = input("Enter name: ")
        ID = input("Enter ID: ")
        while ID in employee_dict.keys():
            ID = input("ID is used already. Enter another ID: ")
        employee = Employee(name, ID, input("Enter Department: "), input("Enter Title: "))
        employee_dict[ID] = employee
    elif command == "3":
        update_id = input("Enter ID of employee you want to update: ")
        while update_id not in employee_dict.keys() and update_id != "q":
            update_id = input("Invalid ID. Try again or enter 'q' to exit: ").lower()
        if update_id != "q":
            employee = employee_dict[update_id]
        attribute_to_be_updated = input("Enter field you want to update(Name/ID/Department/Title): ").lower()
        while attribute_to_be_updated not in ["name", "id", "department", "title"]:
            print("Invalid field. Try again.")
            attribute_to_be_updated = input("Enter field you want to update(Name/ID/Department/Title): ").lower()
        if attribute_to_be_updated == "name":
            employee.set_name(input("Enter new name: "))
        elif attribute_to_be_updated == "id":
            ID = input("Enter new ID: ")
            employee.set_id(ID)
            employee_dict[ID] = employee
            del employee_dict[update_id]
        elif attribute_to_be_updated == "department":
            employee.set_department(input("Enter new Department: "))
        else:
            employee.set_title(input("Enter new Title: "))
    elif command == "4":
        delete_id = input("Enter ID of employee you want to delete: ")
        while delete_id not in employee_dict.keys() and delete_id != "q":
            delete_id = input("Invalid ID. Try again or enter 'q' to exit: ").lower()
        if delete_id != "q":
            del employee_dict[delete_id]
            print("Employee Removed")
    elif command == "5":
        for employee in employee_dict.values():
            print(employee)
    elif command == "6":
        print("Program exited.")
        break
    else:
        print("Invalid command.")
    print()

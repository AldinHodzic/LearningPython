
def add_to_end(list):
    user_input = input("Enter task: ")
    list.append(user_input)

def print_list(list):
    astring = ", ".join(list)
    print(astring)

def remove_task(list):
    user_input = input("Enter task you want to remove: ")
    if user_input in list:
        list.remove(user_input)
                
def remove_at_index(list):
    user_input = input("Enter index you want to remove: ")
    try:
        idx = int(user_input)
        if idx < len(list) and idx > -1:
            del list[idx]
    except ValueError:
        print("Error with input.")

def add_at_index(list):
    user_input = input("Enter index where you want to add task: ")
    try:
        idx = int(user_input)
        if idx >= 0 and idx < len(list):
            user_input = input("Enter task you want to add: ")
            list.insert(idx, user_input)
    except ValueError:
        print("Error with input.")

list = ["make it work"]

while True:
    print("Enter 1(add to end), 2(remove task), 3(remove at index), 4(add to index), " \
    "5(print), 6(count), 7(exit)")
    while True:
        user_input = input()

        try:
            choice = int(user_input)
            break
        except ValueError:
            print("Try again.")

    if choice>=1 or choice<=7:
        
        if choice == 7:
            break
        elif choice == 1:
            add_to_end(list)
        elif choice == 2:
            remove_task(list)
        elif choice == 3:
            remove_at_index(list)
        elif choice == 4:
            add_at_index(list)
        elif choice == 5:
            print_list(list)
        elif choice == 6:
            print("Enteries in list:", len(list))

with open("tasks.txt", "w") as file:
    for item in list:
        file.write(item + "\n")

print("Exited program")
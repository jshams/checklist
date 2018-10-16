checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(index, list_item)
        index += 1

def mark_completed(index):
    update(index, ("√" + read(index)))

def user_input(prompt):
    # the input function will display a message in the terminal
    user_input = input(prompt)
    return user_input

def select(function_code):

    if function_code in "Aa":
        item = input("Add item:")
        create(item)
    elif function_code in "Rr":
        index = int(input("Enter index:"))
        if index <= len(checklist):
            print(read(index))
        else:
            print("Invalid index")
    elif function_code in "Pp":
        list_all_items()
    elif function_code in "Cc":
        index = int(input("Item index:"))
        if index <= len(checklist):
            mark_completed(index)
        else:
            print("invalid index")
    elif function_code in "Qq":
        return False
    elif function_code in "Uu":
        index = int(input("Index:"))
        if index <= len(checklist):
            item = input("Updated item")
            update(index,item)
        else:
            print("Invalid Index")
    elif function_code in "Ee":
        index = int(input("Item index:"))
        if index <= len(checklist):
            destroy(index)
        else:
            print("Invalid index")
    else:
        print("Unknown Option")
    return True

def test():

    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))

    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)



#test()

running = True
while running:
    selection = user_input(
        "Press A to add to list, R to read from list, P to display list, C to check item, U to update item in list, E to erase item from list, and Q to quit")
    running = select(selection)

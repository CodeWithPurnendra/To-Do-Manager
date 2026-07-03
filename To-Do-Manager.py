def add_task():
    task = input("Enter your task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Tasks Saved successfully")


def read_task():
    try:
        with open("tasks.txt", "r") as f:
            print("---- Your Saved Tasks ----")
            print(f.read())
    except FileNotFoundError:
        print("File Not Found")


while True:
    choice = int(input("\nChoose: (1) Add Task, (2) Read Task: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        read_task()
    else:
        print("Invalid choice,try again")

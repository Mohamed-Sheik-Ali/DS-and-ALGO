queue = []

# Here we can set the priority using tuple like (priority, value) eg: (1, "Some value")


def enqueue():

    element = input("Enter an element: ")
    queue.append(element)
    queue.sort(reverse=True)
    print(f"{queue} is the current queue")


def dequeue():

    if not queue:
        print("Oops! it\'s empty")
    else:
        e = queue.pop(0)
        print(f"{e} is removed")
        print(f'Current queue {queue}')


while True:

    print("What are you going to do? 1/2/3: 1) Enqueue.  2) Dequeue. 3) Exit.")
    print("")
    choice = int(input("Enter a choice 1/2/3: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation.")

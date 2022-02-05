from queue import PriorityQueue

q = PriorityQueue()


def enqueue():

    element = int(input("Enter an element: "))
    q.put(element)
    print(f"{q.qsize()} is the current size of the queue")


def dequeue():

    if not q:
        print("Oops! it\'s empty")
    else:
        e = q.get()
        print(f"{e} is removed")
        print(f'Current queue size {q.qsize()}')


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

def create_queue():
    return []


def enqueue(queue, element):
    return queue.append(element)


def dequeue(queue):
    if len(queue):
        return queue.pop(0)


def is_empty(queue):
    return bool(len(queue))


def peek(queue):
    if len(queue):
        return queue[0]


# ExempelanvÃ¤ndning:
if __name__ == "__main__":
    queue = create_queue()
    enqueue(queue, "A")
    enqueue(queue, "B")
    enqueue(queue, "C")
    print("Forsta element i kÃ¶n Ã¤r:", peek(queue))
    print("Tar ut element:", dequeue(queue))
    print("FÃ¶rsta element i kÃ¶n Ã¤r:", peek(queue))
    print("Tar ut element:", dequeue(queue))
    print("Tar ut element:", dequeue(queue))
    print("Tar ut element:", dequeue(queue))

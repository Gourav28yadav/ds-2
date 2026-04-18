#name: Rudra pratap singh
#roll no.: 2501730451
# ---- Task 1: Dynamic Array ----

class DynamicArray:
    def __init__(self, cap=2):
        self.cap = cap
        self.size = 0
        self.arr = [None] * self.cap

    def append(self, val):
        if self.size == self.cap:
            # need to resize
            old = self.cap
            self.cap = self.cap * 2
            new_arr = [None] * self.cap
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            print(f"  Resized: {old} -> {self.cap}")

        self.arr[self.size] = val
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("empty array cant pop")
            return None
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def display(self):
        items = []
        for i in range(self.size):
            items.append(str(self.arr[i]))
        print(f"  Array: [{', '.join(items)}]  size={self.size} cap={self.cap}")


# ---- Task 2: Singly Linked List ----

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def insert_at_end(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = n

    def delete_by_value(self, val):
        if self.head == None:
            print(f"  list empty, cant delete {val}")
            return
        if self.head.data == val:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next != None:
            if temp.next.data == val:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"  {val} not found")

    def traverse(self):
        items = []
        temp = self.head
        while temp != None:
            items.append(str(temp.data))
            temp = temp.next
        if items:
            print("  " + " -> ".join(items))
        else:
            print("  (empty)")


# ---- Doubly Linked List ----

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        n = DNode(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n

    def insert_after_node(self, target, data):
        temp = self.head
        while temp != None:
            if temp.data == target:
                n = DNode(data)
                n.prev = temp
                n.next = temp.next
                if temp.next != None:
                    temp.next.prev = n
                else:
                    self.tail = n
                temp.next = n
                return
            temp = temp.next
        print(f"  {target} not found")

    def delete_at_position(self, pos):
        # 0-based position
        if self.head == None:
            print("  list empty")
            return
        temp = self.head
        idx = 0
        while temp != None and idx < pos:
            temp = temp.next
            idx += 1
        if temp == None:
            print(f"  position {pos} out of range")
            return

        if temp.prev != None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next != None:
            temp.next.prev = temp.prev
        else:
            self.tail = temp.prev

    def traverse(self):
        items = []
        temp = self.head
        while temp != None:
            items.append(str(temp.data))
            temp = temp.next
        if items:
            print("  " + " <-> ".join(items))
        else:
            print("  (empty)")


# ---- Task 3: Stack using SLL ----

class Stack:
    def __init__(self):
        self.ll = SinglyLinkedList()
        self.count = 0

    def push(self, val):
        self.ll.insert_at_beginning(val)
        self.count += 1

    def pop(self):
        if self.count == 0:
            print("  stack underflow")
            return None
        val = self.ll.head.data
        self.ll.head = self.ll.head.next
        self.count -= 1
        return val

    def peek(self):
        if self.count == 0:
            return None
        return self.ll.head.data

    def is_empty(self):
        return self.count == 0

    def display(self):
        self.ll.traverse()


# ---- Queue using SLL ----

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0

    def enqueue(self, val):
        n = Node(val)
        if self.rear_node == None:
            self.front_node = n
            self.rear_node = n
        else:
            self.rear_node.next = n
            self.rear_node = n
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("  queue empty")
            return None
        val = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node == None:
            self.rear_node = None
        self.count -= 1
        return val

    def front(self):
        if self.count == 0:
            return None
        return self.front_node.data

    def is_empty(self):
        return self.count == 0

    def display(self):
        items = []
        temp = self.front_node
        while temp != None:
            items.append(str(temp.data))
            temp = temp.next
        if items:
            print("  " + " -> ".join(items))
        else:
            print("  (empty)")


# ---- Task 4: Balanced Parentheses Checker ----

def is_balanced(expr):
    s = Stack()
    match = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in '({[':
            s.push(ch)
        elif ch in ')}]':
            if s.is_empty():
                return False
            top = s.pop()
            if top != match[ch]:
                return False

    return s.is_empty()


# ---- main ----

if __name__ == "__main__":

    print("===== TASK 1: Dynamic Array =====")
    da = DynamicArray(2)
    print("appending 12 elements:")
    for i in range(1, 13):
        da.append(i)
    da.display()

    print("popping 3 times:")
    for _ in range(3):
        v = da.pop()
        print(f"  popped {v}")
    da.display()

    print("\n===== TASK 2A: Singly Linked List =====")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(30)
    sll.insert_at_beginning(20)
    sll.insert_at_beginning(10)
    print("after inserting 10,20,30 at beginning:")
    sll.traverse()

    sll.insert_at_end(40)
    sll.insert_at_end(50)
    sll.insert_at_end(60)
    print("after inserting 40,50,60 at end:")
    sll.traverse()

    sll.delete_by_value(30)
    print("after deleting 30:")
    sll.traverse()

    sll.delete_by_value(99)
    print("after trying to delete 99:")
    sll.traverse()

    print("\n===== TASK 2B: Doubly Linked List =====")
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    print("initial list:")
    dll.traverse()

    dll.insert_after_node(20, 25)
    print("after inserting 25 after 20:")
    dll.traverse()

    dll.delete_at_position(1)
    print("after deleting position 1:")
    dll.traverse()

    dll.delete_at_position(3)
    print("after deleting last position:")
    dll.traverse()

    print("\n===== TASK 3A: Stack =====")
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    print("stack after pushing 10, 20, 30:")
    st.display()
    print(f"peek: {st.peek()}")
    print(f"pop: {st.pop()}")
    print(f"pop: {st.pop()}")
    print("stack now:")
    st.display()

    print("\n===== TASK 3B: Queue =====")
    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    print("queue after enqueue 100, 200, 300:")
    q.display()
    print(f"front: {q.front()}")
    print(f"dequeue: {q.dequeue()}")
    print(f"dequeue: {q.dequeue()}")
    print("queue now:")
    q.display()

    print("\n===== TASK 4: Parentheses Checker =====")
    tests = ["([])", "([)]", "(((", "", "{[()]}", "((()))", "}{"]
    for t in tests:
        res = is_balanced(t)
        label = "Balanced" if res else "Not balanced"
        if t == "":
            print(f'  "" (empty) => {label}')
        else:
            print(f'  "{t}" => {label}')

    print("\ndone.")

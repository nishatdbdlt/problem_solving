class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"{self.roll} - {self.name} - {self.marks}"


# ===== ARRAY =====
class StudentArray:
    def __init__(self):
        self.data = []

    def add(self, student):
        self.data.append(student)

    def search(self, roll):
        for s in self.data:
            if s.roll == roll:
                return s
        return None

    def sort_by_marks(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j].marks > self.data[j+1].marks:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]


# ===== LINKED LIST =====
class Node:
    def __init__(self, student):
        self.student = student
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add(self, student):
        new = Node(student)
        new.next = self.head
        self.head = new

    def search(self, roll):
        temp = self.head
        while temp:
            if temp.student.roll == roll:
                return temp.student
            temp = temp.next
        return None


# ===== STACK =====
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop() if self.items else None


# ===== QUEUE =====
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0) if self.data else None


# ===== HASHTABLE =====
class Hashtable:
    def __init__(self):
        self.table = {}

    def add(self, student):
        self.table[student.roll] = student

    def get(self, roll):
        return self.table.get(roll)


# ===== BST =====
class BSTNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None


class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, student):
        self.root = self._insert(self.root, student)

    def _insert(self, root, student):
        if not root:
            return BSTNode(student)
        if student.marks < root.student.marks:
            root.left = self._insert(root.left, student)
        else:
            root.right = self._insert(root.right, student)
        return root

    def inorder(self):
        arr = []
        self._inorder(self.root, arr)
        return arr

    def _inorder(self, root, arr):
        if root:
            self._inorder(root.left, arr)
            arr.append(root.student)
            self._inorder(root.right, arr)


# ===== GRAPH =====
class StudentGraph:
    def __init__(self):
        self.graph = {}

    def add_friend(self, a, b):
        self.graph.setdefault(a, []).append(b)
        self.graph.setdefault(b, []).append(a)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(self.graph.get(node, []))
        return visited


# ===== INSTANCES =====
arr = StudentArray()
ll = StudentLinkedList()
undo_stack = Stack()
requests = Queue()
htable = Hashtable()
bst = StudentBST()
graph = StudentGraph()


# ===== MAIN LOOP =====
while True:
    print("\n____________________________")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Sort by Marks (Array)")
    print("4. Show Rank List (BST - Inorder)")
    print("5. Undo Last Add")
    print("6. Add Friendship")
    print("7. Show Friend Circle (BFS)")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Roll: "))
        name = input("Name: ")
        marks = int(input("Marks: "))
        s = Student(roll, name, marks)

        arr.add(s)
        ll.add(s)
        htable.add(s)
        bst.insert(s)
        undo_stack.push(s)

        print("Student added!")

    elif choice == 2:
        roll = int(input("Enter roll to search: "))
        print("Array Search:", arr.search(roll))
        print("Linked List Search:", ll.search(roll))
        print("Hash Table Search:", htable.get(roll))

    elif choice == 3:
        arr.sort_by_marks()
        print("Sorted by Marks:", arr.data)

    elif choice == 4:
        print("Rank List (BST):", bst.inorder())

    elif choice == 5:
        last = undo_stack.pop()
        print("Undo:", last)

    elif choice == 6:
        a = input("Student A: ")
        b = input("Student B: ")
        graph.add_friend(a, b)
        print("Friendship Added!")

    elif choice == 7:
        name = input("Start from student: ")
        print("Friend Circle:", graph.bfs(name))

    else:
        print("Exiting...")
        break

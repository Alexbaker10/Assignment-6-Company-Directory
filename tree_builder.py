class EmployeeNode:
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    def __init__(self):
        self.root = None
        
    def insert(self, manager_name, employee_name, side, cur_node=None):
        if cur_node == None:
            if self.root == None:
                return False
            cur_node = self.root
    
        if cur_node.name == manager_name:
            if side == "left" and cur_node.left == None:
                cur_node.left = EmployeeNode(employee_name)
                return True
            elif side == "right" and cur_node.right == None:
                cur_node.right = EmployeeNode(employee_name)
                return True
        else return False
    
        left_good = False
        if cur_node.left:
            left_good = self.insert(manager_name, employee_name, side, cur_node.left)
        right_good = False
        if cur_node.right:
            right_good = self.insert(manager_name, employee_name, side, cur_node.right)
    
        return left_good or right_good
        
    def print_tree(self,node=None, level=0):
        if node is None:
            node = self.root
        if node is None:
            print("Your tree is empty")
            return
        print("  " * level + node.name)
        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)
# Test your code here
# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

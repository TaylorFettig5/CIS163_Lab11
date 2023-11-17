"""
Taylor Fettig
Lab 11
11/15/2023
"""

# Creating the Node class that represents each node in the tree.
class Node:
    def __init__(self, value):
        self.value = value
        # Pointers to left and right node
        self.left = None
        self.right = None

# Creating the BinaryTree class
class BinaryTree:
    # Initializes with empty root node
    def __init__(self):
        self.root = None
    
    # Inserts a new node with a given value into the binary tree. If the tree is empty, it sets the root node. 
    # If not, it calls a recursive helper function.   
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)
            
    # Recursive function that helps in inserting a node by comparing values and traversing either left or right of
    # the tree based on comparisons.        
    def _insert_recursive(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)
    
    # In order traversal of the tree, stores values in list and returns list.            
    def in_order_traversal(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result
    
    # Visits the left subtree, appends the current node's value to the result list, then visits the right subtree.
    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)

    # Pre order traversal of the tree, stores values in list and returns list.  
    def pre_order_traversal(self):
        result = []
        self._pre_order_recursive(self.root, result)
        return result
    
    # Appends the current node's value to the result list, then recursively traverses the left and right subtrees.
    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    # Calculates and returns the height of the binary tree.
    def height(self):
        return self._height_recursive(self.root)

    # Computes the height of the tree. Starts from the root and recursively calculates the height of the left 
    # and right subtrees, returning the maximum height between them.
    def _height_recursive(self, node):
        if node is None:
            return -1
        else:
            left_height = self._height_recursive(node.left)
            right_height = self._height_recursive(node.right)
            return max(left_height, right_height) + 1
            
    # Calculates the sum of every path.        
    def sum_of_paths(self):
        paths = []
        self._sum_of_paths_recursive(self.root, [], paths)
        return paths

    # Traverses each path from the root to a leaf node, calculating the sum and appending it to the paths list.
    def _sum_of_paths_recursive(self, node, current_path, paths):
        if node:
            current_path.append(node.value)
            if node.left is None and node.right is None:
                paths.append(sum(current_path))
            else:
                self._sum_of_paths_recursive(node.left, current_path.copy(), paths)
                self._sum_of_paths_recursive(node.right, current_path.copy(), paths)
    
    # Returns size of tree.
    def size(self):
        return self._size_recursive(self.root)

    # Counts each node by summing up nodes in the left and right subtrees, including the root node.
    def _size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
     
    # Returns the level of the node.
    def level_of_node(self, value):
        return self._level_of_node_recursive(self.root, value, 0)

    # Traversing the tree to find nodes level.
    def _level_of_node_recursive(self, node, value, level):
        if node is None:
            return -1
        if node.value == value:
            return level
        down_level = self._level_of_node_recursive(node.left, value, level + 1)
        if down_level != -1:
            return down_level
        down_level = self._level_of_node_recursive(node.right, value, level + 1)
        return down_level

    # Returns the value of every node on a given level.   
    def nodes_at_level(self, level):
        result = []
        self._nodes_at_level_recursive(self.root, level, result)
        return result

    # Traverses the tree to find nodes at the specified level.
    def _nodes_at_level_recursive(self, node, level, result):
        if node is None:
            return
        if level == 0:
            result.append(node.value)
        else:
            self._nodes_at_level_recursive(node.left, level - 1, result)
            self._nodes_at_level_recursive(node.right, level - 1, result)
     
    # Finds and deletes a node with a given value.        
    def delete_node(self, value):
        self.root = self._delete_node_recursive(self.root, value)

    # Preforming the deletion of the node. 
    def _delete_node_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_node_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_node_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min_value_node(node.right)
                node.value = temp.value
                node.right = self._delete_node_recursive(node.right, temp.value)
        return node
        
    # Finds the minimum value node in a subtree.
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Calling BinaryTree class and inserting data.           
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("In-order traversal:", tree.in_order_traversal())
print("Pre-order traversal:", tree.pre_order_traversal())
print("Height of the tree:", tree.height())
print("Sum of paths:", tree.sum_of_paths())
print("Nodes at level 2:", tree.nodes_at_level(2))
print("Size of the tree:", tree.size())

tree.delete_node(3)
print("In-order traversal after deleting node with value 3:", tree.in_order_traversal())

print("Level of node with value 7:", tree.level_of_node(7))

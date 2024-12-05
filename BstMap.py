from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):  # put the word in the bst
        f = Node(key, value, None, None)  # creat a node
        if self.key is None:  # if the actual Node is none
            self = f  # we change it to f
            return
        if self.key == key:  # if the actual node is the same as our word
            self.value = value
            return
        elif self.key > key:
            if self.left is None:  # if left is none
                self.left = f  # we replace it by f
            else:  # if left is not None
                self.left.put(key, value)  # we enter in the left branch
            return
        elif self.key < f.key:
            if self.right is None:  # if right is none
                self.right = f  # we replace right by f
            else:  # if right is not None
                self.right.put(key, value)  # we enter in right
            return

    def to_string(self):  # creat a str from each word in bst
        A = None  # for left
        B = None  # for right
        string = "(" + str(self.key) + "," + str(self.value) + ")" + " "
        if self.left is not None:  # we enter in right and left if not None
            A = self.left.to_string()
        if self.right is not None:
            B = self.right.to_string()
        if A is not None and B is not None:  # we add value A and B to our str
            string = A + string + B
        elif A is not None:
            string = A + string
        elif B is not None:
            string = string + B
        return string  # return it

    def count(self):  # count number of Node
        A = None
        B = None
        count = 1
        if self.right is not None:  # get number of node in right and left
            A = self.right.count()
        if self.left is not None:
            B = self.left.count()
        if A is not None and B is not None:  # add it to count
            count = count + A + B
        elif A is not None:
            count = count + A
        elif B is not None:
            count = count + B
        return count  # return count

    def get(self, key):  # get a word
        A = None
        B = None
        J = None
        if self.key == key:  # if actual node is the word
            J = self.value  # we take his value
        if self.right is not None:
            A = self.right.get(key)
        if self.left is not None:
            B = self.left.get(key)
        if A is not None:  # we return the one that has a value
            return A
        elif B is not None:
            return B
        else:
            return J

    def max_depth(self):  # get the max depth
        depthright = None
        depthleft = None
        if self.right is not None:  # enter in right and left and get the depth
            depthright = self.right.max_depth()
        if self.left is not None:
            depthleft = self.left.max_depth()
        if self.right is not None and self.left is not None:
            if depthright >= depthleft:  # get the biggest depth and add 1
                depthright = depthright + 1
                return depthright
            else:
                depthleft = depthleft + 1
                return depthleft
        else:
            if self.right is not None:
                depthright = depthright + 1
                return depthright
            elif self.left is not None:
                depthleft = depthleft + 1
                return depthleft
            else:
                return 1  # return it

    def count_leafs(self):  # count number of leaf
        A = None  # right
        B = None  # left
        if self.right is None and self.left is None:
            return 1  # if we are in leaf we return 1
        else:  # if not we get value in right and left
            if self.right is not None:
                A = self.right.count_leafs()
            if self.left is not None:  #
                B = self.left.count_leafs()
            if A is not None and B is not None:
                C = A + B
                return C  # return it
            elif A is not None:
                return A  # return it
            elif B is not None:
                return B  # return it

# We do a left-to-right in-order traversal of the tree
# to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        A = None
        B = None
        lst = [(self.key, self.value)]
        if self.left is not None:
            A = self.left.as_list(lst)
        if self.right is not None:
            B = self.right.as_list(lst)
        if A is not None and B is not None:
            lst = A + lst + B
        elif A is not None:
            lst = A + lst
        elif B is not None:
            lst = lst + B
        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)

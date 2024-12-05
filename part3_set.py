from dataclasses import dataclass
from typing import Any
from typing import List


@dataclass
class Node:  # normal bst class
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key):  # thus function add the word to the bst

        if self.key == key:  # if the words are the same
            self.value += 1  # add 1 to value
            return

        if self.key <= key:  # choose if we go right or left
            if self.left is None:  # if left is None
                self.left = Node(key, 1, None, None)  # add the word
                return
            self.left.put(key)  # if left is not none we enter in it
            return

        else:  # we go to right
            if self.right is None:  # check if right is None
                self.right = Node(key, 1, None, None)  # add the word
                return
            self.right.put(key)  # if right is not none we enetr in it
            return

    def as_list(self, lst):  # creat list from bst
        A = None  # creat A and B
        B = None
        lst = [(self.key, self.value)]  # get the key and value in a list
        if self.left is not None:  # if left is not None we enter in it
            A = self.left.as_list(lst)  # A is the list of list in left bucket
        if self.right is not None:  # if right is not None
            B = self.right.as_list(lst)  # B is the list of list in right
        if A is not None and B is not None:
            lst = A + lst + B
        elif A is not None:
            lst = A + lst
        elif B is not None:
            lst = lst + B
        return lst

    def count(self):  # count the number tree node
        A = None  # A for right
        B = None  # B for left
        count = 1  # we are in a node so count = 1
        if self.right is not None:  # take number of node in right and left
            A = self.right.count()
        if self.left is not None:
            B = self.left.count()
        if A is not None and B is not None:  # add them to count
            count = count + A + B
        elif A is not None:
            count = count + A
        elif B is not None:
            count = count + B
        return count

    def max_depth(self):  # get the max depth in the bst
        depthright = None  # depth in right and left
        depthleft = None
        if self.right is not None:  # enter in right or left if not None
            depthright = self.right.max_depth()
        if self.left is not None:
            depthleft = self.left.max_depth()
        if self.right is not None and self.left is not None:
            if depthright >= depthleft:  # get the higher depth and return it
                depthright = depthright + 1  # add 1 because we are in a node
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
                return 1  # if we are at max

    def count_leafs(self):  # count number of leaf
        A = None  # A for right
        B = None  # B for left
        if self.right is None and self.left is None:
            return 1  # if we are in a leaf, we return 1
        else:  # if not then we take the number of leaf in right and left
            if self.right is not None:
                A = self.right.count_leafs()
            if self.left is not None:
                B = self.left.count_leafs()
            if A is not None and B is not None:
                C = A + B
                return C
            elif A is not None:
                return A
            elif B is not None:
                return B


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hashword = ""
        for i in word:  # get each letter
            hashword = hashword + str(ord(i))  # add as a str (1 + 2 = 12)
        hashword = int(hashword)  # convert into int
        for i in word:  # get each letter
            hashword = hashword + ord(i)  # add as int
        return hashword  # return with mod

    # Doubles size of bucket list
    def rehash(self):
        savebuckets = [word for sublist in self.buckets for word in sublist]
        self.size = 0
        self.buckets = [[] for i in range(len(self.buckets)*2)]
        for word in savebuckets:
            self.add(word)

    # Adds a word to set if not already added
    def add(self, word):
        hash = self.get_hash(word) % len(self.buckets)  # get hash value
        if self.size < len(self.buckets):  # check if we need to rehash
            if self.buckets[hash] == []:  # if list is empty
                self.buckets[hash].append(word)  # add the word
                self.size = self.size + 1  # add 1 to size
            else:  # if not we check if the word is not already in the list
                for i in self.buckets[hash]:
                    if i == word:  # if already in the list
                        return
                self.buckets[hash].append(word)
                self.size = self.size + 1
        else:  # if need to reash
            self.rehash()  # reash
            self.add(word)  # add the word

    # Returns current number of elements in set
    def get_size(self):
        return self.size

# get the max bucket size
    def max_bucket_size(self):
        max = 0  # creat max
        for list in self.buckets:  # check each bucket
            if max < len(list):  # compare actual and bigger
                max = len(list)  # if bigger then replace by the bigger
        return max

    def bucket_list_size(self):
        return len(self.buckets)

    def zero_bucket_ratio(self):  # calculate ratio zero
        numberofempty = 0
        for list in self.buckets:
            if list == []:  # we count the number of empty buck
                numberofempty = numberofempty + 1
        ratio = numberofempty/len(self.buckets)  # calculate the ratio
        return ratio


@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key)

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

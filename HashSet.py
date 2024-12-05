from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):  # initialisation
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hashword = 0  # creat hashword
        for i in word:  # for take each letter
            hashword = hashword + ord(i)  # add ascii value of the word
        return hashword

    # Doubles size of bucket list
    def rehash(self):
        savebuckets = self.buckets  # save the actual bucket
        self.buckets = [[] for i in range(len(self.buckets)*2)]  # double buck
        self.size = 0  # reset the size
        for list in savebuckets:  # take each saved bucket
            for word in list:  # take each word
                self.add(word)  # add to the new buckets

    # Adds a word to set if not already added
    def add(self, word):
        hash = self.get_hash(word) % len(self.buckets)  # get hash value
        if self.size < len(self.buckets):  # check if we need to rehash
            if self.buckets[hash] == []:  # if bucket is empty
                self.buckets[hash].append(word)  # we add the wordto the buck
                self.size = self.size + 1   # size increases by one after word
            else:
                z = 0  # when the list is not empty
                for i in self.buckets[hash]:
                    if i == word:  # we verify words
                        z = 1   # if its repeated it doesn't add it
                if z == 0:  # adds
                    self.buckets[hash].append(word)  # word appends to the list
                    self.size = self.size + 1
        else:
            self.rehash()
            self.add(word)

    # Returns a string representation of the set content
    def to_string(self):
        string = "{ "  # define the string
        for list in self.buckets:
            for word in list:  # for every word in the list
                if word != []:  # if word is not empty
                    string = string + word + " "  # we sum them
        string = string + "}"  # close string
        return string

    # Returns current number of elements in set
    def get_size(self):
        return self.size  # gives the size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        z = 0
        for list in self.buckets:  # to check
            for wordinlist in list:  # if the wordinlist is a word
                if wordinlist == word:
                    z = 1  # it´s value is 1
        if z == 1:  # if i'ts one it returns the word else false
            return True
        else:
            return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)  # returns the number of  elements

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        x = 0
        for list in self.buckets:
            z = 0
            for wordinlist in list:
                if wordinlist == word:  # checks again if it's a word
                    del self.buckets[x][z]
                    self.size = self.size - 1   # rest the size to remove
                z = z + 1
            x = x + 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max = 0
        for list in self.buckets:  # the list
            if max < len(list):   # if maxx is less than the len of list
                max = len(list)   # value of max is now the value of the list
        return max

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        numberofempty = 0
        for list in self.buckets:
            if list == []:  # if list is empty
                numberofempty = numberofempty + 1   # we add one to the counter
        ratio = numberofempty/len(self.buckets)  # divide numberofempty by len
        return ratio

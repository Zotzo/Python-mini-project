import part3_set as part3


# this function will calculate the number of unique words
def unique(filename):
    with open(filename, "r", encoding="utf-8") as f:  # open the text
        listoftext = f.read().split()  # create a list
    words = part3.HashSet()  # creat a set
    words.init()  # we initial it
    for word in listoftext:  # for each word in list
        words.add(word)  # we add to the hash set
    print("In this file, their is :", words.get_size(), "unique words")
    print("size of list of bucket:", words.bucket_list_size())
    print("max bucket size :", words.max_bucket_size())
    print("empty bucket ratio :", words.zero_bucket_ratio())


# This function will calculate the top 10 mostes used words
def top10(filename):
    with open(filename, "r", encoding="utf-8") as f:  # open file
        listoftext = f.read().split()  # creat list with splite word
    listoftext2 = [word for word in listoftext if len(word) > 4]
    words = part3.BstMap()  # creat a class set bst
    for word in listoftext2:  # each word in the list
        words.put(word, 1)  # add word to the list
    wordlst = words.as_list()  # get a list from the bst
    wordlst.sort(key=lambda a: a[1], reverse=True)  # sort the list
    ran = wordlst[0:10]  # get the top 10
    list = []  # creat empty list
    print("the top ten most used word in the text is :")
    for i in ran:  # add the top ten to a list
        list.append(i)
    print(list)  # print the list
    print("Number of leafs:", words.count_leafs())
    print("Max depth :", words.max_depth())
    print("Number of tree node", words.size())


filename1 = "output_file_life_of_brian.txt"
filename2 = "output_swe_news.txt"

unique(filename1)
top10(filename1)
print("---------------------------------------------")
unique(filename2)
top10(filename2)

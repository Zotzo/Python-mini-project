def creatset(textname):  # create a function to create the set
    with open(textname, "r", encoding="utf-8") as f:  # open the text
        listoftext = f.read().split()  # read the file and split
    setoftext = set(listoftext)  # create a set from the list
    print("In", textname, "their is :", len(setoftext), "unique words.")
    workingindict(listoftext, setoftext)  # calling function for top 10


def workingindict(list, set):
    emplylist = [0]  # a list for the dico
    emplylist = emplylist * len(set)
    n_dico = dict(zip(set, emplylist))  # now we have our dico
    for j in list:
        if len(j) > 4:  # words with bigger lenght than 4
            n_dico[j] = n_dico[j] + 1
    get_top10(n_dico)  # calling a function


def get_top10(dict):
    print("the top ten most used word in the text is :")
    max_valuelist = []
    for x in range(10):
        max_value = max(dict, key=dict.get)  # we get the biggest key value
        max_valuelist.append(max_value)  # we append to the empty list
        max_valuelist.append(dict[max_value])
        dict[max_value] = 0  # we turn it to zero to get other big words
    print(max_valuelist)


file1 = "output_swe_news.txt"
file2 = "output_file_life_of_brian.txt"
creatset(file1)
print("-------------------------------------------")
creatset(file2)

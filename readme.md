************************

# Mini-project report 
Members: Denis Devlet and Iker Garcia Martinez   
Program: Software technology and Network security   
Course: 1DV501/1DT901  
Date of submission: 2022-11-06

## Introduction  

The program ``"introduction to programming"``, is the first course of Software technology and Network security, as the name says it is for many student the first time they meet the concept of programming. The mini project is the conclusion of this introduction in wich the student will concentrate his new knowledge in 3 programs , 3 tasks : 

 
- **number 1** : Counting the number of unique words by making use of set class, and  using the text output files from the previous assignment 3 exercises. As of the second part we will be using python’s dictionary class to produce a top 10 list of the most commonly used words in each file but only those having a length larger than four  and also print the frequency in which they appear. 

- **number 2** : In this exercise we must make use of the two skeletons we are provided, one for Hash sets and the other is a BST map, since we are tasked with implementing a set based on the before mentioned hash and BST, we are also provided with two output txt files which showcase the desired result after meddling and tuning the map and hash, as well with the main files that run our processes  

- **number 3** : This exercise is almost similar to the first one, we start by counting unique words from the same text files but this time we need to make use of hash sets in order to do it since we are forbidden from using sets as in the first one, then as for our top 10, instead of using dictionaries we must make use of Bst map as we are also forbidden from using dictionary classes. Where this exercise separates itself from the first one is what is next, just like in the bst and hash main python files we were provided, we need to provide the bucket list size, the max bucket size and the zero bucket ratio after all words have been added from the text files, next we are asked to provide the number of tree nodes, max depth and leaf count of the BST when all words have been added both key and value. 

The student is facing this probleme with a partener wich will introduce him to the project working in group as it is done in big compagnies. 

## Part 1: Count unique words 1

**The corresponding files are : exercice1.py**

This exercice , as said previoucly, have to **return the number of unique words** and the ``top 10 lists of used word which has a lenght more than 4`` from 2 files : output_file_life_of_brian.txt and output_swe_news.txt wich have ``12607 words`` for life of brian and ``14972459 words`` for swe_news.

### **Unique words**

We have, as asked by the examinator, to make use of the **set** here. 

The main objective is to return the number of unique words. So for we ``open the file`` given, ``splite the text`` so that we get a list of all the words, ``convert this list into a set`` wich will have only unique words (as they cannot be 2 same words in a set). Finnaly we just have to ``print the lenght of the set``. 

The **result** for the 2 files are :

| life_of_brian   | swe_news          |
|:---------------:|:-----------------:|
|2043 unique words|417512 unique words|

### **Top 10**

We have, as asked by the examinator, to make use of the **Dictionnary** here.

The main objective is to **return a top 10 of the most used words wich lenght is bigger than 4**. For this we ``take the list of all the words and the set of unique words created in the program getting the unique words``. For creating the dictionary we ``generat a list full of 0`` that has the same lenght as the set. We ``fuse these 2 lists/set`` creating a dictionnary.

We ``compare then each words`` from the list of all words ``with the dict`` :

- We ``take a word from the list`` : ``if`` his lenght is ``less or equale`` than 4 we return
- ``If`` the word is ``bigger than 4``: we call the word in the dict and ``add 1 to his value``

The result of this opperation is an dictionary with all words and the number of time they are repeated in the file. For getting the top 10 of it we ``get the word with the biggest key``, and ``print it``. After that we ``replace his key to 0`` so that the next time we get the second largest ect... we ``repeat it ten time`` for getting the top ten.

The **result** is :

| life_of_brian   | swe_news          |
|:---------------:|:-----------------:|
|brian / 368|säger / 47494|
|crowd / 161|under / 44969|
|centurion / 121|kommer / 42122|
|mother / 104|efter / 36472|
|right / 99|eller / 30834|
|crucifixion / 78|också / 30060|
|pilate / 68|andra / 27075|
|pontius / 64|finns / 26887|
|don't / 59|sedan / 24833|
|rogers / 52|skulle / 23469|

## Part 2: Implementing data structures

**The corresponding files are : HashSet.py, hash_main.py, BstMap.py, bst_main.py**

The part 2, as said before, is composed of 4 files : 2 skelton and program. The main objective is to create a hash set and a binary search tree in the 2 skelton so that the 2 program function, with additional function wich give information about how well the program performe ( zero ratio bucket/max buckets lenght/ number of leaf/ number of branch).

### **Hash Set**

The hash set is a set containing 2 objects : 

- a list of list(buckets)
- a size wich is the number of word in the buckets

The concepte of it is a ``way to store data`` in a efficient way : 

- Each data (in our case a word) has a ``hash value`` that is **unique** to him, this value will help us find the place we are going to store ( in wich buckets), ``if`` the number of word is ``bigger`` than the number of buckets, we have to duble the number of buckets and replace each word in the new buckets. This set give us the possibility to get the word we need by a very fast way with only the hash value of it.

The ``main function`` we need for the hash set is the function that will ``add`` a word to the buckets :

- The function **get_hash** will compute a ``hash value`` to a given word, we will here just add the ``ascii value`` of each letter of the word together.

- The **rehash** function will ``double the number of buckets`` by ``saving`` all the words in the existing buckets, ``reset`` the buckets by making it equale to 2 times the number of buckets before, and finnaly re add all the saved wordsto the buckets

- The function **ADD** is a function that will ``add a word in the buckets`` if he is not already added, for this we need in the first step the ``hash value`` of the word : we use the function called ``get_hash``, after getting the hash value we ``verify if the number of word added is not equale to the number of buckets``, if it is we call the ``rehash`` function, if it's not, we find the bucket needed by computing the ``hash value % number of buckets``, then we enter in the bucket, if it is empty we add the word and add 1 to the size, if not then we verify if the word is not already in the buckets, if it is not we add the word and 1 to the size. 

The sorting result of the ``hash_main`` are prety similare to what is expected, ``still there are some difference``, the bigest one is the ``Zero Bucket ratio``n and the ``order of the word`` in the buckets, this is due to ``the way of calculating the hash function`` on wich depend the placement of the words, better the get_hash function is, lower the zero ratio is, and of cours getting this value is far more intressting after before a rehash so that we can see if the words are nicely placed or not ( if we do just after a rehash, their will be minimum half the buckets empty as after the rehash 2 *number of word = number of buckets)

### **Binary Search Tree**

The binery search tree is a ``way of storing data`` with an logic order, with 4 object :

- The key
- The value
- Right
- Left

The concepte is that we have a ``Node`` wich store a data and 2 other node that are similare, one is the ``righ``t node and one is the ``left`` Node, and a way choosen to class the value wich give a way to put a new value to the right or to the left. 

We need, for this set some function, 1 for adding word to the BST and 1 for going threw the bst :

- The function ``put`` will add a word to the bst or modify it's value if he is already in it by ``multiple step of condition`` and ``recursive call`` : 
    * ``if`` the word we want to add is **equale** to the actual node, we **replace** the value of the **actual node** by the value of the word we want to add
    * ``elif`` we choose by the **alphabetic** order if we have to go right or left (we just **compaire** the key of the actual node and the key of the word in the way you want to sort your tree)
    * after choosing in wich way we go, we ``verify`` if this way if empty or not, if it is we replace this empty node by our word, if not we enter inite by calling the function put itself

- The function max_depth is build in a way that will be used for all over function that work in the bst, this build is simple :
    * for getting the max depth we ``verify`` if our ``right node and left node`` are ``None or not``
    * If the right and the left are None, we ``return 1``
    * If only one of them is none, we enter in the one that is not None by calling the function itself ``(recursive)`` in this direction, the value that this recursive call will return will be return but with an addition of 1. 
    * If the 2 are not None, we enter in the 2 by a recursive call, and ``compare`` the 2 value returned by the recursive function, we pick the ``biggest one and add to it one``. This new value will after this be return.

The main concepte behind the BST is as we can see the ``recursive call``. But as we can understand the more our bst is depth, the more the function will call itself, and will be more and more slow, this is why the ideal bst is a bst that has the minimal depth.
Their is no difference between the output of the BST program and the wanted output given in the file.

## Part 3: Count unique words 2

**The corresponding files are : exercice3.py and part3_set.py**

The ``Part 3`` is the same as the part 1, but ``instead`` of using a dictionary and a set, we have to use our own 2 set : 
- The ``hash`` set for the counting the unique word
- The ``bst`` for the top 10

### **Unique words with the hashset**

The hash set for the part 3 is ``not the same`` as in the part, it has been improved, and optimized for processing ``faster``,for getting the numnber of unique word we basicaly add each word from the file given in a hashset, then print the size of it.

Why ``changing`` the hash set ?

- The part 3 is processing far more word than in the part 3, because of it the hash set needed to be optimise by deleting some part not needed so that the program could compute faster.

- The ``result`` given by the part 3 were not as good as we want : With the ``HashSet.py``, swe_news has a maximum buckets of 600 wich is ``not`` wanted, because of it the hashing has been changed.

``Modification`` made :

- The hash set is now adding each ascii value of each letter from the word in a form of a ``str`` ( **such as "1" + "2" = "12"**), after getting this value we add again each ascii value of each letter in a float from ( normal form such as 1 + 2 = 3). This hash value is far better than the hash value of the part 2.

**Result** :

- Life of Brian : 
    * In this file, their is : 2043 unique words
    * size of list of bucket: 2048
    * max bucket size : 5
    * empty bucket ratio : 0.3720703125

- Swe_news :
    * In this file, their is : 417512 unique words
    * size of list of bucket: 524288
    * max bucket size : 13
    * empty bucket ratio : 0.46425628662109375

A ``perfect`` hashing function would give us a zero bucket ration of 0 and a max bucket of 1 so that each word has his own bucket. Here we can see that we get arround 50%, still this value is not as interresting, if we wanted to get a better idea of the hash function we should get the ratio just before a rehash so that ``the number of word = number of bucket``
Overall this function could be improved by using an other way of getting a hash value and placing the word in the buckets.

### **Top 10 with the bst**

For the top 10 this time we used **bst implementation**:

- We use the **put** function to add each words from the text that are bigger than 4 (for not processing words we don't need to) to the bst, This function was simplyfied in the part 3 skelton for running **fasted** than in the part 3 and instead of changing the value we just add 1 to the value when the words are already in the bst.

- We use the **as_list** for creating a list from the bst with the number.

After getting a list of list with all unique words and the number of time they are repeated, we ``sort`` them, and get the 10 first.

Result : 

- Life of brian :
    * [('brian', 368), ('crowd', 161), ('centurion', 121), ('mother', 104), ('right', 99), ('crucifixion', 78), ('pilate', 68),('pontius', 64), ("don't", 59), ('rogers', 52)]
    * Number of leafs: 469
    * Max depth : 24
    * Number of tree node 1442

- Swe_News:
    * [('säger', 47494), ('under', 44969), ('kommer', 42122), ('efter', 36472), ('eller', 30834), ('också', 30060), ('andra', 27075), ('finns', 26887), ('sedan', 24833), ('skulle', 23469)]
    * Number of leafs: 133042
    * Max depth : 50
    * Number of tree node 403175

The **perfect** result, should be, for the number of leafs around ``half`` the number of tree node, and the max depth should be the ``lowest`` possible, as we want a tree that proceed faster with ``minimal`` value. As we can see our program don't realy reach this goal. For reaching this program we could shuffle the list so that the order is the most random and the node are placed in the best way.

## Project conclusions and lessons learned

### technical issues  

The miniproject has been done in ``1 week``. The first exercice was not a probleme and was easy to creat. The second exercice took a bit more time as we had to ``assimilate`` the concepte of Hash set and Binery search tree. The third part took more time has we had to find a way to make the program run ``faster``, and for the hash set to find a way to hash so that we get a ``low zero ratio``.

Secondly, the working with gitlal has not been done correctely : we worked toghether in the same repertory so that we could not push together, resulting in an error and in the lost of the work done by one of us.

The main knowledge we get from this project is :

- The principe of the hashing, the bst
- The way of working with gitlab

If we had ``more time``, we would improve the BST function so that we get a good number of leaf and depth, and improve the Hash so that we get an even ``lower zero buckets ratio``. 

### Project issues 

The communication between us has been mainly done with ``Discord`` (a chat in internet) and ``in personne`` at the **library**. When we were together at library we devied the work and do it together, when we are at home we send us by message wich one do wich work. We communicate each day of the week. Unfortunately Iker was sick wich ``didn't`` allow him to work in the best condition.

Work done by ``each`` individual on each part :

- Part 1 : Iker and Denis in an equal way
- Part 2 : Denis
- Part 3 : program : Iker and Denis / skelton : Denis

Iker:
- ``mainly`` part 1 and the top 10 and unique words of part 3 

Denis: 
- All part 2 ,implementing some things to part 3 as well as created the skeleton for part 3 
- estimated hour of work in the week : Arround 23h

Main contributors to the written report: Mainly ``Denis`` and partialy ``Iker`` 

Some lessons I learned is that falling ill really impeded me from some things as i could not perform tasks in my best condition but thankfully my partner really helped out a lot. if i were faced to a similar project  I would try to organize better and try to see which parts i can contribute most as well as spending more time.-IK 

In fact i just think we should have started the mini project earlier, and we should have done a better repartition of the work as i did a lot more than Iker. - Denis
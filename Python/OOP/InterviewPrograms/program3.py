# Write a Python Program to convert two lists into a dictionary

# eg : 
# list1 = [Naina, Kimi, Sheena]
# list2 = [8543, 4567, 5646]

def list_to_dist():
    keys = [1, 2, 3]
    values = ["one", "two", "three"]
    result = dict(zip(keys, values))
    print(result)

list_to_dist()

def dict_to_tuple():
    x={1: 'one', 2: 'two', 3: 'three'}
    for i in x.items():
        print(i)
    
dict_to_tuple()


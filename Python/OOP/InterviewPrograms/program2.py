# Write a program to Count the frequency of words appearing in a string

# example - 
# Sheena loves eating apple and mango . Her sister also loves eating apple and mango .
# Sheena : 1, loves : 2, etc


def freq_words():
    str = input("Enter a string: ")
    li = str.split()
    d={}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)

freq_words()

# Write a python program to find out common letters between two strings
# ex - NAINA, REENE  o/p - N


def common_letters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    s1 = set(str1)
    s2 = set(str2)

    print(s1)
    print(s2)

    lst = s1 & s2 # & operator is used to find the common letter from set
    print(lst) 

common_letters()
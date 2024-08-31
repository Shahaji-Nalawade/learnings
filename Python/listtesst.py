# list1 = [1,2,4,5]
# list2 = [7,8,9]

# list3 = []


def assend_list(list1,list2):
    list3 = []
    
    return list3



def sort_list(list):
    for i in range(1,len(list)):
        for j in range(i+1, len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    print(list)


list1 = [1,4,3,7,9,6,2]
list2 = [13,10,11]
sort_list(list2)



{
    "name":"john",
    "age":"30"
}


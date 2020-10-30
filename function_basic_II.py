
def countdown (num):
    new_list = []
    for i in range(num, -1, -1):
        new_list.append(i)
    return new_list

print(countdown(10))

def print_and_return (list):
    print(list[0])
    return list[1]

print(print_and_return([6,9]))

def first_plus_length (list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second (list):
    if len(list) < 2:
        return false
    counter = 0
    new_list = []
    for i in range(0, len(list), 1):
        if list[i] > list[1]:
            new_list.append(list[i])
            counter += 1
    print(counter)
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))

def length_and_value (a,b):
    list=[]
    for i in range(0,a,1):
        list.append(b)
    return list

print(length_and_value(6,2))
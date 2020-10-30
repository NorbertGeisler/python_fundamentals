
# def biggie_size(list):
#     for i in range(0, len(list), 1):
#         if list[i]>0:
#             list[i]="big"
#     return list
# print(biggie_size([-1, 3, 5, -5]))


# def count_positives(list):
#     counter=0
#     for i in range(0, len(list), 1):
#         if i != len(list)-1:
#             if list[i]>0:
#                 counter+=1
#         else:
#             list[i]=counter
#     return list
# print(count_positives([1,6,-4,-2,-7,-2]))


# def sum_total(list):
#     sum=0
#     for i in list:
#         sum+=i
#     return sum
# print(sum_total([6,3,-2]))


# def averager(list):
#     sum=0
#     for i in list:
#         sum+=i
#     sum/=len(list)
#     return sum
# print(averager([1,2,3,4]))


# def length(list):
#     long=len(list)
#     return long
# print(length([]))


# def mini(list):
#     if len(list)>0:
#         smol=list[0]
#         for i in list:
#             if i<smol:
#                 smol=i
#         return smol
#     else:
#         return False
# print(mini([]))


# def lerge(list):
#     if len(list)>0:
#         birg=list[0]
#         for i in list:
#             if i>birg:
#                 birg=i
#         return birg
#     else:
#         return False
# print(lerge([37,2,1,-9]))


# def ultimate_analysis(list):
#     sum=0
#     birg=list[0]
#     smol=list[0]
#     length=len(list)
#     for i in list:
#         sum+=i
#     avg=sum/length
#     for i in list:
#         if i>birg:
#             birg=i
#         if i<smol:
#             smol=i
#     output={'sumTotal':sum, 'average':avg,'minimum':smol, 'maximum':birg, 'length':length}
#     return output
# print(ultimate_analysis([37,2,1,-9]))


def reverse_list(list):
    temp=0
    i=0
    for j in range(len(list)-1 ,0 , -1):
        if j>i:
            temp=list[j]
            list[j]=list[i]
            list[i]=temp
            i+=1
        else:
            return list
print(reverse_list([37,2,1,-9]))
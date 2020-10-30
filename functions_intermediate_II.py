# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# def updateValues (x, students, sports_directory, z):
#     x[1][0] = 15
#     students[0]["last_name"] = "Bryant"
#     sports_directory["soccer"][0] = "Andres"
#     z[0]["y"] = 30
#     return x, students, sports_directory, z
# print(updateValues(x, students, sports_directory, z))

students = [
        {'first_name' :  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary1(some_list):
#     for i in some_list:
#         newStr=""
#         for j in i:
#             newStr+= j
#             newStr+=" - "
#             newStr+=i[j]
#             newStr+=", "
#         print(newStr)
# iterateDictionary1(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterateDictionary2(key_name, some_list):
#     for i in some_list:
#         for j in i:
#             if j == key_name:
#                 print(i[j])
# iterateDictionary2("first_name",students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo (some_dict):
    print(some_dict["locations"][0])
    for i in some_dict:
        print(len(some_dict[i]), i.upper())
        for j in some_dict[i]:
            print(j)

print(printInfo(dojo))


# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
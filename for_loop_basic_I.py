for i in range(0, 151, 1):
    print(i)

for i in range(5, 1005, 5):
    print(i)

for i in range(1, 101, 1):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

sum = 0
for i in range(0, 500001, 1):
    if i % 2 != 0:
        sum += i
print(sum)

for i in range(2018, 0, -4):
    print(i)

low_num = 0
high_num = 69
mult = 3
for i in range(low_num, high_num, 1):
    if i % mult == 0:
        print(i)

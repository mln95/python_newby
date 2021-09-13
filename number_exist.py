list_number = [2,10,44,38,50,24,16,78,65,7,11,49,33]
list_number.sort()
print(list_number)

arr_value = len(list_number)-1

print('Check if the following number exists')
number = int(input())
found = False

while (arr_value >= 0 and found == False):
    if(list_number[arr_value] == number):
        print('Ok')
        print(f'The number is at the position {arr_value}')
        found = True
    else:
        arr_value = arr_value-1

if value_break == False:
    print('The number do not exist in the list')

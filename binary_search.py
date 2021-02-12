def binary_saerch(list, item):
    low=0
    high = len(list)-1
    count=0
    while low <= high:
        count = count+1
        mid = round((low+high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_saerch(my_list, 7))
print(binary_saerch(my_list, -1))
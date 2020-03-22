# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.
#
# Note: no empty arrays will be given.
#
# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3


def highest_rank(arr):
    numbers = set(arr)
    print(numbers)
    max = 0
    number_max = 0 
    for number in numbers:
        count = arr.count(number)
        if count > max:
            print(number, count, number_max)
            max = count
            number_max = number
        elif count == max:
            print(number, count, number_max)
            if number > number_max:
                number_max = number
    return number_max


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))
# reduce :  apply a function of two arguments cumulatively to the elements of a sequence, from left to right, to reduce the sequence to a single value.
# reduce : performs function on first two elements and repeats the process until 1 value remains
# reduce(function, iteratable)

from functools import reduce

def add(x,y):
    return x+y

list = [1,2,3,4,5]
sum = reduce(add,list)
print(sum)


letters = ["H","e","l","l","o"]
def combine_letters(accumulator, letter):
    return accumulator + letter

# word = reduce(combine_letters, letters)

word = reduce(lambda x, y : x + y, letters, "Hi, ")

print(word)



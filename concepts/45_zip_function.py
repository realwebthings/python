# zip(*iterables) : aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

print(type(users)) # <class 'zip'>

for i in users:
    print(i)
#prints
# ('Dude', 'p@ssword', '1/1/2021')
# ('Bro', 'abc123', '1/2/2021')
# ('Mister', 'guest', '1/3/2021')

# For dictionary, we need only 2 elements per tuple (key-value pairs)
dict_users = dict(zip(usernames, passwords))
print(dict_users)
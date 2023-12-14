#list comprehension
n = 5
squares_list = [k*k for k in range(1,n+1)]
print(squares_list)

#set comprehension
n = 5
squares_set = {k*k for k in range(1,n+1)}
print(squares_set)

#generator comprehension
n = 5
squares_generator = (k*k for k in range(1,n+1))
for square in squares_generator:
    print(square)

#dict comprehension
n = 5
square_dictionary = {k: k*k for k in range(1,n+1)}
print(square_dictionary)
print(square_dictionary[1])

#sum of first n squares, generator version
n = 50
total = sum(k*k for k in range(1,n+1))
print(total)
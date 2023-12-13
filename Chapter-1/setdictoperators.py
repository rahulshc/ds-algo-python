set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "banana", "mango"}

print( set1 ^ set2 )

d1 = { "k1" : 1, "k2" : 2}
d2 = { "k1" : 1, "k2" : [2]}

print(d1==d2)

#beta += foo is not same as beta = beta + foo
alpha = [1, 2, 3]
beta = alpha # an alias for alpha
beta += [4, 5] # extends the original list with two more elements
beta = beta + [6, 7] # reassigns beta to a new list [1, 2, 3, 4, 5, 6, 7]
print(alpha) # will be [1, 2, 3, 4, 5]
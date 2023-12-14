def gen_fibonacci():
    current = 0
    next = 1
    while True:
        yield current
        next_to_next = current + next
        current = next                  #next value becomes current for next iteration
        next = next_to_next

fib_generator = gen_fibonacci()

for _ in range(10):
    value = next(fib_generator)
    print(value)

#function to calculate all the factors of a number n
def calc_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

print(calc_factors(20))

#generator version of calc_factors
def gen_factors(n):
    for i in range(1,n+1):
        if n%i == 0:
            yield i

# gen_factors_ref = gen_factors(20)
# for _ in range(1,21):
#     print(next(gen_factors_ref))

#optimised version of gen_factors
def gen_factors_optimised(n):
    i = 1
    while i*i < n:
        if n%i == 0:
            yield i
            yield n//i
        i+=1
    if i*i == n:
        yield i

gen_factors_optimised_ref = gen_factors_optimised(20)
for _ in range(1,21):
    print(next(gen_factors_optimised_ref))
	
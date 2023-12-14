def compute_gpa(grades, points={ 'A+' :4.0,
'A' :4.0, 'A-' :3.67, 'B+' :3.33,
'B' :3.0, 'B-' :2.67, 'C+' :2.33, 'C' :2.0,
'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}):
    num_courses = 0
    total_points = 0
    grades = ['C+']      #does not mutate
    #grades.append('C+') #mutates the original parameter on line 15
    for g in grades:
        if g in points: # a recognizable grade
            num_courses += 1
            total_points += points[g]
    return total_points / num_courses

grades = ['A','B+']
print(compute_gpa(grades))
print(grades)

#example of where original mutation is intended
def scale(data, factor):
    for j in range(len(data)):
        data[j]*=factor

def foo(a, b=15, c=27):
    return a+b+c

foo(4, 12, 8) #valid
foo(4)        #valid
foo(8, 20)    #valid

#bar(a, b=15, c): invalid signature if a default parameter value is present for
#one parameter, it must be present for all further parameters.'''

print(max(-35, 20, key=abs)) #abs of 35 is more than 20
print(hash({"key": "val"}))
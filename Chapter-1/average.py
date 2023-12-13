print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
#map from letter grade to point value
points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':                 #empty line from user
        done = True
    elif grade not in points:
        print("Unknown grade '{0} being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0:
    print('Your GPA is {0:.3}'.format(total_points / num_courses))
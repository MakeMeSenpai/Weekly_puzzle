# first I create a locker object
class Locker:
    def __init__(self, state=False):
        # True == Open, False == Closed
        self.state = False

# next I'll create an array of lockers
lockers = []
for i in range(1000):
    lockers.append(Locker())

# then I'll make a func based on the pattern
students = 1000 # there are 1 thousand students
# each student has a task
for student in range(students): 
    # students must search threw every locker
    for i in range(len(lockers)): 
        """ i + 1 and student + 1 so that 0 is never divided
        i is the locker number and must be divided evenly 
        by the student. Taking modulo to get the correct locker """
        if  (i + 1) % (student + 1) == 0:
            # check if the locker is opened
            if lockers[i].state == True:
                # then close it
                lockers[i].state = False
            # or closed
            else:
                # then open it
                lockers[i].state = True

# finally we check for all opened lockers
opened_lockers = 0
for i in lockers:
    if i.state == True:
        opened_lockers += 1

print(f"The answer is {opened_lockers}")
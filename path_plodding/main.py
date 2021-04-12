# okay so the order goes...
order = ["start", "C", "F", "D", "A", "B", "C", "G", "start", "finish", "A", "E", "F", "finish"]

# but the issue is how can I code this...

# I'll start with creating pointers
class Node:
    def __init__(self, id, left, right, up, down):
        self.id = id
        self.left = left
        self.right = right
        self.up = up
        self.down = down

# then creating all our nodes
Start = Node('start', 'finish', 'G', 'C', None)
A = Node('A', 'finish', 'B', 'D', 'E')
B = Node('B', 'A', 'C', None, None)
C = Node('C', 'B', 'G', None, 'start')
D = Node('D', 'A', 'F', None, None)
E = Node('E', 'A', 'F', None, None)
F = Node('F', 'E', 'C', 'D', 'finish')
G = Node(None, None, 'C', 'start')
Finish = Node('finish', None, 'start', 'A', None)

# it's okay for a path to visit the same node more than once
# but what we need to check for is that we don't take the same
# street as before...

# lets give streets names, we can create them while making the path
# such as going from start to C, will equal startC/Cstart which then
# we can compar either a hash or try to use "is in" to figure out
# whether or not we have taken this path before. 
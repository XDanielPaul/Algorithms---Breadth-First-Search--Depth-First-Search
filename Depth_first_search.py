import time

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=bad-whitespace
# pylint: disable=trailing-whitespace
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=singleton-comparison

# This program simulates Depth-first search on following example
# Consider you have 2 White stones and 2 Black stones
# You have a wooden box with 5 holes so you can put these stones in any hole
# Result will be 4 holes filled with stones and 1 empty space
# The goal is to move the stones from "Starting position" to "Goal position" following these rules in given order:
# (Consider B = Black stone, W = White stone, E = empty space, >> = Example )
# Rule 1: You may jump over a stone with different color to the right to fill the empty space >> (B,W,E,W,B) -> (E,W,B,W,B)
# Rule 2: You may move one stone to the left on the empty space >> (B,E,W,B,W) -> (B,W,E,B,W)
# Rule 3: You may move one stone to the right on the empty space >> (B,E,W,B,W) -> (E,B,W,B,W)
# Rule 4: You may jump over a stone with different color to the left to fill the empty space >> (B,W,E,W,B) -> (B,W,B,W,E) 

# Represents Black stone
class Black:
    def __repr__(self):
        return "BLACK"

# Represents white stone
class White:
    def __repr__(self):
        return "WHITE"

# Represents empty space
class Empty:
    def __repr__(self):
        return "EMPTY"
        
# Represents BFS class
class BFS:

    # Initializing open = list with nodes to expand, count = number in order of nodes, goal = required position to reach
    def __init__(self, start, goal):
        self.open = [] 
        self.count = 1
        self.open.append(start)
        self.closed = []
        self.goal = goal
        self.iterate()

    # Increments variable that gives order to node
    def count_up(self):
        self.count += 1
        return self.count

    # Iterates over Open stack
    def iterate(self):
        while(self.found() != True):
            # Open stack is empty and result has not been found
            if(len(self.open) == 0):
                print("Open is empty, goal was not found")
                return
            self.use_rules()
        
        # Adding goal node to the closed stack
        self.closed.append(self.open[-1])
        self.open.pop()
        print("GOAL: ", self.goal)
        print("OPEN: " , self.open)
        print("CLOSED: " , self.closed)
        # Creating and printing path
        self.find_and_print_path()

    # Creates path from goal node to the start node by comparing parent (5th element of list) with child (6th element of list)
    def find_and_print_path(self):
        # Reverses list (Starting from goal node)
        self.closed.reverse()
        root = self.closed[0]
        self.closed.pop(0)
        path = []
        path.append(root) 
        # Checks whether the current node in Closed is "Parent" of a "Child". If yes, then the node is appended to the path list, else the node is popped from Closed
        while(self.closed[0][5] != 0):
            if(root[5] == self.closed[0][6]):
                root = self.closed[0]
                path.append(root)
            else:
                self.closed.pop(0)
        # Appending first node
        path.append(self.closed[0])
        # Reversing list to print it from the start to goal
        path.reverse()
        print("Path: " , path)

    # Checks if created node is in Open or Close stack
    def check(self, sequence):
        isInOpen = False
        isInClosed = False
        for seq in self.open:
            cnt = 0
            for i in range(0,len(sequence)-2):
                if(type(seq[i]) is type(sequence[i])):
                    cnt += 1
            if (cnt == len(sequence)-2):
                isInOpen = True

        for seq in self.closed:
            cnt = 0
            for i in range(0,len(sequence)-2):
                if(type(seq[i]) is type(sequence[i])):
                    cnt += 1
            if (cnt == len(sequence)-2):
                isInClosed = True

        if (isInOpen == False and isInClosed == False):
            self.open.append(sequence)
        else:
            self.count -= 1
            
    # Creates new sequences (nodes) by using given rules
    def use_rules(self):

        index = 0
        # State = just assigning this to new variable, cause self.open[0] would be untidy/disarranged
        state = self.open[-1]
        self.closed.append(self.open[-1])
        self.open.pop()
        # Assigning = just assigning this to new variable, cause state[5] + 1 would be untidy/disarranged
        child = state[5] + 1
        
        # Checks on which index is "Empty" space
        for index in range(0,len(state)):
            if(type(state[index]) is type(Empty())):
                break
        
        # Appends new sequences created by rules to Open stack if it is not contained Closed or Open already

        if(index == 0):
            self.check([state[1],Empty(),state[2],state[3],state[4],child, self.count_up()])

        if(index == 1):
            self.check([state[0],state[2],Empty(),state[3],state[4],child, self.count_up()])
            self.check([Empty(),state[0],state[2],state[3],state[4],child, self.count_up()])
             
            if(type(state[2]) == type(Black()) and type(state[3]) == type(White())):
                self.check([state[0],White(),Black(),Empty(),state[4],child, self.count_up()])
                 
            if(type(state[2]) == type(White()) and type(state[3]) == type(Black())):
                self.check([state[0],Black(),White(),Empty(),state[4],child, self.count_up()])
                 

        if(index == 2):
            if(type(state[0]) == type(Black()) and type(state[1]) == type(White())):
                self.check([Empty(),White(),Black(),state[3],state[4],child, self.count_up()])
                 
            if(type(state[0]) == type(White()) and type(state[1]) == type(Black())):
                self.check([Empty(),Black(),White(),state[3],state[4],child, self.count_up()])
                 
            self.check([state[0],state[1],state[3],Empty(),state[4],child, self.count_up()])   
            self.check([state[0],Empty(),state[1],state[3],state[4],child, self.count_up()])
             
            if(type(state[3]) == type(Black()) and type(state[4]) == type(White())):
                self.check([state[0],state[1],White(),Black(),Empty(),child, self.count_up()])
                 
            if(type(state[3]) == type(White()) and type(state[4]) == type(Black())):
                self.check([state[0],state[1],Black(),White(),Empty(),child, self.count_up()])
                 

        if(index == 3):
            if(type(state[1]) == type(Black()) and type(state[2]) == type(White())):
                self.check([state[0],Empty(),White(),Black(),state[4],child, self.count_up()])
                 
            if(type(state[1]) == type(White()) and type(state[2]) == type(Black())):
                self.check([state[0],Empty(),Black(),White(),state[4],child, self.count_up()])
                 
            self.check([state[0],state[1],state[2],state[4],Empty(),child, self.count_up()])
            self.check([state[0],state[1],Empty(),state[2],state[4],child, self.count_up()])
             

        if(index == 4):
            self.check([state[0],state[1],state[2],Empty(),state[3],child, self.count_up()])

    # Checks if node to be expanded is the goal node
    def found(self):
        i = 0
        for i in range(0,len(self.open[-1])-2):
            if(type(self.open[-1][i]) is not type(self.goal[i])):
                return False          
        return True


if __name__ == '__main__':
    start_time = time.time()
    # Starting position = You can change by your liking
    starting_pos = [Empty(), Black(), White(), White(), Black(), 0, 1]
    # Goal position = You can change by your liking
    goal_pos = [Black(), White(), Black(), White(), Empty()]
    root = BFS(starting_pos, goal_pos)
    print("--- %s seconds ---" % (time.time() - start_time))
    
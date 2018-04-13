import numpy as np
import argparse

class node():
    def __init__(self,matrix,father):
        self.matrix = matrix
        self.father = father

def is_solution(q_matrix):
    print(q_matrix)
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", "-str", type=str, required=True)
    parser.add_argument("--showstate", "-show", type=str, required=True)
    parser.add_argument("--sides", "-n", type=str, required=True)
    args = parser.parse_args()
    args.showstate = args.showstate.lower()
    args.strategy = args.strategy.lower()
    print("strategy   : "+args.strategy)
    print("show state : "+args.showstate)
    print("n sides    : "+args.sides)
    args.showstate.lower()
    if(args.showstate == 'yes' or args.showstate == 'y'):
        show = True
    else:
        show = False

    n = int(args.sides)
    root = node(np.array([[0 for x in range(n)] for y in range(n)]),
                None)
    print("root matrix:")
    print(root.matrix)
    board = np.array([[0 for x in range(n)] for y in range(n)])

    with open("board.txt") as f:
        row = 0
        for line in f:
            #print(line)
            line = line.replace('[','')
            line = line.replace(']','')
            line = line.replace('\n','')
            boxes = line.split(',')
            #print (boxes)
            column = 0
            for box in boxes:
                board[row][column] = int(box)
                #print(str(row)+" "+str(column))
                column = column + 1
            if(column == n): row = row + 1
    print("tablero a resolver:")
    print(board)

    #State list
    Q = [root]

    while(len(Q)):
        if(show): print("Largo de Q: "+str(len(Q)))

        q = Q.pop()
        print("current matrix")
        print(q.matrix)

        if(is_solution(q.matrix)):
            print("es solucion")
    

import numpy as np
import argparse

class node():
    def __init__(self,matrix,father):
        self.matrix = matrix
        self.father = father

    def generate_sons(self):
        sons_list = []
        for coords in np.argwhere(self.matrix == 0):
            son = self.matrix.copy()
            son[coords[0]] = -1                 # block horizontal
            son.transpose()[coords[1]] = -1     # block vertical
            shape = son.shape[0]
            for x in [-1, 1]:
                for y in [-1, 1]:
                    if coords[0]+x > -1 and coords[1]+y > -1:
                        try:
                            son[coords[0]+x][coords[1]+y] = -1 # block diagonals
                        except Exception as e:
                            pass
            son[coords[0]][coords[1]] = 1 # put tree
            sons_list.append(node(son,self))
        return sons_list

def is_solution(q_matrix,board, n):
    for x in q_matrix:
        count = len(np.argwhere(x == 1)) # count where's a tree /horizontal
        if count > 1:
            return False
    for x in q_matrix.transpose():
        count = len(np.argwhere(x == 1)) # count where's a tree /vertical
        if count > 1:
            return False
    for x in range(1, n+1):
        count = 0
        for y in np.argwhere(board == x):
            if q_matrix[y[0]][y[1]] == 1:
                count = count + 1
        if count > 1:
            return False
    if len(np.argwhere(q.matrix == 1)) != board.shape[0]:
        return False
    return True

def load_board(n):
    board = np.array([[0 for x in range(n)] for y in range(n)])
    with open("board.txt") as f:
        row = 0
        for line in f:
            line = line.replace('[','')
            line = line.replace(']','')
            line = line.replace('\n','')
            boxes = line.split(',')
            column = 0
            for box in boxes:
                board[row][column] = int(box)
                column = column + 1
            if(column == n): row = row + 1
    return board

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
    if(args.showstate == 'yes' or args.showstate == 'y'):
        show = True
    else:
        show = False

    if(args.strategy not in ['bfs','dfs']):
        exit()
    n = int(args.sides)
    root = node(np.array([[0 for x in range(n)] for y in range(n)]),
                None)
    board = load_board(n)
    print("tablero a resolver:")
    print(board)    

    #State list
    Q = [root]

    # check for shape
    if(not(board.shape == root.matrix.shape) and root.matrix.shape[0] == n):
        print("El tablero y la dimension solicitada no corresponden.")
        exit()

    while(len(Q)):
        if(show): print("Largo de Q: "+str(len(Q)))

        q = Q.pop()

        if(is_solution(q.matrix, board,n)):
            print("Es solucion: ")
            matrix_return = q.matrix.copy()
            for coords in np.argwhere(q.matrix == -1):
                matrix_return[coords[0],coords[1]] = 0
            print(matrix_return)
            exit()
        
        sons = q.generate_sons()
        sons.reverse() # swap childrens place

        if(args.strategy == 'dfs'):
            # deep search strategy
            Q = Q + sons
        elif(args.strategy == 'bfs'):
            # level search strategy
            Q = sons + Q
    print("No hay solucion.")
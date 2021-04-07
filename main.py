import time
import os
import maze
import solver
import walker

class game:
    def __init__(self):
        print("Select the item you want:")
        print("1 - generate a maze")
        print("2 - load an existing maze")
        s = int(input())
        if s == 1:
            self.generate()
        else:
            self.loadmaze()
        self.menu()

    def generate(self):
        os.system("clear")
        print("Enter size of maze and type of generation(0 - dfs, 1 - Kruskal)")
        n, m, type = map(int, input().split())
        self.cur = maze.maze(n, m, type)
        print("Generation was successful")

    def loadmaze(self):
        os.system("clear")
        print("Enter name of file")
        name = input()
        try:
            in_file = open(name, 'r')
            first = True
            i = 0
            for line in in_file:
                if line[-1] == '\n':
                    line = line[:-1]
                if line[-1] == ' ':
                    line = line[:-1]
                if first:
                    n, m = map(int, line.split(" "))
                    first = False
                    self.cur = maze.maze(n, m, type)
                    continue
                self.cur.maze[i] = list(map(int, line.split(" ")))
                i += 1
            print("loading was successful")
            in_file.close()
        except:
            print("file is not found")
            exit(0)

    def print(self):
        os.system("clear")
        self.cur.print()

    def on_solver(self):
        os.system("clear")
        solver.solver(self.cur).print()
        self.off_solver()

    def off_solver(self):
        for i in range(self.cur.n):
            for j in range(self.cur.m):
                self.cur.maze[i][j] = min(self.cur.maze[i][j], 1)

    def save(self):
        os.system("clear")
        print("Enter name of file")
        name = input()
        out_file = open(name, 'w')
        out_file.write(str(self.cur.n) + ' ' + str(self.cur.m) + '\n')
        for i in range(self.cur.n):
            for j in range(self.cur.m):
                out_file.write(str(min(1, self.cur.maze[i][j])) + ' ')
            out_file.write('\n')
        out_file.close()
        print('maze was saved')

    def walk(self):
        os.system("clear")
        walker.walker(self.cur)


    def menu(self):
        print("Select the item you want:")
        print("1 - Generate a maze")
        print("2 - Load an existing maze")
        print("3 - Print current maze")
        print("4 - Solve maze")
        print("5 - Save current maze to file")
        print("6 - Try to solve with yourself")
        print("7 - Exit")
        s = int(input())
        if s == 1:
            self.generate()
        if s == 2:
            self.loadmaze()
        if s == 3:
            self.print()
        if s == 4:
            self.on_solver()
        if s == 5:
            self.save()
        if s == 6:
            self.walk()
        if s == 7:
            exit(0)
        self.menu()

session = game()
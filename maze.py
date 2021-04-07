import generator


class maze:
    def __init__(self, n, m, type):
        self.n = n
        self.m = m
        d = generator.generator(type, n, m)
        self.maze = d.maze
        self.start = d.start
        self.end = d.end

    def print(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.maze[i][j] == 2:
                    print("\033[42m  \033[0m", end='')
                    continue
                if self.maze[i][j]:
                    print("\033[47m  \033[0m", end='')
                if not self.maze[i][j]:
                    print("\033[40m  \033[0m", end='')
            print()

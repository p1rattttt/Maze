import maze

class solver(maze.maze):
    def __init__(self, maze):
        self.maze = maze.maze
        self.n = maze.n
        self.m = maze.m
        self.start = maze.start
        self.end = maze.end
        self.diff = [[-2, 0, -1, 0], [2, 0, 1, 0], [0, -2, 0, -1], [0, 2, 0, 1]]
        self.solve()

    def solve(self):
        pred = [[[-1, -1, -1, -1]] * self.m for i in range(self.n)]
        was = [[0] * self.m for i in range(self.n)]
        q = []
        q.append(self.start)
        was[self.start[0]][self.start[1]] = 1
        while len(q):
            t = q[-1]
            q.pop(len(q) - 1)
            for i in self.diff:
                ni = t[0] + i[0]
                nj = t[1] + i[1]
                if ni >= 0 and ni < self.n and nj >= 0 and nj < self.m and self.maze[ni][nj] and not was[ni][nj] and self.maze[ni - i[2]][nj - i[3]]:
                    q.append([ni, nj])
                    was[ni][nj] = 1
                    pred[ni][nj] = t + [ni - i[2], nj - i[3]]

        cur = self.end
        while cur[0] != -1:
            self.maze[cur[0]][cur[1]] = 2
            pr = pred[cur[0]][cur[1]]
            if pr[2] != -1:
                self.maze[pr[2]][pr[3]] = 2
            cur = pr[:2]

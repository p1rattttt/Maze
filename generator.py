import random


class generator:
    def gen(self, type):
        self.maze = [[0] * self.m for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if i % 2 != 0 and j % 2 != 0 and i < self.n - 1 and j < self.m - 1:
                    self.maze[i][j] = 1
                    self.all += 1
        if type == 0:
            self.dfs()
        if type == 1:
            self.kruskal()
        endx = 0
        endy = 0
        if self.n % 2 == 0:
            endx = self.n - 3
        else:
            endx = self.n - 2
        if self.m % 2 == 0:
            endy = self.m - 3
        else:
            endy = self.m - 2
        self.end = [endx, endy]

    def __init__(self, type, n, m):
        self.n = n
        self.m = m
        self.start = [1, 1]
        self.all = 0
        self.end = [1, 1]
        self.diff = [[-2, 0, -1, 0], [2, 0, 1, 0], [0, -2, 0, -1], [0, 2, 0, 1]]
        self.diffplus = [[2, 0], [0, 2]]
        self.gen(type)

    def kruskal(self):
        alledge = []
        pred = []
        for i in range(self.n):
            cur = []
            for j in range(self.m):
                cur.append([i, j])
            pred.append(cur)

        def getpred(cur):
            if pred[cur[0]][cur[1]] == cur:
                return cur
            pred[cur[0]][cur[1]] = getpred(pred[cur[0]][cur[1]])
            return pred[cur[0]][cur[1]]

        def merge(a, b):
            a = getpred(a)
            b = getpred(b)
            if a == b:
                return
            if random.randint(0, 1):
                pred[b[0]][b[1]] = a
            else:
                pred[a[0]][a[1]] = b

        for i in range(self.n):
            for j in range(self.m):
                for d in self.diffplus:
                    ni = i + d[0]
                    nj = j + d[1]
                    if ni >= 0 and ni < self.n and nj >= 0 and nj < self.m and self.maze[i][j] and self.maze[ni][nj]:
                        alledge.append([i, j, ni, nj])

        random.shuffle(alledge)

        for ind in range(len(alledge)):
            if getpred(alledge[ind][0:2]) == getpred(alledge[ind][2:]):
                continue
            merge(alledge[ind][0:2], alledge[ind][2:])
            if alledge[ind][0] + 2 == alledge[ind][2]:
                self.maze[alledge[ind][0] + 1][alledge[ind][1]] = 1
            else:
                self.maze[alledge[ind][0]][alledge[ind][1] + 1] = 1

    def dfs(self):
        self.was = [[0] * self.m for i in range(self.n)]

        def check():
            all = []
            for i in range(self.n):
                for j in range(self.m):
                    if not self.was[i][j] and self.maze[i][j]:
                        all.append([i, j])
            if len(all) == 0:
                return [-1, -1]
            return all[random.randint(0, len(all) - 1)]

        def near(x, y):
            all = []
            for i in self.diff:
                ni = x + i[0]
                nj = y + i[1]
                if ni >= 0 and ni < self.n and nj >= 0 and nj < self.m and not self.was[ni][nj] and self.maze[ni][nj]:
                    all.append([ni, nj])
            if len(all) == 0:
                return [-1, -1]
            cur = all[random.randint(0, len(all) - 1)]
            for i in self.diff:
                ni = x + i[0]
                nj = y + i[1]
                if ni == cur[0] and nj == cur[1]:
                    self.was[ni - i[2]][nj - i[3]] = 1
                    self.maze[ni - i[2]][nj - i[3]] = 1
                    break
            return cur

        start = [1, 1]
        cur = start
        stack = []
        while self.all:
            if not self.was[cur[0]][cur[1]]:
                self.all -= 1
            self.was[cur[0]][cur[1]] = 1
            get = near(cur[0], cur[1])
            if get[0] == -1:
                if len(stack) != 0:
                    cur = stack[-1]
                    stack.pop(len(stack) - 1)
                    continue
                cur = check()
                continue
            stack.append(cur)
            cur = get
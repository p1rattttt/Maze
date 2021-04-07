import maze
import sys
import keyboard
import time
import os

class walker(maze.maze):
    def __init__(self, curmaze):
        self.n = curmaze.n
        self.m = curmaze.m
        self.maze = curmaze.maze
        self.cur = curmaze.start
        self.end = curmaze.end
        self.maze[self.cur[0]][self.cur[1]] = 2
        self.game()

    def move(self, x, y):
        nw = self.cur.copy()
        nw[0] += x
        nw[1] += y
        if nw[0] >= 0 and nw[0] < self.n and nw[1] >= 0 and nw[1] < self.m and self.maze[nw[0]][nw[1]]:
            self.maze[self.cur[0]][self.cur[1]] = 1
            self.cur = nw
            self.maze[self.cur[0]][self.cur[1]] = 2

    def game(self):
        curtime = time.time()
        curtimetopress = time.time()
        os.system("clear")
        self.print()
        while True:
            if self.cur == self.end:
                break
            if time.time() - curtimetopress > 0.1:
                curtimetopress = time.time()
                if keyboard.is_pressed('w'):
                    self.move(-1, 0)

                if keyboard.is_pressed('s'):
                    self.move(1, 0)

                if keyboard.is_pressed('a'):
                    self.move(0, -1)

                if keyboard.is_pressed('d'):
                    self.move(0, 1)

            if time.time() - curtime > 0.1:
                curtime = time.time()
                os.system("clear")
                self.print()
        print("good job!!!")
        exit(0)
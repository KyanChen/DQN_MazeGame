import cv2
import numpy as np
import random
import time


class Env:
    def __init__(self):
        super(Env, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.migong = []
        self.x1, self.y1 = 0, 0
        self.end_game = 0
        self.display1 = None
        self.last_action = None

    # 建立虚拟环境
    def start_env(self):
        self.migong = [[1, 0, 0, 0, 0],
                       [0, 0, 0, 3, 0],
                       [0, 0, 0, 0, 0],
                       [0, 3, 0, 0, 0],
                       [0, 0, 0, 0, 2]]
        self.x1, self.y1 = 0, 0
        self.end_game = 0
        return self.migong

    def display(self):
        self.display1 = np.ones((300, 300, 3), dtype=np.uint8)
        self.display1 = np.array(np.where(self.display1 == 1, 255, 0), dtype=np.uint8)
        for i in range(5):
            cv2.line(self.display1, (i * 60, 0), (i * 60, 300), (0, 0, 0), 1)
            cv2.line(self.display1, (0, i * 60), (300, i * 60), (0, 0, 0), 1)
        for x in range(5):
            for y in range(5):
                if self.migong[y][x] == 1:
                    cv2.circle(self.display1, (x * 60 + 30, y * 60 + 30), 25, (255, 0, 0), -1)
                if self.migong[y][x] == 2:
                    cv2.circle(self.display1, (x * 60 + 30, y * 60 + 30), 25, (0, 255, 0), -1)
                if self.migong[y][x] == 3:
                    cv2.circle(self.display1, (x * 60 + 30, y * 60 + 30), 25, (0, 0, 255), -1)

        cv2.imshow('1', self.display1)
        cv2.waitKey(1)

    def step(self, action):
        r = 0
        # ['u'0, 'd'1, 'l'2, 'r'3]
        if (self.last_action, action) in [(0, 1), (1, 0), (2, 3), (3,2)]:
            r += -0.5
        if action == 0:
            if self.y1 == 0:
                r += -1
            else:
                self.migong[self.y1][self.x1] = 0
                self.migong[self.y1 - 1][self.x1] = 1
                self.y1 -= 1
                if self.y1 == 1 and self.x1 == 3:
                    self.end_game = 1
                    r += -1
                elif self.y1 == 3 and self.x1 == 1:
                    self.end_game = 1
                    r += -1
                elif self.y1 == 4 and self.x1 == 4:
                    self.end_game = 2
                    r += 5
        if action == 1:
            if self.y1 == 4:
                r += -1
            else:
                self.migong[self.y1][self.x1] = 0
                self.migong[self.y1 + 1][self.x1] = 1
                self.y1 += 1
                if self.y1 == 1 and self.x1 == 3:
                    self.end_game = 1
                    r += -1
                elif self.y1 == 3 and self.x1 == 1:
                    self.end_game = 1
                    r += -1
                elif self.y1 == 4 and self.x1 == 4:
                    self.end_game = 2
                    r += 5
        if action == 2:
            if self.x1 == 0:
                r += -1
            else:
                self.migong[self.y1][self.x1] = 0
                self.migong[self.y1][self.x1 - 1] = 1
                self.x1 -= 1
                if self.y1 == 1 and self.x1 == 3:
                    self.end_game = 1
                    r += -1
                elif self.y1 == 3 and self.x1 == 1:
                    self.end_game = 1
                    r += -1
                elif self.y1 == 4 and self.x1 == 4:
                    self.end_game = 2
                    r += 5
        if action == 3:
            if self.x1 == 4:
                r += -1
            else:
                self.migong[self.y1][self.x1] = 0
                self.migong[self.y1][self.x1 + 1] = 1
                self.x1 += 1
                if self.y1 == 1 and self.x1 == 3:
                    self.end_game = 1
                    r += -1
                elif self.y1 == 3 and self.x1 == 1:
                    self.end_game = 1
                    r += -1
                elif self.y1 == 4 and self.x1 == 4:
                    self.end_game = 2
                    r += 5
        # return self.migong
        return self.end_game, r, self.migong

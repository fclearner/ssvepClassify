import pygame
import sys
from win32api import GetSystemMetrics
from pygame.locals import *
import numpy as np
import time


class SImage():

    def __init__(self, predictionList):
        self.SR = [GetSystemMetrics(0), GetSystemMetrics(1)]
        self.size = width, height = self.SR[0], self.SR[1]
        # print(self.SR[0], self.SR[1])
        self.predictionList = predictionList
        self.text = ""

        # self.B = np.array([(1, 2), (3, 4)])

    def O_screen(self):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.size[0]/2.5, self.size[1]/6, self.size[0]/5, self.size[1]/5))  # up
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.size[0]/2.5, self.size[1]/6, self.size[0]/5, self.size[1]/5), 1)  # up
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.size[0]*1.6/2.5, self.size[1]/2.4, self.size[0]/5, self.size[1]/5))  # right
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.size[0]*1.6/2.5, self.size[1]/2.4, self.size[0]/5, self.size[1]/5), 1)  # right 
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.size[0]/2.5, self.size[1]*4/6, self.size[0]/5, self.size[1]/5))  # down
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.size[0]/2.5, self.size[1]*4/6, self.size[0]/5, self.size[1]/5), 1)  # down
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.size[0]/6, self.size[1]/2.4, self.size[0]/5, self.size[1]/5))  # left
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.size[0]/6, self.size[1]/2.4, self.size[0]/5, self.size[1]/5), 1)  # left
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.size[0]/2.4, self.size[1]/2.3, self.size[0]/6, self.size[1]/6))
        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.size[0]/2.4, self.size[1]/2.3, self.size[0]/6, self.size[1]/6), 2)

        font = pygame.font.SysFont('microsoft Yahei', 60)
        Button1 = font.render('A', False, (255, 255, 255))
        self.screen.blit(Button1, (self.size[0]/2.05, self.size[1]/4))

        Button2 = font.render('B', False, (255, 255, 255))
        self.screen.blit(Button2, (self.size[0]*1.72/2.35, self.size[1]/2))

        Button3 = font.render('C', False, (255, 255, 255))
        self.screen.blit(Button3, (self.size[0]/2.05, self.size[1] / 1.8 + self.size[1] / 5))

        Button4 = font.render('D', False, (255, 255, 255))
        self.screen.blit(Button4, (self.size[0]/3.95, self.size[1] / 2))
        pygame.display.update()

        fontText = pygame.font.SysFont('microsoft Yahei', 25)
        for i in range(int(len(self.text)/18)+1):
            textArea = fontText.render(self.text[i*18:18*(i+1)], False, (0, 0, 0))
            self.screen.blit(textArea, (self.size[0]/2.3, self.size[1]/2.2 + i*25))

    def move(self, k):
        self.O_screen()
        font = pygame.font.SysFont('microsoft Yahei', 60)
        if k == 1:
            pygame.draw.rect(self.screen, (190, 190, 190), pygame.Rect(self.size[0]/2.5, self.size[1]/6, self.size[0]/5, self.size[1]/5))
            Button1 = font.render('A', False, (255, 0, 0))
            self.screen.blit(Button1, (self.size[0]/2.05, self.size[1]/4))
            self.text = self.text + "A"
        elif k == 2:
            pygame.draw.rect(self.screen, (190, 190, 190), pygame.Rect(self.size[0]*1.6/2.5, self.size[1]/2.4, self.size[0]/5, self.size[1]/5))
            Button2 = font.render('B', False, (255, 0, 0))
            self.screen.blit(Button2, (self.size[0]*1.72/2.35, self.size[1]/2))
            self.text = self.text + "B"
        elif k == 3:
            pygame.draw.rect(self.screen, (190, 190, 190), pygame.Rect(self.size[0]/2.5, self.size[1]*4/6, self.size[0]/5, self.size[1]/5))
            Button3 = font.render('C', False, (255, 0, 0))
            self.screen.blit(Button3, (self.size[0]/2.05, self.size[1] / 1.8 + self.size[1] / 5))
            self.text = self.text + "C"
        elif k == 4:
            pygame.draw.rect(self.screen, (190, 190, 190), pygame.Rect(self.size[0]/6, self.size[1]/2.4, self.size[0]/5, self.size[1]/5))
            Button4 = font.render('D', False, (255, 0, 0))
            self.screen.blit(Button4, (self.size[0]/3.95, self.size[1] / 2))
            self.text = self.text + "D"
        else:
            pass
        fontText = pygame.font.SysFont('microsoft Yahei', 25)
        for i in range(int(len(self.text)/18)+1):
            textArea = fontText.render(self.text[i*18:18*(i+1)], False, (0, 0, 0))
            self.screen.blit(textArea, (self.size[0]/2.3, self.size[1]/2.2 + i*25))

        pygame.display.update()

    def popup(self, i, j):
        if self.B[i][j] == 1:
            pass
        elif self.B[i][j] == 2:
            pass
        elif self.B[i][j] == 3:
            pass
        elif self.B[i][j] == 4:
            pass

    def run(self):
        B = np.array([(1, 2), (3, 4)])

        pygame.init()
        self.screen = pygame.display.set_mode(self.size, FULLSCREEN, 32)
        self.O_screen()

        # ################################################ key control
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == QUIT:
        #             sys.exit()
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_ESCAPE:
        #                 sys.exit()
        #             else:
        #                 if event.key == pygame.K_DOWN:
        #                     self.move(3)
        #                 elif event.key == pygame.K_UP:
        #                     self.move(1)
        #                 elif event.key == pygame.K_LEFT:
        #                     self.move(4)
        #                 elif event.key == pygame.K_RIGHT:
        #                     self.move(2)
        #                 elif event.key == pygame.K_a:
        #                     pass
        #                 elif event.key == pygame.K_b:
        #                     pass
        #                 else:
        #                     pass
        # ################################################ key control
        # ################################################ EEG control
        count = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                else:
                    pass
            if count < len(self.predictionList):
                print(self.predictionList[count])
                if self.predictionList[count] == 0:
                    self.move(1)
                    time.sleep(0.5)
                elif self.predictionList[count] == 1:
                    self.move(2)
                    time.sleep(0.5)
                elif self.predictionList[count] == 2:
                    self.move(3)
                    time.sleep(0.5)
                elif self.predictionList[count] == 3:
                    self.move(4)
                    time.sleep(0.5)
                else:
                    pass

                count += 1
            else:
                pass


# si = SImage([0, 1, 2, 3])

# si.run()
from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time

#class structure
sense = SenseHat()
sense.clear()
def validate(b, d):
        if b == d:
            pass
        else:
            print "You lose"
            sense.clear()
            exit()
class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self.gaming = True
    
    def startGame(self):
        pygame.time.set_timer(USEREVENT +1, 800)
        x = 0
        y = 7
        coord_list = [ ]
        while self.gaming:
                sense.set_pixel(x, y, (0, 0, 255))
                time.sleep(.3)
                #sense.clear()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        sense.set_pixel(x, y, (0, 0, 255))
                        coord_list.append(x)
                        coord_list.append(y)
                        if len(coord_list) > 2:
                            #a = coord_list[len(coord_list)-1]
                            b = coord_list[len(coord_list)-2]
                            #c = coord_list[len(coord_list)-3]
                            d = coord_list[len(coord_list)-4]
                            validate(b, d) 
                        y = y-1
                        if y == -1:
                            print "You win"
                            self.gaming = False    
                    else:    
                        sense.set_pixel(x, y, (0, 0, 0))
                    x +=1
                    if x == 8:
                        x = 0    
    
if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()

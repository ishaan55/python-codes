import pygame

LENGHT = 7
class Toothpick:
    def __init__(self,cx,cy,direction,WIN) -> None:
        self.cx,self.cy = cx,cy
        self.dir = direction
        if direction == 1:
            self.ax,self.ay = cx - LENGHT,cy
            self.bx,self.by = cx + LENGHT,cy
        else:
            self.ax,self.ay = cx, cy - LENGHT
            self.bx,self.by = cx, cy + LENGHT
        self.WIN = WIN
        
    def show(self,color='black'):
        pygame.draw.line(self.WIN,(color),(self.ax,self.ay),(self.bx,self.by),width=2)
    
    def next(self,others):
        a_available = b_available = True
        for i in others:
            if i != self:
                if (i.ax,i.ay) == (self.ax,self.ay) or (i.bx,i.by) == (self.ax,self.ay):
                    a_available = False
                    break
        for i in others:
            if i != self:
                if (i.ax,i.ay) == (self.bx,self.by) or (i.bx,i.by) == (self.bx,self.by):
                    b_available = False
                    break
        
        result = []
        if a_available:
            result.append((self.ax,self.ay))
        if b_available:
            result.append((self.bx,self.by))

        return result

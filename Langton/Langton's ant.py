# Simulation of Langton's ant https://en.wikipedia.org/wiki/Langton%27s_ant 
# Change settings in line 12
# Add more ants in line 62

import pygame
pygame.init()

WIDTH,HEIGHT = 1920,1080
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Langton's Ant")

# Settings                                
BACKGROUND_COLOR = (0,0,0)
OTHER_COLOR = (0,255,0)
SPACING = 1
STEPS_PER_FRAME = 100
FPS = 60

rows = int(WIDTH/SPACING)
cols = int(HEIGHT/SPACING)

class ant:
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.dir = (0,1)

    def move(self,ndir):
        if ndir == 0:
            self.dir = (-1,0)
        elif ndir == 1:
            self.dir = (0,1)
        elif ndir == 2:
            self.dir = (1,0)
        elif ndir == 3:
            self.dir = (0,-1)
        self.x += self.dir[0]
        self.y += self.dir[1]
        if self.x < 0:
            self.x = rows-1
        elif self.x > rows-1:
            self.x = 0
        elif self.y < 0:
            self.y = cols-1
        elif self.y > cols-1:
            self.y = 0


def main():

    grid = []

    for i in range(rows):
        temp = []
        for j in range(cols):
            x = [pygame.Rect(i*SPACING,j*SPACING,SPACING,SPACING),BACKGROUND_COLOR]
            temp.append(x)
        grid.append(temp)
    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(WIN,grid[i][j][1],grid[i][j][0])

    # Add ants [make an ant instance and add it in the ants list]
    ant1 = [ant(int(rows/2),int(cols/2)),0]                  # 2nd argument is starting direction 0-UP, 1-RIGHT, 2-DOWN, 3-LEFT
    # ant2 = [ant(int(rows/2)+9,int(cols/2)),0]
    ants = [ant1]

    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for ant_ in ants:
            for _ in range(STEPS_PER_FRAME):
                x,y = ant_[0].x,ant_[0].y
                if grid[x][y][1] == BACKGROUND_COLOR:
                    ant_[1] -= 1
                    if ant_[1] > 3:
                        ant_[1] = 0
                    elif ant_[1]<0:
                        ant_[1] = 3
                    ant_[0].move(ant_[1])
                    grid[x][y][1] = OTHER_COLOR
                    pygame.draw.rect(WIN,grid[x][y][1],grid[x][y][0])
                x,y = ant_[0].x,ant_[0].y
                if grid[x][y][1] == OTHER_COLOR:
                    ant_[1] += 1
                    if ant_[1] > 3:
                        ant_[1] = 0
                    elif ant_[1] < 0:
                        ant_[1] = 3
                    ant_[0].move(ant_[1])
                    grid[x][y][1] = BACKGROUND_COLOR
                    pygame.draw.rect(WIN,grid[x][y][1],grid[x][y][0])

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()
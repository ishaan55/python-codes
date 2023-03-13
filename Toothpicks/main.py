import pygame
from toothpick import Toothpick
pygame.init()

WIDTH,HEIGHT = 1920,1080
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Toothpick')
FONT = pygame.font.Font(None, 64)



def main():
    picks = []
    nextpicks = []
    x = Toothpick(WIDTH/2,HEIGHT/2,1,WIN)
    picks.append(x)
    nextpicks.append(x)
    
    Total = 1
    total_font = FONT.render(str(Total),True,(0,0,0))
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                p = []
                for pick in nextpicks:
                    new = pick.next(picks)
                    for i in new:
                        x = Toothpick(i[0],i[1],pick.dir * -1,WIN)
                        p.append(x)

                picks += p
                nextpicks = p.copy()
                total_font = FONT.render(str(len(picks)),True,(0,0,0))


        WIN.fill('white')
        WIN.blit(total_font,(50,50))
        for pick in picks:
            if pick in nextpicks:
                pick.show('blue')
            else:
                pick.show()

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()
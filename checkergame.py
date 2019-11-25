import pygame
pygame.init()

#The initiliazation
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Checkerboard")
board = pygame.image.load('check.jpg')

clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.block = [8,1]


    def draw(self,win):
        self.contour = (self.x,self.y,self.width,self.height)
        pygame.draw.rect(win,(255,0,0), self.contour,2)
class piece(object):
    def __init__(self,position,color):
        self.position = position
        self.color = color
    def draw(self,win):
        self.coords = (25+28+(self.position[1]-1)*56,30+27+(self.position[0]-1)*55)
        pygame.draw.circle(win,self.color, self.coords, 20)


def redrawGameWindow():
    win.blit(board, (0,0))
    text = font.render('It is your turn!', 1, (255,255,255))
    win.blit(text,(300,10))
    player1.draw(win)
    for whitepiece in whitepieces:
        whitepiece.draw(win)

    pygame.display.update()


#mainloop
font = pygame.font.SysFont('comicsans',30,True,False)
player1 = player(25,470-55,55,55)
whitepieces = []
#for x in range(1,5):
#    for y in range(1,5):
#        piece = piece([1+(y-1)*2,x])
apiece = piece([1,1],(255,255,255))
whitepieces.append(apiece)
walkLoop = 0

run = True
while run:
    clock.tick(27)
    if walkLoop > 0:
        walkLoop += 1
    if walkLoop > 5:
        walkLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #The inputs:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player1.x>0 and walkLoop == 0:
        player1.x -= 56
        walkLoop = 1
        player1.block[1]-=1
        print(player1.block)
    if keys[pygame.K_UP] and player1.y>62.5 and walkLoop == 0:
        player1.y -= 55
        walkLoop = 1
        player1.block[0]-=1
        print(player1.block)
    if keys[pygame.K_RIGHT] and player1.x<(437.5) and walkLoop == 0:
        player1.x += 56
        walkLoop = 1
        player1.block[1]+=1
        print(player1.block)
    if keys[pygame.K_DOWN] and player1.y<437.5 and walkLoop == 0:
        player1.y += 55
        walkLoop = 1
        player1.block[0]+=1
        print(player1.block)

    redrawGameWindow()

pygame.quit()

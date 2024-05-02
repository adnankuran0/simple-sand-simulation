import pygame, math
import random as r

pygame.init()


screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
dt = 0
running = True
fps = 60


grid_size = 20


grain_objects = []



class grain:
    def __init__(self):
        mouse = pygame.mouse.get_pos()
        self.pos = pygame.Vector2((math.floor(mouse[0]/grid_size))*grid_size,mouse[1])
        self.is_moving = True
        self.rightCheckList = []
        self.leftCheckList = []
        self.colour = (r.randint(150,250),r.randint(150,250),r.randint(150,250))
        
    
    def checkRight(self,g):
        self.gr = g

        if self.gr.pos.x == self.pos.x+grid_size and self.gr.pos.y <  self.pos.y + (3*grid_size):
            self.rightCheckList.append(True)
            
        else:
            self.rightCheckList.append(False)

    def checkLeft(self,g):
        self.gr = g

        if self.gr.pos.x == self.pos.x-grid_size and self.gr.pos.y <  self.pos.y + (3*grid_size):
            self.leftCheckList.append(True)
            
        else:
            self.leftCheckList.append(False)
            

    def update(self):
        global grid_size

        if self.is_moving:
            self.pos.y += 800 * dt

            if self.pos.y > 720 - grid_size:
                self.pos.y = 720 - grid_size
                self.is_moving = False

        for g in grain_objects:
            self.checkRight(g)
            self.checkLeft(g)
            

        for g in grain_objects:
            
            if self.pos.y + grid_size >= g.pos.y and self.pos.y + grid_size < g.pos.y + grid_size:
                if self.pos.x == g.pos.x:
                    

                    if not g.is_moving:
                        self.is_moving = False
                        self.pos.y = g.pos.y - grid_size

                    

                    if True not in self.leftCheckList and True not in self.rightCheckList:
                        if not g.is_moving:
                            if r.randint(0,1) == 1:                                         
                                self.pos.x += grid_size
                                self.is_moving = True
                                self.rightCheckList = []
                            else:
                                self.pos.x -= grid_size
                                self.is_moving = True
                                self.leftCheckList = []

                    
                 
                    elif True not in self.rightCheckList:
           
                        if not g.is_moving:                                         
                            self.pos.x += grid_size
                            self.is_moving = True
                            self.rightCheckList = []

                    elif True not in self.leftCheckList:
        
                        if not g.is_moving:                                         
                            self.pos.x -= grid_size
                            self.is_moving = True
                            self.leftCheckList = []
                    else:
                        self.rightCheckList = []
                        self.leftCheckList = []

                           

        pygame.draw.rect(screen,self.colour,((self.pos.x,self.pos.y,grid_size,grid_size)))


time_since_last_grain = 0
grain_interval = 1



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    m = pygame.mouse.get_pressed()
    

    if m[0]:
        time_since_last_grain += dt * 10


        if time_since_last_grain >= grain_interval:
            grain_objects.append(grain())
            time_since_last_grain = 0

    screen.fill("black")


    for g in grain_objects:
        g.update()

        

    pygame.display.flip()

    dt = clock.tick(fps) / 1000



pygame.quit()
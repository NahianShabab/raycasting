import math
class Point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Vector2D:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y
    def dot(self,other):
        return self.x*other.x+self.y*other.y
    def cross(self,other):
        return self.x*other.y-self.y*other.x
    def rotate(self,theta:float):
        return Vector2D(self.x*math.cos(theta)-self.y*math.sin(theta),self.x*math.sin(theta)+self.y*math.cos(theta))

class Case:
    def __init__(self,o:Point2D,dir:Vector2D,p:Point2D,v:Vector2D):
        self.o=o
        self.dir=dir
        self.p=p
        self.v=v

def test_case(c:Case):
    A = c.v.cross(c.dir)
    if A == 0:
        return (False,-1,-1)
    t = (-c.v.y*(c.p.x-c.o.x)+c.v.x*(c.p.y-c.o.y))/A
    s = (c.dir.x*(c.p.y-c.o.y)-c.dir.y*(c.p.x-c.o.x))/A
    if t<0 or s<0 or s>1:
        return (False,t,s)
    return (True,t,s)

cases=[
    Case(Point2D(5,2),Vector2D(0,1),Point2D(4,5),Vector2D(6,0)),
    Case(Point2D(7,2),Vector2D(0,1),Point2D(4,5),Vector2D(6,0)),
    Case(Point2D(9,2),Vector2D(0,1),Point2D(4,5),Vector2D(6,0)),
    Case(Point2D(5,-10),Vector2D(0,-1),Point2D(4,5),Vector2D(6,0)),
    Case(Point2D(11,2),Vector2D(0,1),Point2D(4,5),Vector2D(6,0)),
    Case(Point2D(11,-10),Vector2D(-1,0),Point2D(4,5),Vector2D(6,0)),
    Case(Point2D(9,2),Vector2D(-1/2**0.5,1/2**0.5),Point2D(4,5),Vector2D(6,0))
]

def test_all_cases():
    # iterate all cases with index
    for i,c in enumerate(cases):
        result,t,s=test_case(c)
        if result==True:
            p_t=Point2D(c.o.x+c.dir.x*t,c.o.y+c.dir.y*t)
            p_s=Point2D(c.p.x+c.v.x*s,c.p.y+c.v.y*s)
            dist=c.dir.y*t
            print(f"Case {i+1} : passed: t={t}, s={s} p_t=({p_t.x},{p_t.y}) p_s=({p_s.x},{p_s.y}) dist={dist}")
        else:
            print(f"Case {i+1} : failed: t={t}, s={s}")

# test_all_cases()

# print(test_case(cases[3]))


class Wall:
    def __init__(self,p1:Point2D,p2:Point2D):
        self.p1=p1
        self.p2=p2
    def get_dir(self):
        return Vector2D(self.p2.x-self.p1.x,self.p2.y-self.p1.y)




import pygame

# Initialize Pygame
pygame.init()

# Set up display dimensions
width = 800
height = 600

# Create a window
screen = pygame.display.set_mode((width, height))

# Set the caption for the window
pygame.display.set_caption("Pygame Window")

o=Point2D(0,0)
l=Vector2D(1/2**0.5,1/2**0.5)

# sw=100
# sh=50
fov=60

wall=Wall(Point2D(-5,5),Point2D(5,5))

def perform_ray_cast():
    for i in range(0,width):
        angle=math.radians(fov/2-(fov/(width-1))*i)
        dir = l.rotate(angle)
        c=Case(o,dir,wall.p1,wall.get_dir())
        result,t,s=test_case(c)
        if result==True:
            p_t=Point2D(c.o.x+c.dir.x*t,c.o.y+c.dir.y*t)
            p_s=Point2D(c.p.x+c.v.x*s,c.p.y+c.v.y*s)
            dist=dir.dot(l) * t
            if dist==0:
                dist=1
            dist=1*height/dist
            # print(f"Case {i} : passed: t={t}, s={s} p_t=({p_t.x},{p_t.y}) p_s=({p_s.x},{p_s.y}) dist={dist}")
            if dist>height:
                dist=height
            # print(dist)
            pygame.draw.line(screen,(255,0,0),(i,height/2-dist/2),(i,height/2+dist/2))
        else:
            print("failed")
            # print(f"Case {i} : failed: t={t}, s={s}")
            pass

# perform_ray_cast()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # player movement WASD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                o.x = o.x + l.x *2
                o.y = o.y + l.y *2
                pass
            elif event.key == pygame.K_s:
                o.x = o.x - l.x *2
                o.y = o.y - l.y *2
            elif event.key == pygame.K_a:
                l = l.rotate(math.radians(5))
            elif event.key == pygame.K_d:
                l = l.rotate(math.radians(-5))

            
    
    screen.fill((0,0,0),(0,0,width,height))
    
    # Add game logic and rendering here
    perform_ray_cast()
    # Update the display
    pygame.display.flip()
    # print(o.y)

# Quit Pygame
pygame.quit()

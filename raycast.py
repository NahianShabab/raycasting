import math,sys
import pygame
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
    # # checking if the line is behind the ray
    # vec1=Vector2D(c.p.x-c.o.x,c.p.y-c.o.y)
    # vec2=Vector2D(c.p.x+c.v.x-c.o.x,c.p.y+c.v.y-c.o.y)
    # if vec1.dot(c.dir)<0 and vec2.dot(c.dir)<0:
    #     return (False,-1,-1)
    A = c.v.cross(c.dir)
    if A == 0:
        return (False,-1,-1)
    # for reducing calculations
    X=c.p.x-c.o.x
    Y=c.p.y-c.o.y
    
    t = (-c.v.y*X+c.v.x*Y)/A
    s = (c.dir.x*Y-c.dir.y*X)/A
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
    def __init__(self,p1:Point2D,p2:Point2D,color:tuple=(255,255,255)):
        self.p1=p1
        self.p2=p2
        self.color=color
    def get_dir(self):
        return Vector2D(self.p2.x-self.p1.x,self.p2.y-self.p1.y)





# Initialize Pygame
pygame.init()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

# Set up display dimensions
width = 800
height = 600

# Create a window
screen = pygame.display.set_mode((width, height))

# Set the caption for the window
pygame.display.set_caption("Pygame Window")

o=Point2D(545,299)
l=Vector2D(0,1)

# sw=100
# sh=50
fov=60

mouse_sensitivity=0.03

wall=Wall(Point2D(-5,5),Point2D(5,5),color=(255,0,0))
walls = [
 Wall(Point2D(193,110),Point2D(547,106),(192,160,98)),
Wall(Point2D(547,106),Point2D(548,186),(47,69,96)),
Wall(Point2D(548,186),Point2D(495,186),(214,167,66)),
Wall(Point2D(495,186),Point2D(498,137),(169,169,65)),
Wall(Point2D(498,137),Point2D(446,139),(94,67,107)),
Wall(Point2D(446,139),Point2D(443,183),(180,135,249)),
Wall(Point2D(443,183),Point2D(390,181),(247,235,165)),
Wall(Point2D(390,181),Point2D(402,140),(103,92,25)),
Wall(Point2D(402,140),Point2D(343,141),(242,167,16)),
Wall(Point2D(343,141),Point2D(337,189),(138,203,218)),
Wall(Point2D(337,189),Point2D(287,190),(131,19,165)),
Wall(Point2D(287,190),Point2D(280,146),(176,52,24)),
Wall(Point2D(280,146),Point2D(237,148),(140,79,239)),
Wall(Point2D(237,148),Point2D(229,195),(124,48,108)),
Wall(Point2D(229,195),Point2D(200,195),(178,241,112)),
Wall(Point2D(200,195),Point2D(141,194),(29,240,83)),
Wall(Point2D(141,194),Point2D(146,247),(170,128,56)),
Wall(Point2D(146,247),Point2D(191,252),(39,79,64)),
Wall(Point2D(191,252),Point2D(195,308),(216,159,161)),
Wall(Point2D(195,308),Point2D(151,306),(15,5,175)),
Wall(Point2D(151,306),Point2D(159,363),(92,209,242)),
Wall(Point2D(159,363),Point2D(200,365),(121,122,94)),
Wall(Point2D(200,365),Point2D(200,415),(210,168,132)),
Wall(Point2D(200,415),Point2D(159,419),(63,77,87)),
Wall(Point2D(159,419),Point2D(163,476),(134,106,5)),
Wall(Point2D(163,476),Point2D(206,476),(139,143,124)),
Wall(Point2D(206,476),Point2D(202,527),(193,194,50)),
Wall(Point2D(202,527),Point2D(163,524),(21,35,202)),
Wall(Point2D(163,524),Point2D(170,571),(18,28,182)),
Wall(Point2D(170,571),Point2D(225,572),(171,195,45)),
Wall(Point2D(225,572),Point2D(281,570),(23,3,32)),
Wall(Point2D(281,570),Point2D(280,526),(6,76,223)),
Wall(Point2D(280,526),Point2D(339,476),(59,65,196)),
Wall(Point2D(339,476),Point2D(371,517),(101,18,150)),
Wall(Point2D(371,517),Point2D(385,566),(26,126,162)),
Wall(Point2D(385,566),Point2D(452,559),(108,201,53)),
Wall(Point2D(452,559),Point2D(453,507),(148,5,154)),
Wall(Point2D(453,507),Point2D(518,504),(159,183,214)),
Wall(Point2D(518,504),Point2D(518,557),(247,37,90)),
Wall(Point2D(518,557),Point2D(576,553),(121,242,143)),
Wall(Point2D(576,553),Point2D(580,500),(91,175,150)),
Wall(Point2D(580,500),Point2D(632,502),(13,232,231)),
Wall(Point2D(632,502),Point2D(624,439),(85,48,197)),
Wall(Point2D(624,439),Point2D(580,438),(33,48,77)),
Wall(Point2D(580,438),Point2D(578,377),(232,17,200)),
Wall(Point2D(578,377),Point2D(632,376),(234,244,48)),
Wall(Point2D(632,376),Point2D(627,304),(243,210,220)),
Wall(Point2D(627,304),Point2D(562,311),(255,27,113)),
Wall(Point2D(562,311),Point2D(563,243),(179,207,149)),
Wall(Point2D(563,243),Point2D(628,239),(171,28,194)),
Wall(Point2D(628,239),Point2D(624,178),(173,202,251)),
Wall(Point2D(624,178),Point2D(619,26),(31,6,104)),
Wall(Point2D(619,26),Point2D(192,28),(36,3,40)),
Wall(Point2D(192,28),Point2D(192,110),(246,200,142)),
Wall(Point2D(192,110),Point2D(193,110),(187,157,143)),
Wall(Point2D(345,240),Point2D(390,240),(171,57,22)),
Wall(Point2D(390,240),Point2D(388,274),(136,32,128)),
Wall(Point2D(388,274),Point2D(349,274),(145,85,156)),
Wall(Point2D(349,274),Point2D(344,245),(202,243,3)),
Wall(Point2D(344,245),Point2D(345,240),(244,0,161)),


]

floor_color=(128,128,128)
ceil_color=(255,255,255)

def perform_ray_cast():
    for i in range(0,width):
        angle=math.radians(fov/2-(fov/(width-1))*i)
        dir = l.rotate(angle)
        t=sys.float_info.max
        intersected=False
        color=(0,0,0)
        for w in walls:
            c=Case(o,dir,w.p1,w.get_dir())
            result,t_1,s=test_case(c)
            if result==True:
                intersected=True
                # p_t=Point2D(c.o.x+c.dir.x*t,c.o.y+c.dir.y*t)
                # p_s=Point2D(c.p.x+c.v.x*s,c.p.y+c.v.y*s)
                if t_1<t:
                    t=t_1
                    color=w.color
                    # print(f"Case {i} : passed: t={t}, s={s} p_t=({p_t.x},{p_t.y}) p_s=({p_s.x},{p_s.y})")
            else:
                # print("failed")
                # print(f"Case {i} : failed: t={t}, s={s}")
                pass
            
        if intersected:
            dist=dir.dot(l) * t
            if dist==0:
                dist=1
            dist=32*height/dist
            # print(f"Case {i} : passed: t={t}, s={s} p_t=({p_t.x},{p_t.y}) p_s=({p_s.x},{p_s.y}) dist={dist}")
            if dist>height:
                dist=height
            # print(dist)
            pygame.draw.line(screen,color,(i,height/2-dist/2),(i,height/2+dist/2))
            pygame.draw.line(screen,ceil_color,(i,0),(i,height/2-dist/2))
            pygame.draw.line(screen,floor_color,(i,height/2+dist/2),(i,height-1))
            
def render_minimap():
    minimap_scale = 0.5  # Adjust the scale for the minimap
    minimap_offset_x = 10  # Adjust the offset for the minimap
    minimap_offset_y = 10

    for w in walls:
        p1_x = int(w.p1.x * minimap_scale) + minimap_offset_x
        p1_y = height- int(w.p1.y * minimap_scale) + minimap_offset_y
        p2_x = int(w.p2.x * minimap_scale) + minimap_offset_x
        p2_y = height- int(w.p2.y * minimap_scale) + minimap_offset_y
        pygame.draw.line(screen, w.color, (p1_x, p1_y), (p2_x, p2_y), 1)

    player_x = int(o.x * minimap_scale) + minimap_offset_x
    player_y = height- int(o.y * minimap_scale) + minimap_offset_y
    pygame.draw.circle(screen, (255,0,0), (player_x, player_y), 6)
    pygame.draw.line(screen,(0,0,255),(player_x,player_y),(player_x+l.x*40,player_y-l.y*40))

# Add the render_minimap function within the game loop
# Below the perform_ray_cast function call, add the render_minimap function call
# before updating the display


prev_mouse_pos=pygame.mouse.get_pos()
clock=pygame.time.Clock()
time_passed=0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # player movement WASD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                o.x = o.x + l.x *20
                o.y = o.y + l.y *20
                pass
            elif event.key == pygame.K_s:
                o.x = o.x - l.x *20
                o.y = o.y - l.y *20
            elif event.key == pygame.K_a:
                l = l.rotate(math.radians(5))
            elif event.key == pygame.K_d:
                l = l.rotate(math.radians(-5))
                
        if event.type == pygame.MOUSEMOTION:
            # print("here")
            pos=pygame.mouse.get_pos()
            dx=pos[0]-prev_mouse_pos[0]
            prev_mouse_pos=pos
            l=l.rotate(-dx*mouse_sensitivity)
    
    
    # FPS KEEPING AT 25
    time_passed+=clock.tick()
    if time_passed>=40:
        print(time_passed)
        time_passed=0
    else:
        continue
    
    screen.fill((0,0,0),(0,0,width,height))
    
    # Add game logic and rendering here
    perform_ray_cast()
    render_minimap()
    # Update the display
    pygame.display.flip()
    # print(o.y)

# Quit Pygame
pygame.quit()

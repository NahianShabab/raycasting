import pygame
import random as r

# Initialize Pygame
pygame.init()

# Set up display dimensions
width = 800
height = 600

# Create a window
screen = pygame.display.set_mode((width, height))

# Set the caption for the window
pygame.display.set_caption("Draw Lines")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# List to store the points
points = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                points.append(event.pos)
                print(event.pos)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the points as lines
    if len(points) > 1:
        pygame.draw.lines(screen, BLACK, False, points, 2)

    # Update the display
    pygame.display.flip()

with open('wall.txt', 'w') as file:
    for i in range(0,len(points)):
        p_1=points[i]
        p_2=points[i+1] if i!=len(points)-1 else points[0]
        color=(r.randrange(0,256),r.randrange(0,256),r.randrange(0,256))
        file.write(f"Wall(Point2D({p_1[0]},{p_1[1]}),Point2D({p_2[0]},{p_2[1]}),({color[0]},{color[1]},{color[2]})),\n")

# Quit Pygame
pygame.quit()

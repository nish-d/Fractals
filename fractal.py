

import pygame
import eztext
white = (0, 0, 0)
black = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
fractal_level = 1

def recursive_draw(x, y, width, height, count):

 
    pygame.draw.rect(screen,black,[x,y,width,height],1)
    pygame.draw.line(screen,
                     black,
                     [x + width * .25, height // 2 + y],
                     [x + width * .75, height // 2 + y],
                     3)
    pygame.draw.line(screen,
                     black,
                     [x + width * .25, (height * .5) // 2 + y],
                     [x + width * .25, (height * 1.5) // 2 + y],
                     3)
    pygame.draw.line(screen,
                     black,
                     [x + width * .75, (height * .5) // 2 + y],
                     [x + width * .75, (height * 1.5) // 2 + y],
                     3)

    if count > 0:
        count -= 1
        # Top left
        recursive_draw(x, y, width // 2, height // 2, count)
        # Top right
        recursive_draw(x + width // 2, y, width // 2, height // 2, count)
        # Bottom left
        recursive_draw(x, y + width // 2, width // 2, height // 2, count)
        # Bottom right
        recursive_draw(x + width // 2, y + width // 2, width // 2, height // 2, count)

def recursive_triangle(p1,p2,p3,count):

    pygame.draw.polygon(screen, black, [p1, p2, p3], 3)

    p3t=getmid(p1,p2)
    p1t=getmid(p2,p3)
    p2t=getmid(p3,p1)
    if(count>0):
        count-=1
        recursive_triangle(p1t,p2t,p3t,count)       #middle traingle
        recursive_triangle(getmid(p2t,p3t), getmid(p1,p3t), getmid(p2t,p1), count-1)     #upper triangle
        recursive_triangle(getmid(p2,p1t),getmid(p3t,p1t), getmid(p2,p3t), count-1)
        recursive_triangle(getmid(p3,p1t), getmid(p2t,p3), getmid(p2t,p1t), count-1)


def getmid(p1,p2):
    midx=abs(p1[0]+p2[0])/2
    midy=abs(p1[1]+p2[1])/2
    return [midx,midy]


pygame.init()

# Set the height and width of the screen
size = [700, 700]
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 24)
instruction_page=1
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

display_instructions=True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# --------INTRODUCTION ----------------
# -------- Instruction Page Loop -----------

while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                instruction_page = 2
            if event.key == pygame.K_LEFT:
                instruction_page = 3
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    fractal_level += 1
            if event.key == pygame.K_DOWN:
                    fractal_level -= 1

        if fractal_level < 0 or fractal_level > 10:
                    fractal_level = 0

    # Set the screen background
    screen.fill(white)

    if instruction_page == 1:
        text = font.render("Instructions", True, black)
        screen.blit(text, [10, 10])

        text = font.render("A fractal is a natural phenomenon or a mathematical set that exhibits a repeating", True, black)
        screen.blit(text, [10, 30])

        text = font.render(" pattern that displays at every scale.", True, black)
        screen.blit(text, [10, 50])

        text = font.render("We are displaying the following fractals:", True, black)
        screen.blit(text, [10, 90])

        text = font.render("1. Triangle", True, black)
        screen.blit(text, [10, 110])

        text = font.render("2. H- like form", True, black)
        screen.blit(text, [10, 130])

        text = font.render("Navigation:", True, black)
        screen.blit(text, [10, 150])

        text = font.render("Left: H  Fractal", True, black)
        screen.blit(text, [10, 170])

        text = font.render("Right: Triangular  Fractal", True, black)
        screen.blit(text, [10, 190])

        text = font.render("Up: Increase the fractal level", True, black)
        screen.blit(text, [10, 210])
        text = font.render("Down: Decrease the fractal level", True, black)
        screen.blit(text, [10, 230])

    if instruction_page == 2:
        recursive_draw(0, 0, 700,700,fractal_level)

    if instruction_page == 3:
        p1 = [0, 0]
        p2 = [0, 700]
        p3 = [700, 0]
        p4=[700,700]
        recursive_triangle(p1,p2,p3,fractal_level)
        recursive_triangle(p4, p2, p3, fractal_level)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()

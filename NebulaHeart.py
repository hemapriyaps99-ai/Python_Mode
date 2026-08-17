import turtle
import math
import random
import colorsys

# 1. Define main function
def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#000000")
    screen.title("Nebula Heart Animation")
    screen.tracer(0)

    swarm_size = 300
    
    # 2. DEFINE PARTICLES LIST HERE (INSIDE main)
    particles = []

    # 3. Fill the list
    for _ in range(swarm_size):
        p = turtle.Turtle(shape="circle")
        p.speed(0)
        p.penup()
        p.shapesize(0.2)
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(50, 300)
        p.goto(dist * math.cos(angle), dist * math.sin(angle))
        particles.append(p)

    frame = 0

    # 4. Use particles inside the loop
    while True:
        try:
            scale = 15 + 2 * math.sin(frame * 0.05)

            for i, p in enumerate(particles):
                x, y = p.pos()
                
                t = (i / swarm_size) * 2 * math.pi
                target_x = 16 * (math.sin(t) ** 3) * scale
                target_y = (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * scale
                
                p.goto(x + (target_x - x) * 0.08, y + (target_y - y) * 0.08)
                
                hue = (frame * 0.005 + i / swarm_size) % 1.0
                r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
                p.color(r, g, b)

            screen.update()
            frame += 1
            
        except turtle.Terminator:
            break

# 5. Call main
if __name__ == "__main__":
    main()
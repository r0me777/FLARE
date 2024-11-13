import pygame
import random
import time
from Drone import Drone  # Importing the Drone class from your file

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drone Simulation")

# Drone settings
NUM_DRONES = 5
TARGET_COLOR = (255, 0, 0)  # Red
DRONE_COLOR = (0, 0, 255)  # Blue

# Initialize drones with random positions within the screen bounds
drones = [
    Drone(drone_id=i, start_x=random.uniform(0, WIDTH), start_y=random.uniform(0, HEIGHT))
    for i in range(NUM_DRONES)
]

# Set initial random targets for each drone
# TODO: Targets might need there own class, send they'd be athletes | sending out loc
targets = [
    (random.uniform(0, WIDTH), random.uniform(0, HEIGHT))
    for _ in range(NUM_DRONES)
]

# Main loop
running = True
clock = pygame.time.Clock()  # For controlling the frame rate

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))  # White background


    for i, drone in enumerate(drones):

        target_x, target_y = targets[i]
        drone.move_towards(target_x, target_y)


        if drone.calculate_distance(target_x, target_y) < 5:
            # Assign a new random target within the screen
            targets[i] = (random.uniform(0, WIDTH), random.uniform(0, HEIGHT))

        pygame.draw.circle(screen, DRONE_COLOR, (int(drone.x), int(drone.y)), 5)  # Drone as blue circle
        pygame.draw.circle(screen, TARGET_COLOR, (int(target_x), int(target_y)), 5)  # Target as red circle
        drone.relay_data()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(20)

# Quit Pygame
pygame.quit()

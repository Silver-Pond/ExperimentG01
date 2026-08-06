import sys

import pygame

sys.path.append("pyggel")

import pyggel
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import gluLookAt
from OpenGL.GLU import gluPerspective

# ----------------------------
# Initialise PYGGEL
# ----------------------------
pyggel.view.init(screen_size=(800, 600))

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(60, 800 / 600, 0.1, 100.0)

glMatrixMode(GL_MODELVIEW)

# ----------------------------
# Map
# ----------------------------
mapA = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# ----------------------------
# Boxes
# ----------------------------
boxes = [
    {"x": 4.5, "y": 3.5, "size": 1.0, "height": 1.0}
]

# --------------------
# Textures
# --------------------
def load_texture(filename):

    surface = pygame.image.load(filename).convert_alpha()

    data = pygame.image.tostring(surface, "RGBA", True)

    texture = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGBA,
        surface.get_width(),
        surface.get_height(),
        0,
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        data
    )

    return texture

grassTexture = load_texture("grass.png")
boxTexture = load_texture("box.png")

# ----------------------------
# Draw Map
# ----------------------------
def draw_map():

    for x in range(len(mapA)):
        for y in range(len(mapA[x])):

            if mapA[x][y] == 1:

                glPushMatrix()

                glTranslatef(x + 0.5, y + 0.5, 0.5)

                draw_textured_cube(1, grassTexture)

                glPopMatrix()

# ----------------------------
# Draw Floor
# ----------------------------
def draw_floor():

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, grassTexture)

    glColor3f(1, 1, 1)

    for x in range(len(mapA)):
        for y in range(len(mapA[x])):

            glBegin(GL_QUADS)

            glTexCoord2f(0, 0)
            glVertex3f(x, y, 0)

            glTexCoord2f(1, 0)
            glVertex3f(x + 1, y, 0)

            glTexCoord2f(1, 1)
            glVertex3f(x + 1, y + 1, 0)

            glTexCoord2f(0, 1)
            glVertex3f(x, y + 1, 0)

            glEnd()

    glDisable(GL_TEXTURE_2D)

# ----------------------------
# Draw Boxes
# ----------------------------
def draw_boxes():

    for box in boxes:

        glPushMatrix()

        glTranslatef(
            box["x"],
            box["y"],
            box["height"] / 2
        )

        draw_textured_cube(
            box["size"],
            boxTexture
        )

        glPopMatrix()

# ----------------------------
# Draw Cubes
# ----------------------------
def draw_textured_cube(size, texture):

    s = size / 2

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)

    glColor3f(1,1,1)

    glBegin(GL_QUADS)

    # Front
    glTexCoord2f(0,0); glVertex3f(-s,-s, s)
    glTexCoord2f(1,0); glVertex3f( s,-s, s)
    glTexCoord2f(1,1); glVertex3f( s, s, s)
    glTexCoord2f(0,1); glVertex3f(-s, s, s)

    # Back
    glTexCoord2f(0,0); glVertex3f( s,-s,-s)
    glTexCoord2f(1,0); glVertex3f(-s,-s,-s)
    glTexCoord2f(1,1); glVertex3f(-s, s,-s)
    glTexCoord2f(0,1); glVertex3f( s, s,-s)

    # Left
    glTexCoord2f(0,0); glVertex3f(-s,-s,-s)
    glTexCoord2f(1,0); glVertex3f(-s,-s, s)
    glTexCoord2f(1,1); glVertex3f(-s, s, s)
    glTexCoord2f(0,1); glVertex3f(-s, s,-s)

    # Right
    glTexCoord2f(0,0); glVertex3f( s,-s, s)
    glTexCoord2f(1,0); glVertex3f( s,-s,-s)
    glTexCoord2f(1,1); glVertex3f( s, s,-s)
    glTexCoord2f(0,1); glVertex3f( s, s, s)

    # Top
    glTexCoord2f(0,0); glVertex3f(-s, s, s)
    glTexCoord2f(1,0); glVertex3f( s, s, s)
    glTexCoord2f(1,1); glVertex3f( s, s,-s)
    glTexCoord2f(0,1); glVertex3f(-s, s,-s)

    # Bottom
    glTexCoord2f(0,0); glVertex3f(-s,-s,-s)
    glTexCoord2f(1,0); glVertex3f( s,-s,-s)
    glTexCoord2f(1,1); glVertex3f( s,-s, s)
    glTexCoord2f(0,1); glVertex3f(-s,-s, s)

    glEnd()

    glDisable(GL_TEXTURE_2D)

# Mouse settings
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

mouseSensitivity = 0.003

# Position settings
playerX = 5
playerY = 7.5
playerZ = 0.3

# cam and player rotation
cameraRot = 0.0
playerRot = 0.0
cameraDistance = 4.0
cameraHeight = 1.0

# Game variables
verticalVelocity = 0.0
gravity = -0.015
jumpStrength = 0.25
playerRadius = 0.25

# Heights
groundHeight = 0.3
stepHeight = 0.45

# ----------------------------
# Draw Player
# ----------------------------
def draw_player():

    glPushMatrix()

    glTranslatef(playerX, playerY, playerZ)

    glColor3f(1, 0, 0)

    draw_textured_cube(0.5, 0)

    glPopMatrix()

# ----------------------------
# Movement Helper Method
# ----------------------------
def can_move(x, y):

    checks = [
        (x-playerRadius, y),
        (x+playerRadius, y),
        (x, y-playerRadius),
        (x, y+playerRadius)
    ]

    for cx, cy in checks:

        if mapA[int(cx)][int(cy)] == 1:
            return False

    return True

# ----------------------------
# Jump Helper Method
# ----------------------------
def get_floor_height(x, y):

    floor = groundHeight

    for box in boxes:

        if (
            abs(x - box["x"]) < box["size"] - playerRadius and
            abs(y - box["y"]) < box["size"] - playerRadius
        ):
            floor = max(floor, box["height"] + playerRadius)

    return floor

# ----------------------------
# Box Helper Method
# ----------------------------
def collides_with_box(x, y, z):

    for box in boxes:

        half = box["size"] / 2

        # Inside the box footprint?
        if (
            abs(x - box["x"]) < half + playerRadius and
            abs(y - box["y"]) < half + playerRadius
        ):

            # Only collide with the sides if below the top
            if z < box["height"] - 0.02:
                return True

    return False

# ----------------------------

glEnable(GL_DEPTH_TEST)

clock = pygame.time.Clock()
running = True

while running:

    # -------------------------
    # Handle events
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    speed = 0.1

    # -------------------------
    # Mouse look
    # -------------------------
    mouseX, mouseY = pygame.mouse.get_rel()

    cameraRot -= mouseX * mouseSensitivity

    # Make the player always face the camera direction
    playerRot = cameraRot

    # -------------------------
    # Camera follows player
    # -------------------------
    camX = playerX - np.cos(cameraRot) * cameraDistance
    camY = playerY - np.sin(cameraRot) * cameraDistance
    camZ = cameraHeight + playerZ

    # -------------------------
    # Keyboard movement
    # -------------------------
    newX = playerX
    newY = playerY

    if keys[pygame.K_w]:
        newX += np.cos(playerRot) * speed
        newY += np.sin(playerRot) * speed

    if keys[pygame.K_s]:
        newX -= np.cos(playerRot) * speed
        newY -= np.sin(playerRot) * speed

    if keys[pygame.K_a]:
        newX -= np.sin(playerRot) * speed
        newY += np.cos(playerRot) * speed

    if keys[pygame.K_d]:
        newX += np.sin(playerRot) * speed
        newY -= np.cos(playerRot) * speed

    # Move on the X-axis if possible
    if can_move(newX, playerY) and not collides_with_box(newX, playerY, playerZ):
        playerX = newX

    # Move on the Y-axis if possible
    if can_move(playerX, newY) and not collides_with_box(playerX, newY, playerZ):
        playerY = newY

    # -------------------------
    # Jump
    # -------------------------
    floor = get_floor_height(playerX, playerY)

    if keys[pygame.K_SPACE] and abs(playerZ - floor) < 0.01:
        verticalVelocity = jumpStrength

    verticalVelocity += gravity
    playerZ += verticalVelocity

    floor = get_floor_height(playerX, playerY)

    if playerZ <= floor:
        playerZ = floor
        verticalVelocity = 0

    # -------------------------
    # Exit
    # -------------------------
    if keys[pygame.K_ESCAPE]:
        running = False

    # -------------------------
    # Render
    # -------------------------
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    gluLookAt(
        camX, camY, camZ,
        playerX, playerY, playerZ,
        0, 0, 1
    )
    # Calling methods
    draw_map()
    draw_floor()
    draw_boxes()
    draw_player()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
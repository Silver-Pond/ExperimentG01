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

grassSurface = pygame.image.load("grass.png")
grassData = pygame.image.tostring(grassSurface, "RGBA", True)

grassTexture = glGenTextures(1)

glBindTexture(GL_TEXTURE_2D, grassTexture)

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

glTexImage2D(
    GL_TEXTURE_2D,
    0,
    GL_RGBA,
    grassSurface.get_width(),
    grassSurface.get_height(),
    0,
    GL_RGBA,
    GL_UNSIGNED_BYTE,
    grassData
)

glEnable(GL_TEXTURE_2D)
glEnable(GL_DEPTH_TEST)

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

def draw_cube(size):

    s = size / 2

    glBegin(GL_QUADS)

    # Front
    glVertex3f(-s,-s, s)
    glVertex3f( s,-s, s)
    glVertex3f( s, s, s)
    glVertex3f(-s, s, s)

    # Back
    glVertex3f(-s,-s,-s)
    glVertex3f(-s, s,-s)
    glVertex3f( s, s,-s)
    glVertex3f( s,-s,-s)

    # Left
    glVertex3f(-s,-s,-s)
    glVertex3f(-s,-s, s)
    glVertex3f(-s, s, s)
    glVertex3f(-s, s,-s)

    # Right
    glVertex3f( s,-s,-s)
    glVertex3f( s, s,-s)
    glVertex3f( s, s, s)
    glVertex3f( s,-s, s)

    # Top
    glVertex3f(-s, s,-s)
    glVertex3f(-s, s, s)
    glVertex3f( s, s, s)
    glVertex3f( s, s,-s)

    # Bottom
    glVertex3f(-s,-s,-s)
    glVertex3f( s,-s,-s)
    glVertex3f( s,-s, s)
    glVertex3f(-s,-s, s)

    glEnd()

# Mouse settings
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

mouseSensitivity = 0.003

# Jump settings
playerX = 3
playerY = 7.5
playerZ = 0.3

# cam and player rotation
cameraRot = 0.0
playerRot = 0.0

verticalVelocity = 0.0
gravity = -0.015
jumpStrength = 0.25
groundHeight = 0.3

def draw_player():

    glPushMatrix()

    glTranslatef(playerX, playerY, playerZ)

    glColor3f(1, 0, 0)

    draw_cube(0.4)

    glPopMatrix()

cameraDistance = 4.0
cameraHeight = 1.0

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

    speed = 0.05

    # -------------------------
    # Mouse look
    # -------------------------
    mouseX, mouseY = pygame.mouse.get_rel()

    cameraRot += mouseX * mouseSensitivity

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
    forwardX = np.cos(cameraRot)
    forwardY = np.sin(cameraRot)

    rightX = -np.sin(cameraRot)
    rightY = np.cos(cameraRot)

    if keys[pygame.K_w]:
        playerX += forwardX * speed
        playerY += forwardY * speed

    if keys[pygame.K_s]:
        playerX -= forwardX * speed
        playerY -= forwardY * speed

    if keys[pygame.K_a]:
        playerX -= np.sin(playerRot) * speed
        playerY += np.cos(playerRot) * speed

    if keys[pygame.K_d]:
        playerX += np.sin(playerRot) * speed
        playerY -= np.cos(playerRot) * speed

    # -------------------------
    # Jump
    # -------------------------
    if keys[pygame.K_SPACE] and playerZ <= groundHeight + 0.001:
        verticalVelocity = jumpStrength

    verticalVelocity += gravity
    playerZ += verticalVelocity

    if playerZ < groundHeight:
        playerZ = groundHeight
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

    draw_floor()
    draw_player()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
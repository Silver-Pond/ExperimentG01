import sys

import pygame
from OpenGL.raw.GLU import gluQuadricTexture, gluQuadricNormals, GLU_SMOOTH, gluCylinder, gluDisk

sys.path.append("pyggel")

import pyggel
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import gluLookAt, gluNewQuadric
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
    [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1]
]

# ----------------------------
# Boxes
# ----------------------------
boxes = [
    {"x": 4.5, "y": 3.5, "size": 1.0, "height": 1.0}
]

# ----------------------------
# Flowers
# ----------------------------
flowers = [
    {"x": 6.5, "y": 5.5, "size": 0.5, "height": 0.5},
    {"x": 8.5, "y": 4.5, "size": 0.5, "height": 0.5},
    {"x": 7.5, "y": 3.5, "size": 0.5, "height": 0.5},
    {"x": 3.5, "y": 2.5, "size": 0.5, "height": 0.5},
    {"x": 3.5, "y": 6.5, "size": 0.5, "height": 0.5},
    {"x": 3.5, "y": 9.5, "size": 0.5, "height": 0.5},
    {"x": 5.5, "y": 9.5, "size": 0.5, "height": 0.5},
    {"x": 4.5, "y": 10.5, "size": 0.5, "height": 0.5},
    {"x": 6.5, "y": 10.5, "size": 0.5, "height": 0.5},
    {"x": 8.5, "y": 8.5, "size": 0.5, "height": 0.5},
    {"x": 6.5, "y": 12.5, "size": 0.5, "height": 0.5},
    {"x": 7.5, "y": 10.5, "size": 0.5, "height": 0.5},
    {"x": 9.5, "y": 11.5, "size": 0.5, "height": 0.5},
    {"x": 10.5, "y": 16.5, "size": 0.5, "height": 0.5},
    {"x": 10.5, "y": 12.5, "size": 0.5, "height": 0.5},
    {"x": 9.5, "y": 14.5, "size": 0.5, "height": 0.5}
]

# ----------------------------
# Coins
# ----------------------------
coins = [
    {"x": 12.5, "y": 7.5, "z": 0.5},
    {"x": 14.5, "y": 7.5, "z": 0.5},
    {"x": 16.5, "y": 7.5, "z": 0.5},
    {"x": 18.5, "y": 7.5, "z": 0.5},
    {"x": 20.5, "y": 7.5, "z": 0.5}
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
wallTexture = load_texture("wall.png")
boxTexture = load_texture("box.png")
flowerTexture = load_texture("flower.png")
coinTexture = load_texture("coin.png")

# ----------------------------
# Draw Map
# ----------------------------
def draw_map():

    for x in range(len(mapA)):
        for y in range(len(mapA[x])):

            if mapA[x][y] == 1:
                for level in range(WALL_HEIGHT):
                    glPushMatrix()

                    glTranslatef(x + 0.5, y + 0.5, level + 0.5)

                    draw_textured_cube(1, wallTexture)

                    glPopMatrix()

# ----------------------------
# Draw Floor
# ----------------------------
def draw_floor():

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
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

        glTranslatef(box["x"], box["y"], box["height"] / 2)

        draw_textured_cube(box["size"], boxTexture)

        glPopMatrix()

# ----------------------------
# Draw Coins
# ----------------------------
quadric = gluNewQuadric()

gluQuadricNormals(
    quadric,
    GLU_SMOOTH
)

gluQuadricTexture(
    quadric,
    GL_TRUE
)

def draw_coin():

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, coinTexture)

    # Coin thickness and radius
    radius = 0.18
    thickness = 0.06

    # Draw the coin
    gluCylinder(quadric, radius, radius, thickness, 32, 4)

    # Front face
    glPushMatrix()

    glTranslatef(0, 0, thickness)

    gluDisk(quadric, 0, radius, 32, 1)

    glPopMatrix()

    # Back face
    glPushMatrix()

    glRotatef(180, 1, 0, 0)

    gluDisk(quadric, 0, radius, 32, 1)

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)

def draw_coins():

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, coinTexture)

    glColor3f(1.0, 1.0, 1.0)

    for coin in coins:

        glPushMatrix()

        # Position
        glTranslatef(
            coin["x"],
            coin["y"],
            coin["z"]
        )

        # Make coin upright
        glRotatef(90, 1, 0, 0)

        # Spin around its vertical axis
        glRotatef(
            coinRotation,
            0, 1, 0
        )

        # Center the coin
        glTranslatef(0, 0, -0.03)

        # Coin cylinder
        gluCylinder(
            quadric,
            0.18,
            0.18,
            0.06,
            32,
            4
        )

        # Front
        glPushMatrix()

        glTranslatef(0, 0, 0.06)

        gluDisk(
            quadric,
            0,
            0.18,
            32,
            1
        )

        glPopMatrix()

        # Back
        glPushMatrix()

        glRotatef(180, 1, 0, 0)

        gluDisk(
            quadric,
            0,
            0.18,
            32,
            1
        )

        glPopMatrix()

        glPopMatrix()

    glDisable(GL_TEXTURE_2D)

# ----------------------------
# Draw Flowers
# ----------------------------
def draw_flower():

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, flowerTexture)

    glColor3f(1, 1, 1)

    # Draw three crossed planes
    for angle in (0, 60, 120, 180):

        glPushMatrix()

        glRotatef(angle, 0, 0, 1)

        glBegin(GL_QUADS)

        glTexCoord2f(0, 0)
        glVertex3f(-0.25, 0, 0)

        glTexCoord2f(1, 0)
        glVertex3f(0.25, 0, 0)

        glTexCoord2f(1, 1)
        glVertex3f(0.25, 0, 0.6)

        glTexCoord2f(0, 1)
        glVertex3f(-0.25, 0, 0.6)

        glEnd()

        glPopMatrix()

    glDisable(GL_TEXTURE_2D)

def draw_flowers():

    for flower in flowers:

        glPushMatrix()

        glTranslatef(flower["x"], flower["y"], flower["height"] / 2)

        draw_flower()

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
CAMERA_DISTANCE = 4.0

# Game variables
verticalVelocity = 0.0
GRAVITY = -0.025
jumpStrength = 0.25
playerRadius = 0.25
walkAngle = 0.0
coinRotation = 0.0

# Heights
GROUND_HEIGHT = 0.3
CAMERA_HEIGHT = 1.0
WALL_HEIGHT = 3

# ----------------------------
# Draw Player
# ----------------------------
def draw_player():

    glPushMatrix()

    # Move to player position
    glTranslatef(playerX, playerY, playerZ)

    # Rotate player to face movement direction
    glRotatef(np.degrees(playerRot) - 90, 0, 0, 1)

    swing = np.sin(walkAngle) * 50

    glColor3f(1, 1, 1)

    # -------------------
    # Body
    # -------------------
    glPushMatrix()
    glTranslatef(0, 0, 0.35)
    glScalef(0.45, 0.25, 0.45)
    draw_textured_cube(1, 0)
    glPopMatrix()

    # -------------------
    # Head
    # -------------------
    glPushMatrix()
    glTranslatef(0, 0, 0.75)
    glScalef(0.30, 0.30, 0.25)
    draw_textured_cube(1, 0)
    glPopMatrix()

    # -------------------
    # Left Arm
    # -------------------
    glPushMatrix()
    glTranslatef(-0.32, 0, 0.36)
    glRotatef(swing, 1, 0, 0)
    glScalef(0.12, 0.12, 0.40)
    draw_textured_cube(1, 0)
    glPopMatrix()

    # -------------------
    # Right Arm
    # -------------------
    glPushMatrix()
    glTranslatef(0.32, 0, 0.36)
    glRotatef(-swing, 1, 0, 0)
    glScalef(0.12, 0.12, 0.40)
    draw_textured_cube(1, 0)
    glPopMatrix()

    # -------------------
    # Left Leg
    # -------------------
    glPushMatrix()
    glTranslatef(-0.12, 0, -0.05)
    glRotatef(-swing, 1, 0, 0)
    glScalef(0.14, 0.14, 0.25)
    draw_textured_cube(1, 0)
    glPopMatrix()

    # -------------------
    # Right Leg
    # -------------------
    glPushMatrix()
    glTranslatef(0.12, 0, -0.05)
    glRotatef(swing, 1, 0, 0)
    glScalef(0.14, 0.14, 0.25)
    draw_textured_cube(1, 0)
    glPopMatrix()

    glPopMatrix()

# ----------------------------
# Movement Helper Method
# ----------------------------
def can_move(x, y):

    checks = [
        (x - playerRadius, y),
        (x + playerRadius, y),
        (x, y - playerRadius),
        (x, y + playerRadius)
    ]

    for cx, cy in checks:

        if mapA[int(cx)][int(cy)] == 1:
            return False

    return True

# ----------------------------
# Jump Helper Method
# ----------------------------
def get_floor_height(x, y):

    floor = GROUND_HEIGHT

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

    # Player speed
    speed = 0.2

    # Coin rotation
    coinRotation += 3.0

    if coinRotation >= 360:
        coinRotation -= 360

    # -------------------------
    # Mouse look
    # -------------------------
    mouseX, mouseY = pygame.mouse.get_rel()

    cameraRot -= mouseX * mouseSensitivity

    # -------------------------
    # Camera follows player
    # -------------------------
    camX = playerX - np.cos(cameraRot) * CAMERA_DISTANCE
    camY = playerY - np.sin(cameraRot) * CAMERA_DISTANCE
    camZ = CAMERA_HEIGHT + playerZ

    # -------------------------
    # Keyboard movement
    # -------------------------
    newX = playerX
    newY = playerY
    moving = False

    if keys[pygame.K_w]:
        newX += np.cos(playerRot) * speed
        newY += np.sin(playerRot) * speed
        moving = True

    if keys[pygame.K_s]:
        newX -= np.cos(playerRot) * speed
        newY -= np.sin(playerRot) * speed
        moving = True

    if keys[pygame.K_a]:
        newX -= np.sin(playerRot) * speed
        newY += np.cos(playerRot) * speed
        moving = True

    if keys[pygame.K_d]:
        newX += np.sin(playerRot) * speed
        newY -= np.cos(playerRot) * speed
        moving = True

    if moving:
        walkAngle += 0.5
        # Make the player always face the camera direction
        playerRot = cameraRot
    else:
        walkAngle *= 0.11  # Smoothly return to standing

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

    verticalVelocity += GRAVITY
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
    draw_floor()
    draw_map()
    draw_boxes()
    draw_flowers()
    draw_coins()
    draw_player()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
import sys
import pygame
from pygame.locals import *
from pygame import mixer
from math import sqrt, pow
from load_levels import levels


# Initialise PyGame.
pygame.init()

# Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
fps = 60.0
fpsClock = pygame.time.Clock()

# Set up the window.
width, height = int(1920 / 2), int(1080 / 2)
screen = pygame.display.set_mode((width, height))

# icon
icon = pygame.image.load("game_files/blob.ico")
pygame.display.set_icon(icon)

#title
pygame.display.set_caption("corcle")



class Distance():
    def distance(self, x1, y1, x2, y2):
        return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))


class circle_wall(Distance):
    def __init__(self, radius, cords):
        self.radius = radius
        self.cords = cords
        self.x, self.y = self.cords

    def circle_update(self, P):  # playerx, playery

        pygame.draw.circle(screen, (211, 211, 211), self.cords, self.radius)

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and not P.launched:
            if P.x > self.x:
                P.setx += self.radius + P.radius - \
                    self.distance(P.x, P.y, self.x, self.y) + 2
                P.append_to_keys_blocked("a")

            elif P.x < self.x:
                P.setx -= self.radius + P.radius - \
                    self.distance(P.x, P.y, self.x, self.y) + 2
                P.append_to_keys_blocked("d")

            if P.y > self.y:
                P.sety += self.radius + P.radius - \
                    self.distance(P.x, P.y, self.x, self.y) + 2
                P.append_to_keys_blocked("w")

            elif P.y < self.y:
                P.sety -= self.radius + P.radius - \
                    self.distance(P.x, P.y, self.x, self.y) + 2
                P.append_to_keys_blocked("s")


class player(Distance):
    x = 100
    y = 200
    v = 0.3
    radius = 30
    keys_blocked = []
    arrested = False
    restart_level = False
    font = pygame.font.SysFont("Arial", 24)
    counter = 0
    launched = False

    def __init__(self):
        pass

    def draw(self, dt):

        keys = pygame.key.get_pressed()

        keys_down = []

        if keys[K_w]:
            keys_down.append("w")
        if keys[K_s]:
            keys_down.append("s")
        if keys[K_d]:
            keys_down.append("d")
        if keys[K_a]:
            keys_down.append("a")
        if keys[K_r]:
            keys_down.append("r")
        if self.radius < 100:
            pygame.draw.circle(screen, (0, 0, 255),
                               (self.x, self.y), self.radius)

        if "r" in keys_down:
            self.restart_level = True

        if self.arrested:
            keys_down = []
            text = self.font.render('Press r to restart', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.y = screen.get_height()*0.8 + 50
            screen.blit(text, text_rect)
            text = self.font.render('You are caught', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.y = screen.get_height()*0.8
            screen.blit(text, text_rect)

        if "w" in keys_down and not "w" in self.keys_blocked:
            self.y -= self.v * dt

        if "s" in keys_down and not "s" in self.keys_blocked:
            self.y += self.v * dt

        if "d" in keys_down and not "d" in self.keys_blocked:
            self.x += self.v * dt

        if "a" in keys_down and not "a" in self.keys_blocked:
            self.x -= self.v * dt

        self.keys_blocked = []

    @property
    def setx(self):
        return self.x

    @property
    def sety(self):
        return self.y

    @setx.setter
    def setx(self, x):
        self.x = x

    @sety.setter
    def sety(self, y):
        self.y = y

    def append_to_keys_blocked(self, key):
        self.keys_blocked.append(key)

    def set_arrested(self, state: bool):
        self.arrested = state

    @property
    def Radius(self):
        print(self.radius)

    @sety.setter
    def Radius(self, radius):
        self.radius = radius

    def set_restart(self, state: bool):
        self.restart_level = state

    def set_launched(self, state: bool):
        self.launched = state


class guard(Distance):
    v = 1
    death = False
    sound_played = False
    # runing = False

    def __init__(self, cords1, cords2, radius):
        self.cords1 = cords1
        self.cords2 = cords2
        self.radius = radius
        self.current_cords = cords1
        self.current_goal = cords2
        self.x1, self.y1 = cords1
        self.x2, self.y2 = cords2
        self.x, self.y = self.x1, self.y1

    def guard_update(self, P, loaded_level, dt):
        self.x, self.y = self.current_cords

        move = 2

        if self.current_goal == self.current_cords:
            if self.current_goal == self.cords1:
                self.current_goal = self.cords2
            elif self.current_goal == self.cords2:
                self.current_goal = self.cords1

        if self.current_goal[0] > self.current_cords[0]:
            var = self.current_cords[0] + move
            self.current_cords = (var, self.current_cords[1])

        elif self.current_goal[0] < self.current_cords[0]:
            var = self.current_cords[0] - move
            self.current_cords = (var, self.current_cords[1])

        if self.current_goal[1] < self.current_cords[1]:
            var = self.current_cords[1] - move
            self.current_cords = (self.current_cords[0], var)

        elif self.current_goal[1] > self.current_cords[1]:
            var = self.current_cords[1] + move
            self.current_cords = (self.current_cords[0], var)

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and not self.death and not P.launched:
            if P.radius < self.radius + 10:
                P.set_arrested(True)
                # move player
                if P.x > self.x:
                    P.setx += self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("a")

                elif P.x < self.x:
                    P.setx -= self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("d")

                if P.y > self.y:
                    P.sety += self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("w")

                elif P.y < self.y:
                    P.sety -= self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("s")

            else:
                hit = mixer.Sound("game_files/hit.wav")
                hit.play(0)
                self.death = True

        if not self.death:
            pygame.draw.circle(screen, (255, 0, 0),
                               self.current_cords, self.radius)

        if P.arrested and not self.sound_played:
            hit = mixer.Sound("game_files/hit.wav")
            hit.play(0)
            self.sound_played = True

class size_pad(Distance):
    font = pygame.font.SysFont("Arial", 24)

    def __init__(self, radius, cords, size_change_max, size_change_min):
        self.radius = radius
        self.x, self. y = cords
        self.cords = cords
        self.size_change_max = size_change_max
        self.size_change_min = size_change_min

    def shrinking_pad_update(self, P):

        pygame.draw.circle(screen, (34, 139, 34), self.cords, self.radius)

        text = self.font.render('(v)', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.cords[0]
        text_rect.centery = self.cords[1]
        screen.blit(text, text_rect)

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and not P.launched:
            if P.radius > self.size_change_min:
                P.Radius = P.radius - 1
            else:
                pass

    def growing_pad_update(self, P):
        pygame.draw.circle(screen, (34, 139, 34), self.cords, self.radius)

        text = self.font.render('(^)', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.cords[0]
        text_rect.centery = self.cords[1]
        screen.blit(text, text_rect)

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and not P.launched:
            if P.radius < self.size_change_max:
                P.Radius = P.radius + 1
            else:
                pass


class end_point(Distance):
    font = pygame.font.SysFont("Arial", 24)
    played = False

    def __init__(self, radius, cords, next_level):
        self.radius = radius
        self.cords = cords
        self.x, self.y = cords
        self.next_level = next_level

    def end_point_update(self, P):
        pygame.draw.circle(screen, (255, 170, 71), self.cords, self.radius)

        text = self.font.render('(-)', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.cords[0]
        text_rect.centery = self.cords[1]
        screen.blit(text, text_rect)

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and not P.launched:
            if not self.played:
                end_sound = mixer.Sound("game_files/next_level.wav")
                end_sound.play(0)
                self.played = True

            return self.next_level, False
        else:
            return current_level, True


class text_box(Distance):
    font = pygame.font.SysFont("Arial", 24)
    played = False

    def __init__(self, radius, cords, text, next_level):
        self.cords = cords
        self.x, self.y = cords
        self.text = text
        self.next_level = next_level
        self.radius = radius

    def text_update(self, P):
        text = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.cords[0]
        text_rect.centery = self.cords[1]
        screen.blit(text, text_rect)

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and not P.launched:
            if self.next_level != None:
                if not self.played:
                    end_sound = mixer.Sound("game_files/next_level.wav")
                    end_sound.play(0)
                    self.played = True

                return self.next_level, False

        return current_level, True


class coin(Distance):
    font = pygame.font.SysFont("Arial", 24)
    pickedUp = False

    def __init__(self, radius, cords):
        self.cords = cords
        self.x, self.y = cords
        self.radius = radius

    def coin_update(self, P):
        if not self.pickedUp:
            pygame.draw.circle(screen, (255, 170, 71), self.cords, self.radius)

            text = self.font.render('$', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = self.cords[0]
            text_rect.centery = self.cords[1]
            screen.blit(text, text_rect)

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and not self.pickedUp and not P.launched:
            self.pickedUp = True
            coin_sound = mixer.Sound("game_files/coin_sound.wav")
            coin_sound.play()


class radius_wall(Distance):
    def __init__(self, radius, cords, bufer_cords, bufer_cords_small):
        self.radius = radius
        self.x, self.y = cords
        self.cords = cords
        self.bufer_cords = bufer_cords
        self.bufer_cords_small = bufer_cords_small

    def radius_wall_update(self, P):
        if self.bufer_cords != None:
            if self.bufer_cords >= P.radius:
                pygame.draw.circle(
                    screen, (173, 216, 230, 255), self.cords, self.radius)
            else:
                pygame.draw.circle(screen, (173, 216, 255, 0),
                                   self.cords, self.radius)

            if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and self.bufer_cords >= P.radius and not P.launched:
                if P.x > self.x:
                    P.setx += self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("a")

                elif P.x < self.x:
                    P.setx -= self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("d")

                if P.y > self.y:
                    P.sety += self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("w")

                elif P.y < self.y:
                    P.sety -= self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("s")

        elif self.bufer_cords_small != None:
            if self.bufer_cords_small <= P.radius:
                pygame.draw.circle(
                    screen, (173, 216, 230, 255), self.cords, self.radius)
            else:
                pygame.draw.circle(screen, (173, 216, 255, 0),
                                   self.cords, self.radius)

            if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and self.bufer_cords_small <= P.radius and not P.launched:
                if P.x > self.x:
                    P.setx += self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("a")

                elif P.x < self.x:
                    P.setx -= self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("d")

                if P.y > self.y:
                    P.sety += self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("w")

                elif P.y < self.y:
                    P.sety -= self.radius + P.radius - \
                        self.distance(P.x, P.y, self.x, self.y) + 2
                    P.append_to_keys_blocked("s")


class jump_pad(Distance):
    font = pygame.font.SysFont("Arial", 24)
    launched = False
    x_range = []
    y_range = []

    def __init__(self, radius, cords, lauch_to):
        self.cords = cords
        self.x, self.y = cords
        self.radius = radius
        self.x2, self.y2 = lauch_to
        self.lauch_to = lauch_to

    def jump_pad_update(self, p):
        pygame.draw.circle(screen, (50, 205, 50), self.cords, self.radius)

        text = self.font.render("_", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.cords[0]
        text_rect.centery = self.cords[1]
        screen.blit(text, text_rect)

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius:
            self.launched = True
            P.set_launched(True)
            P.append_to_keys_blocked("a")
            P.append_to_keys_blocked("w")
            P.append_to_keys_blocked("s")
            P.append_to_keys_blocked("d")

            self.x_range.clear()

            for x in range(-5, 6):
                self.x_range.append(self.x2 + x)

            self.y_range.clear()
            for x in range(-5, 6):
                self.y_range.append(self.y2 + x)

        if self.launched:
            move = 5
            if int(P.x) in self.x_range:
                pass
            elif P.x > self.x2:
                movex = int(P.x / self.x + 6)
                P.setx -= movex
            else:
                movex = int(self.x2 / P.x + 6)
                P.setx += movex
            if int(P.y) in self.y_range:
                pass
            elif P.y > self.y2:
                movey = int(P.y / self.y2 + 6)
                P.sety -= movey
            else:
                movey = int(self.y2 / P.y + 6)
                P.sety += movey

            P.append_to_keys_blocked("a")
            P.append_to_keys_blocked("w")
            P.append_to_keys_blocked("s")
            P.append_to_keys_blocked("d")
            P.set_launched(True)

        if self.distance(P.x, P.y, self.x2, self.y2) <= 10 + P.radius:
            self.launched = False
            P.set_launched(False)


class Channel():
    channel = {}

    def __init__(self):
        for i in range(1, 10):
            self.channel[str(i)] = False

    def reset(self):
        self.channel.clear()
        for i in range(1, 10):
            self.channel[str(i)] = False


class Button(Distance):
    font = pygame.font.SysFont("Arial", 24)
    display = "^^"
    activited = False

    def __init__(self, radius, cords, hold, channel):
        self.radius, self.cords, self.channel = radius, cords, channel
        self.hold = hold

    def button_update(self, P, C):
        pygame.draw.circle(screen, (0, 0, 0), self.cords, self.radius)

        text = self.font.render(self.display, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.centerx = self.cords[0]
        text_rect.centery = self.cords[1]
        screen.blit(text, text_rect)

        

        if self.distance(P.x, P.y, self.x, self.y) <= self.radius + P.radius and not P.launched:
            C.channel[self.channel] = True
            self.activited = True
            self.display = "="

        elif self.hold:
            if self.activited:
                C.channel[self.channel] = True
                self.display = "="

        else:
            C.channel[self.channel] = False
            self.display = "^^"


dt = 0
running = True
ran = False
keys_down = []
P = player()
C = Channel()
current_level = "main_menu"
loaded_level = []
redirection = []
Levels = levels()
counter = 0

# play the music
mixer.music.load("game_files\\music.wav")
mixer.music.play(-1)
# link https://musiclab.chromeexperiments.com/Song-Maker/song/6698332794126336

# The game can be run by executing run_game.py
# Note: This pygame uses pygame.SCALED and the vsync setting in `pygame.display.set_mode()` to aim
# to provide a better experience for different display sizes.


while running:

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

        if event.type == MOUSEBUTTONDOWN:
                ## if mouse is pressed get position of cursor ##
                print(pygame.mouse.get_pos())

    screen.fill((205-30, 205-30, 205-30))  # Fill the screen with black.

    if not ran or P.restart_level:
        loaded_level.clear()
        redirection.clear()
        data = Levels.level_process(current_level, screen)
        for i in data:
            if i[0] == 0:
                x = i
                x.insert(1, circle_wall(i[1], i[2]).circle_update)
                loaded_level.append(x)

            elif i[0] == 1:
                x = i
                i.insert(1, guard(i[1], i[2], i[3]).guard_update)
                loaded_level.append(i)

            elif i[0] == 2:
                x = i
                P.setx, P.sety = i[2]
                P.Radius = i[1]

            elif i[0] == 3:
                x = i
                i.insert(1, size_pad(i[1], i[2], i[3],
                                     i[4]).shrinking_pad_update)
                loaded_level.append(i)

            elif i[0] == 4:
                x = i
                i.insert(1, size_pad(i[1], i[2], i[3],
                                     i[4]).growing_pad_update)
                loaded_level.append(i)

            elif i[0] == 5:
                x = i
                i.insert(1, end_point(i[1], i[2], i[3]).end_point_update)
                loaded_level.append(i)
                redirection.append(i[4])
            elif i[0] == 6:
                x = i
                i.insert(1, text_box(i[1], i[2], i[3], i[4]).text_update)
                loaded_level.append(i)
                redirection.append(i[5])

            elif i[0] == 7:
                x = i
                i.insert(1, coin(i[1], i[2]).coin_update)
                loaded_level.append(i)

            elif i[0] == 8:
                x = i
                i.insert(1, radius_wall(
                    i[1], i[2], i[3], i[4]).radius_wall_update)
                loaded_level.append(i)
            elif i[0] == 9:
                x = i
                i.insert(1, jump_pad(
                    i[1], i[2], i[3]).jump_pad_update)
                loaded_level.append(i)

        ran = True
        P.set_restart(False)
        P.set_arrested(False)
        C.reset()

    list_current_level = []
    list_ran = []

    for i in loaded_level:
        if i[0] == 0:
            i[1](P)
        elif i[0] == 1:
            i[1](P, loaded_level, dt)

        elif i[0] == 3:
            i[1](P)

        elif i[0] == 4:
            i[1](P)

        elif i[0] == 5:
            var1, var2 = i[1](P)
            list_current_level.append(var1)
            list_ran.append(var2)

        elif i[0] == 6:
            var1, var2 = i[1](P)
            list_current_level.append(var1)
            list_ran.append(var2)

        elif i[0] == 7:
            i[1](P)

        elif i[0] == 8:
            i[1](P)

        elif i[0] == 9:
            i[1](P)

    if False in list_ran:
        ran = False

    for i in redirection:
        if i in list_current_level:
            current_level = i

    # draw player
    P.draw(dt)

    # Flip the display so that the things we drew actually show up.
    pygame.display.update()

    dt = fpsClock.tick(fps)

pygame.quit()
sys.exit()

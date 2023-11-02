from pico2d import *

import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
BIRD_SPEED_KMPH = 20.0
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

class Bird:
    image = None

    def __init__(self, x = 300, y = 400, velocity = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.dir = -1
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw((int(self.frame) % 5) * 182, 167 * (int(self.frame) // 5), 182, 167, self.x, self.y, 100, 100)
        elif self.dir == -1:
            self.image.clip_composite_draw((int(self.frame) % 5) * 182, 167 * (int(self.frame) // 5), 182, 167,  0, 'h',self.x, self.y,
                                 100, 100)
    def update(self):
        self.x += self.dir * BIRD_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

        if self.x < 25 or self.x > 1600 - 25:
            self.dir *= -1

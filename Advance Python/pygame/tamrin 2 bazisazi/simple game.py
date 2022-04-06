import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 320 * 2, 240 * 2
        self.speed = [1, 1]
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        self.ball, self.ballrect = self.load_image("tamrin 2 bazisazi\sq.png")

    @staticmethod
    def load_image(image_name):
        screen = pygame.image.load(image_name)
        tpl = (screen, screen.get_rect())
        return tpl

    def move_ball(self):
        ballrect = self.ballrect.move(self.speed)
        if ballrect.left < 0 or ballrect.right > self.width:
            self.speed[0] = -self.speed[0]
        if ballrect.top < 0 or ballrect.bottom > self.height:
            self.speed[1] = -self.speed[1]
        self.ballrect = ballrect

    def draw(self):
        self.screen.fill(self.black)
        self.screen.blit(self.ball, self.ballrect)
        pygame.display.update()

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


g = Game()
for i in range(10000):
    g.move_ball()
    g.draw()
    pygame.time.delay(10)
    g.handle_events()
    pygame.event.pump()

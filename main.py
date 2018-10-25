import pygame as pg
from player import *
from settings import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('platformer game')
        self.clock = pg.time.Clock()

        self.running = True
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.all_sprites.add(self.player)
        self.run()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def updates(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.updates()
            self.draw()

    def main(self):
        while self.running:
            self.new()


    def __del__(self):
        pg.quit()

g = Game()
g.main()

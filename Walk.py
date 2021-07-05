import pygame
import sys
import os


pygame.init()
clock = pygame.time.Clock()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Walking")



class Walk(pygame.sprite.Sprite):
    def __init__(self, px, py):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for sprite in os.listdir('Assets'):
            if sprite.endswith('.png') and sprite.startswith('Walk'):
                self.sprites.append(pygame.image.load(os.path.join('Assets',sprite)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [px, py]

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]


def main():
    moving_sprites = pygame.sprite.Group()
    walk = Walk(150, 125)
    moving_sprites.add(walk)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                walk.animate()
        screen.fill((0, 0, 0))
        moving_sprites.draw(screen)
        moving_sprites.update()
        pygame.display.flip()
        clock.tick(5)

if __name__ == '__main__':
    main()

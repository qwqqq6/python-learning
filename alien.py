import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像与碰撞体
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #创建外星人位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """当位于屏幕边缘返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
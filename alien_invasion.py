import sys
import pygame

from setting import Settings

def run_game():
    # 初始化
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #重绘屏幕
        screen.fill(ai_settings.bg_color)

        # 最近绘制屏幕可见
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
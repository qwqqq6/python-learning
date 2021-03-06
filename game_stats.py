class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏初始化处于活动状态
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit

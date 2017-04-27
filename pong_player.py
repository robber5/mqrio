"""Simple Pong Player for testing Deep Q logic."""
import pygame.constants as pgc
from PyGamePlayer.pygame_player import PyGamePlayer
from learner.qlearn import DeepQLearner

# Possible actions for Pong. Last one is equivalent to "do noting."
ACTIONS = [pgc.K_DOWN, pgc.K_UP, pgc.K_UNKNOWN]

class PongPlayer(PyGamePlayer):
    def __init__(self, force_game_fps=10, run_real_time=False):
        """
        Example class for playing Pong
        """
        super(PongPlayer, self).__init__(force_game_fps=force_game_fps, run_real_time=run_real_time)
        self.last_bar1_score = 0.0
        self.last_bar2_score = 0.0
        self.dql = DeepQLearner(ACTIONS)

    def get_keys_pressed(self, screen_array, feedback, terminal):
        return self.dql.step(screen_array, feedback, terminal)

    def get_feedback(self):
        # import must be done here because otherwise importing would cause the game to start playing
        from games.pong.pong import bar1_score, bar2_score

        # get the difference in score between this and the last run
        score_change = (bar1_score - self.last_bar1_score) - (bar2_score - self.last_bar2_score)
        self.last_bar1_score = bar1_score
        self.last_bar2_score = bar2_score

        return float(score_change), score_change != 0

    def start(self):
        super(PongPlayer, self).start()
        import games.pong.pong


if __name__ == '__main__':
    player = PongPlayer()
    player.start()
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast[constants.BALL][0]
        ball_v = ball.get_velocity()
        ball_x = ball.get_position().get_x()
        ball_y = ball.get_position().get_y()
        ball_next_x = ball_x + ball_v.get_x()
        ball_next_y = ball_y + ball_v.get_y()

        paddle = cast[constants.PADDLE][0]
        paddle_x = paddle.get_position().get_x()
        paddle_y = paddle.get_position().get_y()
        paddle_l = len(paddle.get_text())

        score = cast[constants.SCORE][0]
        score_n = score.get_text().split(':')
        score_n = score_n[1].lstrip()
        score_n = int(score_n)

        #1 if ball collide with paddle
        if (ball_next_y == paddle_y) and (ball_x >= paddle_x and ball_x <= paddle_x + paddle_l):
            ball.set_velocity(Point(ball_v.get_x(), ball_v.get_y() * -1))
        #2 if ball collide with side wall
        elif (ball_next_x == 0) or (ball_next_x == constants.MAX_X - 1):
            ball.set_velocity(Point(ball_v.get_x() * -1, ball_v.get_y()))
        #3 if ball collide with top, same with #1
        elif ball_y == 1:
            ball.set_velocity(Point(ball_v.get_x(), ball_v.get_y() * -1))
        #4 if ball colide with bottom
        elif ball_next_y == paddle_y + 1:
            ball.set_velocity(Point(ball_v.get_x(), ball_v.get_y() * -1))
            score_n = score_n - 5
        #5 if ball collide with brick
        else:
            for brick in cast[constants.BRICK]:
                # collide with bottm or top of brick
                if brick.get_position().equals(Point(ball_x, ball_next_y)):
                    ball.set_velocity(Point(ball_v.get_x(), ball_v.get_y() * -1))
                    score_n = score_n + 1
                    cast[constants.BRICK].remove(brick)
                    break
                #collide with side of brick
                elif brick.get_position().equals(Point(ball_next_x, ball_y)):
                    ball.set_velocity(Point(ball_v.get_x() * -1, ball_v.get_y()))
                    score_n = score_n + 1
                    cast[constants.BRICK].remove(brick)
                # collide with diagonal
                elif brick.get_position().equals(Point(ball_next_x, ball_next_y)):
                    ball.set_velocity(ball_v.reverse())
                    score_n = score_n + 1
                    cast[constants.BRICK].remove(brick)
        score.set_text("Score: " + str(score_n))
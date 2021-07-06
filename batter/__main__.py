from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    # create paddle
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    paddle = Actor() 
    paddle.set_text(constants.PADDLE_SHAPE) # ===========
    paddle.set_position(position)
    cast[constants.PADDLE] = [paddle]

    # create brick
    cast[constants.BRICK] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Actor()
            brick.set_text(constants.BRICK_SHAPE) # *
            brick.set_position(position)
            cast[constants.BRICK].append(brick)

    # create ball
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, -1)
    ball = Actor()
    ball.set_text(constants.BALL_SHAPE) # @
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast[constants.BALL] = [ball]

    # set score
    x = 0
    y = constants.MAX_Y
    position = Point(x, y)
    velocity = Point(0, 0)
    score = Actor()
    score.set_text("Score: 1")
    score.set_position(position)
    score.set_velocity(velocity)
    cast[constants.SCORE] = [score]
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)
from time import sleep
from game import constants
import pyfiglet

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self.get_score(self._cast[constants.SCORE][0].get_text()) > 0:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)
        print(pyfiglet.figlet_format("L O S E !"))

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)
            
    def get_score(self, score):
        """get score(int) from score(string)
        
        Args:
            score (string): The score(string)
        
        Return:
            score (int): score of the game
        """ 


        temp = score.split(':') 
        return int(temp[1].lstrip())
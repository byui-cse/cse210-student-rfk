from game.action import Action

# TODO: Define the DrawActorsAction class here

class DrawActorsAction(Action): # when called in __main__ the paramater is output_service
    """This class will draw the actors and their action. This class overides the Action class execute.
    
    Attributes:
        _output_service"""

    def __init__(self, output_service):
        """ This module starts the class
        
        args: 
            output_service
            """
        self._output_service = output_service
    def execute(self, cast):
        """gets the function from Action and chagnes it
        
            args:
                cast: a dictionary the has the actor as the key and it's list.
                
        """
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()

# needs to overide the Action class def execute(self, cast):

# needs an attribute called output_service(an instance of output_service)
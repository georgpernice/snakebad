from commands import CommandCreator

class Player():
    """Represent a player in the game."""
    # TODO use this to keep track of state correctly.
    def __init__(self, id, name):
        self.name = name
        self.dead = False
        self.id = id
    def die(self):
        self.dead = True

class Agent():
    """Encapsulate all of the agents logic."""
    def __init__(self, socket):
        self.name = "Default Agent"
        self.cc = CommandCreator(socket)

    def _motd(self):
        self.cc.join()
    def _on_new_game(self, w, h, id):
        self.cc.chat(self.name + " has ID: " + id)

    
    def act(self, event, args):
        """Choose an action depending on the last server msg."""
        if event == "motd":
            self._motd()
        elif event == "tick":
            self.cc.up()
        elif event == "game":
            width, height, id = args
            self._on_new_game(width,height,id)
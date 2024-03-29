from commands import CommandCreator

class Player():
    """Represent a player in the game."""
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
        self.dead = False
        # Creates a list containing 5 lists, each of 8 items, all set to 0
        self.players = []
        self.mapsize = 6 # very likely 4 
        self.map = [[0 for x in range(self.mapsize)] for y in range(self.mapsize)] 
        self.HADES_ID = 99
    def _signup_player(self, id, name):
        self.players.append(Player(id=id, name=name))
    def _tick(self):
        self.cc.up()
    def _motd(self):
        self.cc.join()
        self.dead == False
    def _game(self, w, h, id):
        self.cc.chat(self.name + " has ID: " + id)
        self.mapsize = w
    def _write_pos2map(self, player_id, x, y):
        """Enter a pos update to the map."""
        x, y = int(x), int(y)
        self.map[x][y] == player_id
    def _update_map_on_death(self, dying_id):
        """Purge the map of entries regarding a recently dead player."""
        for x in range(self.mapsize):
            for y in range(self.mapsize):
                id = self.map[x][y]
                if id == dying_id:
                    self.map[x][y] = self.HADES_ID
    def act(self, event, args):
        """Choose an action depending on the last server msg."""
        if event == "motd":
            self._motd()
        elif event == "tick":
            self._tick()
        elif event == "game":
            width, height, id = args
            self._game(width,height,id)
        elif event == "pos":
            player, x, y = args
            self._write_pos2map(player, x, y)
        elif event == "die":
            for player in self.players:
                for dead_id in args:
                    if player.id == dead_id:
                        player.die()
    

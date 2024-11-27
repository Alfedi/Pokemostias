import numpy as np


class Node():

    def __init__(self, gamestate, winner, team, parent):
        # Children Nodes
        self.children = None
        # Número de victorias
        self.w = 0
        # Número de simulaciones
        self.n = 0
        # Gamestate
        self.gamestate = gamestate
        # Is it winner? True | False
        self.winner = winner
        # Link to parent node
        self.parent = parent
        # Team
        self.team = team


    def __getitem__(self, item):
        return self.gamestate[item]

    def get_team(self):
        return self.team
    # @property
    # def children(self):
    #     return self.children
    
    # @children.setter
    # def children(self, children):
    #     self.children = children

    # @property
    # def w(self):
    #     return self.w
    
    # @w.setter
    # def w(self, w):
    #     self.w = w

    # @property
    # def n(self):
    #     return self.n

    # @n.setter
    # def n(self, n):
    #     self.n = n
        
    # @property
    # def gamestate(self):
    #     return self.gamestate
    
    # @gamestate.setter
    # def gamestate(self, gamestate):
    #     self.gamestate = gamestate
        
    # @property
    # def winner(self):
    #     return self.winner
    
    # @winner.setter
    # def winner(self, winner):
    #     self.winner = winner
        
    # @property
    # def parent(self):
    #     return self.parent
    
    # @parent.setter
    # def parent(self, parent):
    #     self.parent = parent
    
    # @property
    # def team(self):
    #     return self.team

    # @team.setter
    # def team(self, team):
    #     self.team = team

    def set_children(self, child):
        self.children = child

    def get_uct_score(self):
        c = np.sqrt(2)
        # Los nodos que no se han explorado tienen un valor máximo para favorecer la exploración
        if self.n == 0:
            return None

        return (self.w / self.n) + c * np.sqrt(
            np.log(self.parent.n) / self.n
        )  # Fórmula mágica de los apuntes

    def next_team(self):
        if self.children is None:
            return None, None

        winners = [child for child in self.children if child.winner]
        if len(winners) > 0:
            return winners[0], winners[0].team

        games = [child.w / child.n if child.n > 0 else 0 for child in self.children]
        best = self.children[np.argmax(games)]
        return best, best.team

    def get_children_with_team(self, move):
        if self.children is None:
            return None
        for child in self.children:
            if child.move == move:
                return child

        raise Exception('Not existing child')
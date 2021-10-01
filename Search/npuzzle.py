import math
import matplotlib.pyplot as plt


class NPuzzleState:
    
    def __init__(self, N=8, tiles=None):
        if tiles is None:
            self.tiles = tuple(range(N + 1))  # [0, 1, 2, ..., N] and 0 is blank
        else:
            N = len(tiles) - 1
            self.tiles = tuple(tiles[:])
        
        self.N = N
        self.grid_size = int(math.sqrt(N + 1))  # for 8-puzzle, this is 3x3
            
    def successors(self):
        ''' Returns a list of possible actions, their costs and their resulting states.
        '''
        
        blank_idx = self.tiles.index(0)
        successors = []
        
        # left
        if blank_idx % self.grid_size > 0:
            tiles = list(self.tiles)
            tiles[blank_idx], tiles[blank_idx - 1] = tiles[blank_idx - 1], tiles[blank_idx]
            successor = NPuzzleState(tiles=tiles)
            successors.append((successor, 'Left', 1))
        
        # up
        if blank_idx >= self.grid_size:
            tiles = list(self.tiles)
            tiles[blank_idx], tiles[blank_idx - self.grid_size] = tiles[blank_idx - self.grid_size], tiles[blank_idx]
            successor = NPuzzleState(tiles=tiles)
            successors.append((successor, 'Up', 1))
        
        # right
        if blank_idx % self.grid_size < self.grid_size - 1:
            tiles = list(self.tiles)
            tiles[blank_idx], tiles[blank_idx + 1] = tiles[blank_idx + 1], tiles[blank_idx]
            successor = NPuzzleState(tiles=tiles)
            successors.append((successor, 'Right', 1))
            
        # down
        if blank_idx + self.grid_size < len(self.tiles):
            tiles = list(self.tiles)
            tiles[blank_idx], tiles[blank_idx + self.grid_size] = tiles[blank_idx + self.grid_size], tiles[blank_idx]
            successor = NPuzzleState(tiles=tiles)
            successors.append((successor, 'Down', 1))
        
        return successors
    
    def is_goal(self, goal_state):
        return self == goal_state
    
    def plot(self, ax=None, title=None, fs=20):
        if ax is None:
            _, ax = plt.subplots(1)
            
        gs = self.grid_size
        
        # draw border
        border = plt.Rectangle((0, 0), gs, gs, ec='k', fc='w', lw=3)
        ax.add_patch(border)
        
        # draw tiles
        for i, tile in enumerate(self.tiles):
            if tile == 0: continue
            col = self.grid_size - 1 - i // self.grid_size
            row = i %  self.grid_size
            cell = plt.Rectangle((row, col), 1, 1, fc='darkslateblue', ec='k', lw=3, alpha=0.4)
            ax.add_patch(cell)
            tileSq = plt.Rectangle((row + 0.15, col + 0.15), 0.7, 0.7, fc='darkslateblue', ec='k', lw=1, alpha=0.8)
            ax.add_patch(tileSq)
            ax.text(row + 0.5, col + 0.5, f"{tile}", color='w', fontsize=fs, va='center', ha='center')
        
        ax.axis('square')
        ax.axis('off')
        if title:
            ax.set_title(title, fontsize=fs)
            
    def __hash__(self):
        return hash(self.tiles)
    
    def __eq__(self, other):
        if self is other: return True  # True object equallity test for efficiency
        if other is None: return False
        if not isinstance(other, NPuzzleState): return False
        
        return self.tiles == other.tiles
    
    def __str__(self):
        """ An string representation of the tiles configuration in 2d format.
        """
        result = ''
        for i in range(len(self.tiles)):
            result += f' {self.tiles[i]:2d} ' if self.tiles[i] != 0 else '    '
            if i % self.grid_size == self.grid_size - 1 and i < self.N:
                result += '\n'
        return result
    
    def __repr__(self):
        return f'NPuzzleState(N={self.N}, tiles={self.tiles})'
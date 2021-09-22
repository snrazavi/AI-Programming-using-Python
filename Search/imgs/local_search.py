class HillClimbing:
    
    def __init__(self):
        self.history = []
        
    def search(self, state, verbose=0):
        current = state
        
        while True:
            if verbose == 1: print(current)
            elif verbose == 2: current.plot(show_conflicts=False)
            elif verbose == 3: current.plot(show_conflicts=True)
            self.history.append(current)

            neighbor = current.best_neighbor()
            if neighbor >= current: return current
            current = neighbor
    
    def __call__(self, state, verbose=0):
        self.search(state, verbose)        
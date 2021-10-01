import math
import time
import heapq, random

import matplotlib.pyplot as plt


def timed(f, *args, **kwargs):
    ''' Decorator function for search algorithms which computes time required for searching'''
    
    start_time = time.time()
    sol = f(*args, **kwargs)
    execution_time = time.time() - start_time
    return execution_time, sol


def print_solution(start_state, path):
    if not isinstance(path, list):
        print("No solution found!")
        return
    
    print(start_state)
    for state, action in path:
        print("\n {} \n".format(action))
        print(state)


def show_solution(start_state, path, ncols=5, fs=18):
    if not isinstance(path, list):
        print("No solution found!")
        return
    
    N = len(path) + 1
    nrows = int(math.ceil(N / ncols))
    
    fig, axes = plt.subplots(nrows, ncols, figsize=(3 * ncols, 3 * nrows))
    
    if nrows > 1:
        start_state.plot(axes[0][0], 'start', fs)
        for i, (state, action) in enumerate(path):
            state.plot(axes[(i + 1) // ncols][(i + 1) % ncols], action, fs)
        for i in range(N, nrows * ncols):
            axes[nrows-1][i % ncols].axis('off')
    
    else:
        start_state.plot(axes[0], 'start', fs)
        for i, (state, action) in enumerate(path):
            state.plot(axes[i + 1], action, fs)
        for i in range(N, ncols):
            axes[i].axis('off')


def solution(node):
    path = []
    while node.parent is not None:
        path = [(node.state, node.action)] + path
        node = node.parent
    return path


def manhatan_distance(tile, state1, state2):
    i = state1.tiles.index(tile)
    j = state2.tiles.index(tile)
    
    gs = state1.grid_size
    
    row_i, col_i = i // gs, i % gs
    row_j, col_j = j // gs, j % gs
    
    return abs(row_i - row_j) + abs(col_i - col_j)


"""
 Data structures useful for implementing Search Strategies
"""

class Stack:
    def __init__(self, items=None):
        self._items = []
        
        if items:
            for item in items:
                self.push(item)
    
    def push(self, item):
        '''Add to the end'''
        self._items.append(item)
    
    def pop(self):
        '''Remove from end'''
        try:
            item = self._items.pop()
            return item
        except:
            print('ERROR! trying to pop an element from an empty stack.')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __repr__(self):
        return f'Stack(items={self._items})'
    
    def __str__(self):
        return f"[{', '.join(self._items)}]"
    

class Queue:
    def __init__(self, items=None):
        self._items = []
        
        if items:
            for item in items:
                self.push(item)
    
    def push(self, item):
        '''Add to the rear'''
        self._items.append(item)
    
    def pop(self):
        '''Remove from front'''
        try:
            item = self._items[0]
            self._items = self._items[1:]
            return item
        except:
            print('ERROR! trying to pop an element from an empty queue.')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __repr__(self):
        return f'Queue(items={self._items})'
    
    def __str__(self):
        return f"[{', '.join(self._items)}]"
    

class PriorityQueue:
    ''' Min Priority Queue '''
    
    def __init__(self, items=None):
        self._items = []
        self.index = 0
        
        if items:
            for item, priority in items:
                self.push(item, priority)
        
    def push(self, item, priority):
        '''Add to the rear'''
        entry = (priority, self.index, item)
        heapq.heappush(self._items, entry)
        self.index += 1
    
    def pop(self):
        '''Remove the item with highest priority'''
        try:
            _, _, item = heapq.heappop(self._items)
            return item
        except:
            print('ERROR! trying to pop an element from an empty priority queue.')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __repr__(self):
        return f'PriorityQueue(items={self._items})'
    
    def __str__(self):
        res = '['
        for priority, _, item in self._items:
            res += f' {item}({priority}) '
        res += ']'
        return res
# path_planning_a_star.py

import heapq
import numpy as np

def heuristic(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def a_star(grid, start, goal):
    """
    Implements A* algorithm for path planning.
    """
    neighbors = [(0,1), (1,0), (0,-1), (-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    open_set = []
    heapq.heappush(open_set, (fscore[start], start))
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        close_set.add(current)
        
        for i, j in neighbors:
            neighbor = (current[0] + i, current[1] + j)
            if neighbor in close_set or grid[neighbor[0]][neighbor[1]] == 1:
                continue
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if neighbor not in gscore or tentative_g_score < gscore[neighbor]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (fscore[neighbor], neighbor))
    
    return []

if __name__ == "__main__":
    grid = np.zeros((10, 10))
    start = (0, 0)
    goal = (9, 9)
    path = a_star(grid, start, goal)
    print("Planned Path:", path)

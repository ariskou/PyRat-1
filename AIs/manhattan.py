##############################################################
# The turn function should always return a move to indicate where to go
# The four possibilities are defined here
##############################################################

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'



##############################################################
# Please put your code here (imports, variables, functions...)
##############################################################

def distance (la, lb) :

    # Manhattan distance
    ax, ay = la
    bx, by = lb
    return abs(bx - ax) + abs(by - ay)



##############################################################
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################

def preprocessing (maze_map, maze_width, maze_height, player_location, opponent_location, pieces_of_cheese, time_allowed) :
    
    # Nothing to do here
    pass



##############################################################
# The turn function is called each time the game is waiting
# for the player to make a decision (a move).
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# player_score : float
# opponent_score : float
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################

def turn (maze_map, maze_width, maze_height, player_location, opponent_location, player_score, opponent_score, pieces_of_cheese, time_allowed) :
    
    # Greedy approach
    closest_poc = (-1, -1)
    best_distance = maze_width + maze_height
    for poc in pieces_of_cheese :
        if distance(poc, player_location) < best_distance :
            best_distance = distance(poc, player_location)
            closest_poc = poc
    
    # Associated move
    ax, ay = player_location
    bx, by = closest_poc
    if bx > ax :
        return MOVE_RIGHT
    elif bx < ax :
        return MOVE_LEFT
    elif by > ay :
        return MOVE_UP
    else :
        return MOVE_DOWN


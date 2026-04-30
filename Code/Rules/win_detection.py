# function to check hand for a win

def can_form_sets(vec):
    '''Checks if 4 sets can be formed as in the win condition
    This is used to check hidden tiles'''

    # find first non-zero tile
    for i in range(34):
        if vec[i] > 0:
            break
    else:
        return True

    # Pung
    if vec[i] >= 3:
        vec[i] -= 3
        if can_form_sets(vec):
            return True
        vec[i] += 3

    # Chow
    if i < 27 and i % 9 <= 6:
        if vec[i+1] > 0 and vec[i+2] > 0:
            vec[i] -= 1
            vec[i+1] -= 1
            vec[i+2] -= 1

            if  can_form_sets(vec):
                return True

            vec[i] += 1
            vec[i+1] += 1
            vec[i+2] += 1

    return False


def can_thirteen_orphans(vec):
    '''Checks for the 13 orphans set'''

    peices = [0,8,9,17,18,26,27,28,29,30,31,32,33]
    p_check = False
    for i in peices:
        if vec[i] == 0:
            return False
        elif vec[i] == 2:
            p_check = True
    
    return p_check
        
        


def is_win(vec):
    '''Checks hand for a win, used for hidden tiles'''

    for i in range(34):
        if vec[i] >= 2:
            vec[i] -= 2 

            if can_form_sets(vec):
                vec[i] += 2
                return True

            vec[i] += 2

    return can_thirteen_orphans(vec)
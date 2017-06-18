assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

from utils import *

def find_twins(values):
    """Find boxes that satisfy the naked twins criteria.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns
        twins(list): a list containing tuples of twins
    """
    twos = [x for x in values.keys() if len(values[x])==2]
    twins = [(x,y) for x in twos for y in peers[x] if values[x]==values[y]]
    return twins
    
def eliminate_twins(values, twins):
    """For boxes from twins, eliminate their values from their peers in "values"
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
        twins(list): a list containing tuples of twins
    Return:
        the values dictionary with the naked twins eliminated from peers.
    """
    for pair in twins:
        digits = values[pair[0]]
        for peer in peers[pair[0]]:
            if peer not in pair and peer in peers[pair[1]]:
                values = assign_value(values, peer, values[peer].replace(digits[0],"").replace(digits[1],""))
    return values
    
def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    twins=find_twins(values)
    # Eliminate the naked twins as possibilities for their peers
    values = eliminate_twins(values,twins)
    return values
     
def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    # Sanity check length
    assert len(grid)==81, "The grid must be 9 by 9."
    # Create dict of boxes
    original = dict(zip(boxes,grid))
    # Fill in periods with naive possible options
    for key in original.keys():
        if original[key]=='.':
            original[key]='123456789'
    return original

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    '''
    Eliminate possibilities if peers conflict.
    '''
    # Compile solved squares
    solved_values=[x for x in values.keys() if len(values[x])==1]
    # Eliminate values if a peer has that value
    for x in solved_values:
        digit=values[x]
        for y in peers[x]:
            values = assign_value(values, y, values[y].replace(digit,""))
    return values

def only_choice(values):
    '''
    Checks to see if values are sufficient.
    '''
    for unit in unitlist:
        for digit in '123456789':
            # Get list of boxes per unit that have digit as possible value
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces)==1:
                # Fill in if only possible choice
                values = assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):
    '''
    Combine eliminate and only_choice to get as far as possible towards solution.
    Easier puzzles will be solved, harder puzzles will require search
    '''
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Eliminate using implemented heuristics
        values = eliminate(values)
        values = naked_twins(values)
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    '''
    Use DFS to search possible solutions if reduce_puzzle does not solve.
    '''
    values = reduce_puzzle(values)
    # Check to see if any squares have no possible value.
    if values is False:
        return False
    # Check to see if puzzle is solved. Check 1
    if all(len(values[s])==1 for s in boxes):
        return values
    # Choose square with minimum number of immediate branches.
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Main DFS loop.
    # Recursively call search  for each immediate branch of box s until Check 1 is satisfied, 
    # i.e. solution has been found.
    for value in values[s]:
        new_sudoku=values.copy()
        new_sudoku = assign_value(new_sudoku,s,value)
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)
    
    
if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

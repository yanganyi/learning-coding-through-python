## Solve Every Sudoku Puzzle

## See http://norvig.com/sudoku.html

## A1 A2 A3| A4 A5 A6| A7 A8 A9    4 . . |. . . |8 . 5     4 1 7 |3 6 9 |8 2 5 
## B1 B2 B3| B4 B5 B6| B7 B8 B9    . 3 . |. . . |. . .     6 3 2 |1 5 8 |9 4 7
## C1 C2 C3| C4 C5 C6| C7 C8 C9    . . . |7 . . |. . .     9 5 8 |7 2 4 |3 1 6 
##---------+---------+---------    ------+------+------    ------+------+------
## D1 D2 D3| D4 D5 D6| D7 D8 D9    . 2 . |. . . |. 6 .     8 2 5 |4 3 7 |1 6 9 
## E1 E2 E3| E4 E5 E6| E7 E8 E9    . . . |. 8 . |4 . .     7 9 1 |5 8 6 |4 3 2 
## F1 F2 F3| F4 F5 F6| F7 F8 F9    . . . |. 1 . |. . .     3 4 6 |9 1 2 |7 5 8 
##---------+---------+---------    ------+------+------    ------+------+------
## G1 G2 G3| G4 G5 G6| G7 G8 G9    . . . |6 . 3 |. 7 .     2 8 9 |6 4 3 |5 7 1 
## H1 H2 H3| H4 H5 H6| H7 H8 H9    5 . . |2 . . |. . .     5 7 3 |2 9 1 |6 8 4 
## I1 I2 I3| I4 I5 I6| I7 I8 I9 

## Throughout this program we have:
##   r is a row,    e.g. 'A'
##   c is a column, e.g. '3'
##   s is a square, e.g. 'A3'
##   d is a digit,  e.g. '9'
##   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
##   grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
##   values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)    # square is the 'cell' in my language

# the complete list of all rows (9), columns (9), and blocks (9) i.e. [ []]
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
# every square is mapped to exactly 3 units. assignment of one square is propagated to all 3 units            
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)  # we create a mapping s->list for every square
# flatten the squares in all 3 units of a given sqaure. squares are unioned and take away the square itself
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

################ Unit Tests ################

def test():
    "A set of tests that must pass."
    assert len(squares) == 81

    # every column, every row, every block is in unitlist
    assert len(unitlist) == 27
    assert ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'] in unitlist
    assert ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'] in unitlist
    assert ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'] in unitlist

    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print('All tests pass.')


################ Parse a Grid ################

# values are the grid/matrix containing all the possibilities, which will get reduced to the final solution of a puzzle

# parse a grid to a dict 'values'
def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    print('debug parse_grid beginning',grid)
    # to start, every square can be any digit; then assign values from the grid.
    # this is {'A1': '123456789', 'A2': '123456789', ... }
    values = dict((s, digits) for s in squares)
    print('debug parse_grid init',values)
    
    # s->d pairs are our best knowledge so far for a given puzzle
    # we try to assign d to square s, we assume this assignment will work
    # if not, such grid is invalid, we return false
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    print('debug parse_grid post',values)
    return values

# given a long grid string representation, zip it with sqaures, that is to mark every single input data onto every square on the board
# sample input: '.....6....59.....82....8....45........3........6..3.54...325..6..................'
# sample return: {'A1': '.', 'A2': '.', 'A3': '.', 'A4': '.', 'A5': '.', 'A6': '6', ... }
def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    #if len(chars) != 81: print(grid, chars, len(chars))
    assert len(chars) == 81
    print('debug grid_values dict of zip(squares,inputChar)',dict(zip(squares, chars)))
    return dict(zip(squares, chars))


################ Constraint Propagation ################

# for square s, there are possible candiates of d and all other digits x
# we eliminate all x, thus only keep d, effectively assign d to square s
# if for any reason, we cann't assign, we return false, signaling that such assignment attempt is invalid, discarding this potential partial solution
def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

# we want to eliminate d from candidate values of square s
def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""

    # d is already eliminated prior to this call, do nothing
    if d not in values[s]:
        return values ## Already eliminated
    
    # we look at the remaining candidate values of square s
    values[s] = values[s].replace(d,'')

    ## (original comment) strategy (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.

    # if the remaining candidate set is empty, this is not a valid solution, return false
    if len(values[s]) == 0:
        return False
    # if we have the last candidate in the set, this is the solution for this square, we then go to eliminate this digit 
    # from all peers of this square. anywhere in this propagation chain there is an error, we will consider the solution to be invalid
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    
    ## (original comment) strategy (2) If a unit u is reduced to only one place for a value d, then put it there.

    # for this given square s, consider its row, its column and its big block -> u
    for u in units[s]:
        # for every square in the current u (i.e. current row, current column, current block)
        # if we find digit d is a possible value for this square, we put it in dplaces
        # for example, we try to find a digit 5 is at which square of this row
        # if there is no square can hold 5, we discard this solution
        # if there is only one square can hold 5, we directly assign 5 to this square
        # all other conditions, we do nothing and continue checking
        # basically we need to check for all 3 cases, ROW/COLUMN/BLOCK. it should not fail on any one of them
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values

################ Display as 2-D grid ################

def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print()

################ Search ################

def solve(grid): return search(parse_grid(grid))

# pick a square s, assign d to s, perform a recursive search call
# if the child search() returns a False, the calling parent discard the solution
# if the child search() returns a non-false value, i.e. (partial) solution, return it to the calling function (grandparent)
# so each generation, or each level in the depth-first search solves one square
# because the constraint propagation is pretty powerful, it is farily quickly to reach the end of the tree or fail early
def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    for d in values[s]:
        result = search(assign(values.copy(), s, d))
        if result: return result

################ System test ################

import time

def solve_all(grids, name=''):
    """Attempt to solve a sequence of grids. Report results."""
    times, results = zip(*[time_solve(grid) for grid in grids])
    N = len(results)
    if N >= 1:
        print("Solved %d of %d %s puzzles (avg %.2f secs (%d Hz), max %.2f secs)." % (
            sum(results), N, name, sum(times)/N, N/sum(times), max(times)))
            
def time_solve(grid):
    start = time.time()
    values = solve(grid)
    t = time.time()-start
    print('debug i solved this puzzle')
    display(values) # for human
    #print(values)  # for machine
    return (t, solved(values))

def solved(values):
    "A puzzle is solved if each unit is a permutation of the digits 1 to 9."
    def unitsolved(unit): return set(values[s] for s in unit) == set(digits)
    return values is not False and all(unitsolved(unit) for unit in unitlist)


grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid2  = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
hard1  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'
    
if __name__ == '__main__':
    test()

    grid0 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300' # easy puzzle, takes less than a second
    grid0 = '800000000003600000070090200050007000000045700000100030001000068008500010090000400' # easy for computer, hard for human, takes less than a second
    #grid0 = '.....6....59.....82....8....45........3........6..3.54...325..6..................' # hard puzzle, takes about 1 minute plus
    
    solve_all([grid0],"try")

    #solve_all(open("sudoku-easy50.txt"), "easy")
    #solve_all(open("sudoku-top95.txt"), "hard")
    #solve_all(open("sudoku-hardest.txt"), "hardest")
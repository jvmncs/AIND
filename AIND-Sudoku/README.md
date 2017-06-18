# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: We implemented a function that checks for naked twins and eliminates twinning values in peers of both of the naked twins.  Naked twins occur when two boxes in a unit (a row, column or 3x3 subregion) have only two possible values and those values are the same for both boxes.  When naked twins occur, we can eliminate their two values from other boxes in that unit, i.e. boxes that are peers of the twinning boxes.  When we eliminate these values, we are effectively propagating more constraints throughout the values dictionary.  This solves the naked twins problem.  The naked twins strategy speeds up the solving of the Sudoku by eliminating more squares before the search function is applied.  Since the search function is essentially a brute force method of guess and check, most of the time in the solving is applied there.  By limiting our use of the search function, we speed up the program as a whole.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: A diagonal sudoku is similar to a regular sudoku, except that new constraints are added that prevent squares on the two main diagonals from having values in common.  In order to solve a diagonal sudoku, we simply add the diagonal units to the unitlist, which is the list of all units in the sudoku.  Since the constraints for each square are updated based on the units within unitlist, any constraints coming from the new diagonal units will automatically be propagated to the rest of the boxes according to the eliminate, naked\_twins, and only\_choice functions.  This solves the diagonal sudoku problem.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.

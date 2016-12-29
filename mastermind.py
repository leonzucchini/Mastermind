"""
A program for solving mastermind puzzles (without repeating colors!)
Uses Knuth's 1977 algorithm as described on Wiki
https://en.wikipedia.org/wiki/Mastermind_(board_game)
"""

import itertools
# import random
# import pandas as pd
# import numpy as np

class game(object):
    """Game object with all permutations, a solution, and storage for turns. """

    def __init__(self, colors, num_positions, solution_sequence):
        """Generate all possible color permutations (witout repeating). Define solution. """

        # Generate all possible permutations of colors for positions
        self.permutations = [p[0:num_positions] for p in list(itertools.permutations(colors))]
        self.permutations.sort()
        list(p for p, _ in itertools.groupby(self.permutations)) # Remove duplicates
        self.num_permutations = len(self.permutations)

        # Define solution
        self.solution_sequence = solution_sequence
        self.solution_score = calc_score(self.solution_sequence, self.solution_sequence)

def calc_score(sequence, solution_sequence):
    """Test a sequence against a solution.
    n_black =  Number of black responses (correct color and position)
    n_white =  Number of white responses (correct color, wrong position)
    """
    n_black = sum([sequence[i] == solution_sequence[i] for i in range(0, len(sequence))])
    n_correct_col = len(list(set(sequence) & set(solution_sequence))) # Number of correct colors
    n_white = n_correct_col - n_black
    return (n_black, n_white)

# class guess(object):
#     """Guess for correct sequence incl. score. """

#     def __init__(self, sequence):
#         """Initiate guess. """
#         self.sequence = sequence

#     def score_guess(self, solution, verbose=False):
#         """Score guess against solution. """
#         self.score = calc_score(self.sequence, sequence)

#         if verbose:
#             print solution.sequence, self.sequence], axis=1).transpose()
#             print self.score

#         return self.score

# class answer_set(object):
#     """Set of potentially correct answers incl. scoring against a guess. """

#     def __init__(self, initial_set):
#         """Initiate answer_set object. """

#         self.initial_set = initial_set # Initial set of potential answers pd.df
#         self.initial_n = initial_set.shape[0] # N obs in initial set
#         self.scores = pd.DataFrame({'nb' : [], 'nw' : []}) # Scores against a guess

#     def score_for_guess(self, guess):
#         """Score answer set against a guess. """

#         for index, row in self.initial_set.iterrows():
#             self.scores.set_value(index, 'nb', calc_score(row, guess.sequence)[0])
#             self.scores.set_value(index, 'nw', calc_score(row, guess.sequence)[1])
#         return self.scores

#     def get_compatible_set(self, guess, score):
#         """Given a guess and a score, return compatible_set = all solutions in the initial set that are consistent that pattern. """

#         self.compatible_set = pd.DataFrame()
#         self.score_for_guess(guess)
#         for index, row in self.scores.iterrows():
#             if sum(row == score) == 2:
#                 self.compatible_set = self.compatible_set.append(self.initial_set.iloc[index], ignore_index=True)
#         self.compatible_n = self.compatible_set.shape[0]
#         return self.compatible_set
#         return self.compatible_n

#     def get_next_guess(self, this_guess, score, random_guess=False):
#         """Find the next guess with the smallest compatible set, or guess at random from compatible set. """

#         self.get_compatible_set(this_guess, score)
#         if random_guess:
#            self.new_guess = guess(self.compatible_set.iloc[random.randint(0, self.compatible_n), :])

#         # for index, row in self.compatible_set.iterrows():
#         #     pass

#         return self.new_guess


# def play(initial_set, initial_guess, solution):
#     """Play game. """

#     solution_score = solution.score_guess(solution)
#     n = initial_set.shape[0]

#     turn = 0
#     answers = answer_set(initial_set)
#     this_guess = initial_guess
#     this_score = this_guess.score_guess(solution)

#     while turn < 10:
#         if sum(this_score == solution_score) == 2:
#             print "Solved it! :)"

#         else:
#             turn += 1

#             this_guess = answers.get_next_guess(this_guess, this_score, random_guess=True)
#             this_score = this_guess.score_guess(solution)
#             answers.get_compatible_set(this_guess, this_score)

#             print "Turn: " + str(turn)
#             # print "Playing sequence: "
#             # print this_guess.sequence
#             # print "Scored: "
#             print "Score: %s" %(this_score.values)
#             print "Compatible answers: %d" %(answers.compatible_n)

#     return None

def main():
    """Initialize game and get solution. """

    # Set up game
    columns = ['R', 'G', 'B', 'P', 'Y', 'L'] #L = light blue
    num_positions = 5
    solution = ['Y', 'B', 'L', 'P', 'G']
    this_game = game(columns, num_positions, solution)


    guess = ['B', 'Y', 'L', 'G', 'R']
    # score = calc_score(guess, solution)

    # play(pos, first_turn, solution)

    # ans = answer_set(pos)
    # ans.get_next_guess(first_turn, first_score, random_guess=True)
    # print type(ans.new_guess.sequence)

    # record games

if __name__ == '__main__':
    main()

### Extensions
# 
## Game
# - Add error handling for duplicate colors in the list / too many positions
# - add posibility to randomly select solution


# ----------------------
# Knuth's algorithm
# Create the set S of 1296 possible codes (1111, 1112 ... 6665, 6666)

# Start with initial guess 1122

### Loop from here
# Play the guess to get a response of colored and white pegs.

# If the response is four colored pegs, the game is won, the algorithm terminates.

# Otherwise, remove from S any code that would not give the same response if it (the guess) were the code.

# Apply minimax technique to find a next guess as follows: 
# For each possible guess, that is, any unused code of the 1296 not just those in S, calculate how many possibilities in S would be eliminated for each possible colored/white peg score. 
# The score of a guess is the minimum number of possibilities it might eliminate from S. 
# - A single pass through S for each unused code of the 1296 will provide a hit count for each colored/white peg score found; 
# - the colored/white peg score with the highest hit count will eliminate the fewest possibilities; 
# - calculate the score of a guess by using "minimum eliminated" = "count of elements in S" - (minus) "highest hit count". 

# From the set of guesses with the maximum score, select one as the next guess, choosing a member of S whenever possible.



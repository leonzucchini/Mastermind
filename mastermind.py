"""
A program for solving mastermind puzzles (without repeating colors)
"""

import itertools
import random
import pandas

## Classes
class Game(object):
    """Game object with all permutations, a solution, and storage for turns. """

    def __init__(self, colors, num_positions, solution):
        """Generate all possible color permutations (witout repeating). Define solution. """

        # Generate set of all possible permutations of colors for positions
        self.set = [p[0:num_positions] for p in list(itertools.permutations(colors))]
        list(p for p, _ in itertools.groupby(self.set)) # Remove duplicates
        self.set = [list(p) for p in self.set] # Change list elements from tuples to lists

        # Define solution
        self.solution_sequence = solution
        self.solution_score = calculate_score(self.solution_sequence, self.solution_sequence)

class AnswerSet(object):
    """Set of potentially correct answers incl. scoring against a guess. """

    def __init__(self, initial_set):
        """Initiate answer set. """

        self.set = initial_set # Set of potential answers (list of lists)
        self.scores = []

    def get_compatible_set(self, guess):
        """Given a guess and a score, return compatible set: all consistent sequences in set. """

        # Get all answers that are compatible with guess-score pair
        new_set = []
        for seq in self.set:

            # Calculate and store score for this sequence
            this_score = calculate_score(guess.sequence, seq)
            self.scores.append(this_score)

            # If score is consistent with the last play, store sequence as compatible
            if this_score == guess.score:
                new_set.append(seq)

        # Reset answer set to reflect the new compatible set
        self.set = new_set

        return self

class Guess(object):
    """Guess for correct sequence incl. score. """

    def __init__(self, sequence, solution):

        self.sequence = sequence # Sequence of colors
        self.score = calculate_score(self.sequence, solution)

## Functions
def calculate_score(sequence, solution):
    """Test a sequence against a solution.
    n_black =  Number of black responses (correct color and position)
    n_white =  Number of white responses (correct color, wrong position)
    """
    n_black = sum([sequence[i] == solution[i] for i in range(0, len(sequence))])
    n_correct_col = len(list(set(sequence) & set(solution))) # Number of correct colors
    n_white = n_correct_col - n_black
    return (n_black, n_white)

def get_next_guess(answers, solution, random_guess=False):
    """Find next guess with smallest compatible set or guess at random. """

    if len(answers.set) == 1:
        new_guess = Guess(answers.set[0], solution)
    elif random_guess:
        new_guess = Guess(answers.set[random.randint(0, len(answers.set)-1)], solution)

    return new_guess

def print_result(answers, guess, solution):
    """Print the results for the guess. """

    print "Number of remaining alternatives: {0}".format(len(answers.set))
    print "Solution: {0}".format(solution)
    print "Guess:    {0}".format(guess.sequence)
    print "Score:    {0}".format(guess.score)

def play_game(initial_set, initial_guess, solution):
    """Play game. """
    answers = AnswerSet(initial_set)

    # First turn
    turn = 1
    guess = initial_guess

    print "Turn {0}".format(turn)
    print_result(answers, guess, solution)

    if guess.sequence == solution:
        print "Found the solution first try!"

    # Subsequent turns
    else:
        while True:
            turn += 1

            # Get compatible answers (path dependent!) and make a new guess
            answers.get_compatible_set(guess)
            guess = get_next_guess(answers, solution, random_guess=True)

            # Print results
            print "Turn {0}".format(turn)
            print_result(answers, guess, solution)

            # Check if the answer is correct
            if guess.sequence == solution:
                print "Found the solution on turn {0}!".format(turn)
                break

    return None

def main():
    """Initialize game and get solution. """

    # Set up game
    columns = ['R', 'G', 'B', 'P', 'Y', 'L'] #L = light blue
    num_positions = 5
    solution = ['R', 'P', 'G', 'B', 'Y']
    game = Game(columns, num_positions, solution)

    # Make initial guess and play game
    guess = Guess(game.set[random.randint(0, len(game.set)-1)], solution)
    play_game(game.set, guess, solution)

if __name__ == '__main__':
    main()

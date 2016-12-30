"""
A program for solving mastermind puzzles (without repeating colors)
Uses Knuth's 1977 algorithm as described on Wiki
https://en.wikipedia.org/wiki/Mastermind_(board_game)
"""

import itertools
import random
import collections

# Scoring is typically done by the keyholder
def calculate_score(sequence, solution):
    """Test a sequence against a solution.
    Note this is typically done by the keyholder (not visible for player).
    n_black =  Number of black responses (correct color and position)
    n_white =  Number of white responses (correct color, wrong position)
    """
    n_black = sum([sequence[i] == solution[i] for i in range(0, len(sequence))])
    n_correct_col = len(list(set(sequence) & set(solution))) # Number of correct colors
    n_white = n_correct_col - n_black
    return (n_black, n_white)

class Guess(object):
    """Guess for correct sequence incl. score. """

    def __init__(self, sequence, solution, verbose=False):

        self.sequence = sequence # Sequence of colors
        self.score = calculate_score(self.sequence, solution)

        if verbose:
            print self.sequence
            print solution
            print self.score

class Game(object):
    """Game object with all permutations, a solution, and storage for turns. """

    def __init__(self, colors, num_positions, solution):
        """Generate all possible color permutations (witout repeating). Define solution. """

        # Generate set of all possible permutations of colors for positions
        self.set = [p[0:num_positions] for p in list(itertools.permutations(colors))]
        self.set.sort()
        list(p for p, _ in itertools.groupby(self.set)) # Remove duplicates
        self.n = len(self.set)

        # Define solution
        self.solution_sequence = solution
        self.solution_score = calculate_score(self.solution_sequence, self.solution_sequence)

class AnswerSet(object):
    """Set of potentially correct answers incl. scoring against a guess. """

    def __init__(self, initial_set):
        """Initiate answer set. """

        self.set = initial_set # Set of potential answers (list of lists)
        self.n = len(self.set) # Number of elements in set
        self.scores = []

    def score_set(self, guess):
        """Score guess against all sequences in answer set. """

        for seq in self.set:
            self.scores.append(calculate_score(guess.sequence, seq))
        return self.scores

    def get_compatible_set(self, guess):
        """Given a guess and a score, return compatible set: all consistent sequences in set. """

        # Return score for guess
        self.score_set(guess)

        # Get all answers that are compatible with guess-score pair
        new_set = []
        for i in range(1, self.n):
            if self.scores[i] == guess.score:
                new_set.append(self.set[i])

        # Reset attributes for the new set
        self.set = new_set
        self.n = len(self.set)

        return self.set, self.n

def get_next_guess(answers, guess, solution, random_guess=False):
    """Find next guess with smallest compatible set or guess at random. """

    answers.get_compatible_set(guess)
    if random_guess:
        print answers.n
        print len(answers.set)
        new_guess = Guess(answers.set[random.randint(0, answers.n)], solution)
        #####
        #####
        ## ERROR SEEMS TO BE IN THE LINE ABOVE
        #####
        #####

    # This is where Knuth's algorithm w the clever guessing would go in as an alternative to a random guess

    return new_guess

def play_game(initial_set, initial_guess, solution):
    """Play game. """

    turn = 0
    answers = AnswerSet(initial_set)

    # Make a guess and get the score
    guess = initial_guess

    while turn < 10:

        # Check if guess is correct
        if guess.sequence == solution:
            print "Solved it! :)"

        else:
            turn += 1

            # Get compatible answers with previous guesses (path dependent!!) and score
            answers.get_compatible_set(guess)

            # Make a new guess and score
            guess = get_next_guess(answers, guess, solution, random_guess=True)

            print "Turn: " + str(turn)
            print "Playing sequence: "
            print guess.sequence
            print "Scored: "
            print "Score: "
            print guess.score
            print "Compatible answers: %d" %(answers.n)

    return None

def main():
    """Initialize game and get solution. """

    # Set up game
    columns = ['R', 'G', 'B', 'P', 'Y', 'L'] #L = light blue
    num_positions = 5
    solution = ['Y', 'B', 'L', 'P', 'G']
    game = Game(columns, num_positions, solution)

    print solution

    guess = Guess(['B', 'L', 'Y', 'G', 'R'], solution)
    answers = AnswerSet(game.set)
    answers.get_compatible_set(guess)

    # print guess.sequence
    # print guess.score
    # print answers.n

    play_game(game.set, guess, solution)




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



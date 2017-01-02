# Mastermind

This code solves the [mastermind game][Wiki][wiki-mastermind]. 

## Background
I was given a mastermind game for Christmas and thought it woud be fun to write a program to solve it. 

The initial plan was to use [Knuth's 1977 algorithm][knuth1977]. However, it turns out that algorithm is specific to a game with six colors, four potential positions, and repeated colors. That doesn't work for my game, which has six colors and *five* positions. The minimax algorithm described there might still be interesting, but I don't fully understand it yet.

## Algorithm
*[watch this space]*


## Extensions / fixes
- Tweaks for game setup
    - Add error handling for duplicate colors in the list / too many positions
    - Add posibility to randomly select solution
    - Add possiblity to randomly select guess
- Add recording for games and plays (at least the number of turns)
- Implement a minimax algorithm for selecting the next guess (instead of randomly from the remaining set)

[knuth1977]: http://www.cs.uni.edu/~wallingf/teaching/cs3530/resources/knuth-mastermind.pdf
[wiki-mastermind]: https://en.wikipedia.org/wiki/Mastermind_(board_game)


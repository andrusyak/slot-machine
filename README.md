# Slot Machine Simulator

This is a simple example package written in Python, which demonstrate using generator functions and handling runtime exception to simulate playing a game.

* Use `game(int)` to start a new game with `int` dollars (default `100`).

* Use `spin()` to continue the current game and simulate pulling a lever (or pushing the spin button) of a slot machine.

The slot machine costs `$10` per spin. The `spin()` function activates the random number generator, causing a certain set of symbols to be displayed. This is where fate takes over: the program will calculate your winning based on the symbols displayed, so if you want to continue to play, all you have to do is keep pressing spin (that is calling the `spin()` function).


# Code Example

```python
import slot_machine as sm

sm.game(50)
sm.spin()
# the last line repeat until the game is over
```


# Installation

Download from TestPyPI:
```
pip install -i https://test.pypi.org/simple/ slot-machine
```
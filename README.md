# Slot Machine Simulator

This is a simple example package written in Python to demonstrate creating an iterator, that is an object which implements the _iterator protocol_ consisting of the special methods `__iter__()` and `__next__()`.

* To start a game, instantiate the class `SlotMachine` passing the `int` argument, which defines the initial amount of dollars (default `100`).

* Use  the `spin()` method to continue the current game and simulate pulling a lever (or pushing the spin button) of a slot machine.

* Use the `restart()` method to start a new game with `int` dollars.

The slot machine costs `$10` per spin. The `spin()` method activates the random number generator, causing a certain set of symbols to be displayed. This is where fate takes over: the program will calculate your winning based on the symbols displayed. So if you want to continue to play, all you have to do is keep pressing spin (that is calling the `spin()` method).


# Code Example

```python
from slot_machine import SlotMachine
sm = SlotMachine(50)

sm.spin()
# the last line repeat until the game is over

sm.restart()
```


# Installation

Download from TestPyPI:
```
pip install -i https://test.pypi.org/simple/ slot-machine
```
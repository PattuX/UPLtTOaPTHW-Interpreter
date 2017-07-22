# UPLtTOaPTHW-Interpreter
A Python interpreter for the Ultimate Programming Language to Take Over a Prison, Then He World

https://esolangs.org/wiki/Ultimate_Programming_Language_to_Take_Over_a_Prison,_Then_He_World

additions to the esolangs entry:

* Respect, fear and clock is recalculated every second maintaining eye contact. This is how I interpret the specification and how I think it makes the most sense, but with this interpretation the given 'Hello World!' example won't work.
* Other function calls (inculding shanking) do not affect the clock, although technically shanking is an arithmetic operation
* RESPECT_MAX is 255 by default

# Usage

```
git clone https://github.com/PattuX/UPLtTOaPTHW-Interpreter
cd src/uplttoapthw
py main.py '../../test/hello_world.uplttoapthw'
```

# New Language Specs?

The language is not made by me which makes me a bit hesitant, but some examples:

* shanking a prisoner usually makes all other prisoners go to maximum respect if they aren't at 0 which sucks, as this means you need to maintain eye contact until the fear dropped under 5 again and then keep maintaining eye contact until respect went down to where you want it to be. Just adding the shanked's respect might be better.
* the fact that calling new prisoners zeroes all other prisoners seems a bit harsh
* it might be useful to be able to only squat in front of a few prisoners to lock the rest

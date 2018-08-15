# pybf
One-line python interpreters for [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) (an esoteric programming language).
* `brainfuck_recursive.py` is a true one-line implementation, using only the `sys` library, but the python language has limited 
support for deep recursion (and this uses tail recursion, with many (50000+) calls), so when running complicated programs,
the error `SIGSEGV (Address boundary error)` may arise.
* `brainfuck.py` contains what should be a fully functional Brainfuck interpreter without any limits (except a data array of size 100000).
I don't consider this to be "one-line" in the truest sense, because I use the `itertools.takewhile` function, which isn't a single line.
`brainfuck_recursive.py` should demonstrate how to make the imports inline, so I didn't bother doing that in this file.

## Usage
Stdin can either be piped from a file, or entered manually (enter triggers code to continue). The code does not work in python2 (in particular for IO).
* `python3 brainfuck_recrusive.py examples/rot13.bf < test.txt`
* `python3 brainfuck.py examples/rot13.bf` (then manually type someting and press enter)
The only difference between calling `brainfuck.py` and `brainfuck_recursive.py` is 
that the former takes an option `--data-size` which sets the maximum size of the data array,
allowing for something like 
* `python3 brainfuck.py examples/rot13.bf --data-size 100 < test.txt`.

## Things that aren't perfect
* If input is piped from a file, an error will be thrown once there is nothing left to read. I don't know a way around this (without try catch)
* `brainfuck.py` isn't really just one line, and the argparse is outside of the function (but the core functionality is the `interpret` lambda function)
* Only works on Python3 (tested with 3.6.3)

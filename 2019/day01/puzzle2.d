#!/usr/bin/env rdmd
module day01.puzzle2;

import std;

int fuel(int mass)
{
    auto f = (mass / 3) - 2;
    if (f <= 0)
    {
        return 0;
    }
    else
    {
        return fuel(f) + f;
    }
}

void main(string[] args)
{
    writeln(slurp!(int)("input", "%d").map!(a => fuel(a))
            .reduce!((a, b) => a + b));
}

#!/usr/bin/env rdmd
module day01.puzzle1;
import std;

void main(string[] args)
{
    writeln(slurp!(int)("input", "%d").map!(a => ((a / 3) - 2))
            .reduce!((a, b) => a + b));
}

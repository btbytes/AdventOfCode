#!/usr/bin/env rdmd

module first;
import std.stdio;
import std.string;
import std.algorithm.sorting;
import std.conv;

void main(string[] args)
{
    auto file = File(args[1], "r");
    auto freq = 0;
    foreach (char[] line; file.byLine())
    {
        immutable char fc = line[0];
        auto num = line[0..$];
        immutable n = to!int(num);
        freq += n;
   }
    writefln("%s", freq);
}

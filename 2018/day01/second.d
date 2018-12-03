#!/usr/bin/env rdmd
module second;
import std.stdio;
import std.string;
import std.algorithm.sorting;
import std.conv;
import std.algorithm : canFind;

void main(string[] args)
{
    auto file = File(args[1], "r");

    int[] freqs;
    freqs ~= 0;
    int[] numbers;
    foreach (char[] line; file.byLine())
    {
        auto num = line[0 .. $];
        immutable n = to!int(num);
        numbers ~= n;
    }
    int freq = 0;
    int cnt = 0;
    writefln("starting to find the dup... #numbers: %s", numbers.length);
    int loop = 0 ;
    while (1)
    {
        
        foreach (int nn; numbers)
        {
            freq += nn;
            if (freqs.canFind(freq))
            {
                writefln("Found: %s", freq);
                goto L1;
            }
            freqs ~= freq;
            cnt += 1;
        }
        loop += 1;
        write(".");
    }
    L1:
        writeln("done.");
}

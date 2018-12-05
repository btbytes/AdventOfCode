#!/usr/bin/env rdmd

module first;
import std.stdio;
import std.string;
import std.algorithm;
import std.conv;
import std.algorithm : canFind;

int twos(char[] line) {
    uint s = 0;
    sort(line.representation);
    int i =0 ;
    
    while(i < line.length) {
        if (line[i+1..$].canFind(i)) {
            s += 1;
                
        }
    }
    
    return s;
}


int threes(char[] line) {
    uint s = 0;
    sort(line.representation);
    for (int i=0; i < (line.length - 2); i++) {
        if (line[i] == line[i+1] && line[i] == line[i+2]) {
            s += 1;
        }
    }
    return s;
}
void main(string[] args)
{
    auto file = File(args[1], "r");
    auto two = 0;
    auto three = 0;
    foreach (char[] line; file.byLine())
    {
        // auto l = to!char[](line);
        auto x = twos(line);
        auto y = threes(line);
        two += x;
        three += y;
        writefln("%s - %s - %s", line, x, y);
   }
   // writefln("%s", two*three);
}

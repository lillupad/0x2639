#!/usr/bin/python3

import sys
import os

global stack

stack = []

def execute(input):
    processed = input.split(' ')
    if processed[0] == "::":
        pass
    elif processed[0] == "7075":
        stack.append(processed[1]);
    elif processed[0] == "706f":
        sys.stdout.write(str(stack[len(stack) - 1]) + '\n')
    elif processed[0] == "7063":
        sys.stdout.write(chr(int(stack[len(stack) - 1])) + '\n')
    elif processed[0] == "726d":
        stack.pop()
    elif processed[0] == "696e":
        inp = sys.stdin.readline()
        stack.append(int(inp))
    elif processed[0] == "6164":
        stack.append(int(stack[len(stack) - 1]) + int(stack[len(stack) - 2]))
    elif processed[0] == "7375":
        stack.append(int(stack[len(stack) - 2]) - int(stack[len(stack) - 1]))
    elif processed[0] == "6d75":
        stack.append(int(stack[len(stack) - 2]) * int(stack[len(stack) - 1]))
    elif processed[0] == "6469":
        stack.append(int(stack[len(stack) - 2]) / int(stack[len(stack) - 1]))



def main():
    if len(sys.argv) == 2:
        raw = open(os.path.join(os.getcwd(), sys.argv[1]), 'r').readlines()
        stripped = []
        for i in range(0, len(raw)):
            temp = raw[i].strip();
            stripped.append(temp);
        for i in range(0, len(stripped)):
            execute(stripped[i])
if __name__ == "__main__":
    main()

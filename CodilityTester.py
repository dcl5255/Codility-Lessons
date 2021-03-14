import importlib
import ast

Problem = importlib.import_module("Lessons.1-Iterations.BinaryGap")



def test(func, data):
    return func(data)


if __name__ == '__main__':
    f = open('test-input.txt')
    a = f.read().splitlines()

    for line in a:
        print(test(Problem.solution, ast.literal_eval(line)))
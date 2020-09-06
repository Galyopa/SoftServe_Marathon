"""Convert a certain expression like 2+3 to expression in a postfix notation.

The given expression can have one of the following tokens:

a number;
a parenthesis;
arithmetic operator:
subtraction (-);
addition (+);
multiplication (*);
devision (/);
modulo operation (%).
Example:

For expression = ["2","+","3"] the output should be ["2","3","+"].

[execution time limit] 4 seconds (py)

[input] array.string expression

An array of tokes of a valid expression in the standard notation.

[output] array.string

Tokens of the expression in the postfix notation."""


def toPostFixExpression(e):
    p = {'+': 2, '-': 2, '*': 3, '/': 3, '%': 3, '(': 1, ')': 1}
    s = []
    r = []
    for c in e:
        if c in p and p[c] > 1:
            while s and p[c] <= p[s[-1]]:
                r += [s.pop()]
            s += [c]
        elif c == '(':
            s += [c]
        elif c == ')':
            while s[-1] != '(':
                r += [s.pop()]
            s.pop()
        else:
            r += [c]
    for c in s[::-1]:
        r += [c]
    return r

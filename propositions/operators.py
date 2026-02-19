# This file is part of the materials accompanying the book
# "Mathematical Logic through Python" by Gonczarowski and Nisan,
# Cambridge University Press. Book site: www.LogicThruPython.org
# (c) Yannai A. Gonczarowski and Noam Nisan, 2017-2022
# File name: propositions/operators.py

"""Syntactic conversion of propositional formulas to use only specific sets of
operators."""

from propositions.syntax import *
from propositions.semantics import *

def to_not_and_or(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'``, ``'&'``, and ``'|'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'``, ``'&'``, and
        ``'|'``.
    """
    # Task 3.5
    def convert(f: Formula) -> Formula:
        if is_variable(f.root):
            return f

        left_converted = None
        
        right_converted = None
        
        if f.first:
            left_converted = convert(f.first)
        if f.second:
            right_converted = convert(f.second)

        if f.root == '~':
            return Formula('~', left_converted)
        
        elif f.root == '&' or f.root == '|':
            return Formula(f.root, left_converted, right_converted)
        
        elif f.root == 'T':
            p = Formula('p')
            return Formula('~', Formula('&', p, Formula('~', p)))
        
        elif f.root == 'F':
            p = Formula('p')
            return Formula('&', p, Formula('~', p))
        
        elif f.root == '->':
            return Formula('|', Formula('~', left_converted), right_converted)
    
        elif f.root == '+':
            left_and_not_right = Formula('&', left_converted, Formula('~', right_converted))
            not_left_and_right = Formula('&', Formula('~', left_converted), right_converted)
            return Formula('|', left_and_not_right, not_left_and_right)
        
        elif f.root == '<->':
            left_impl = Formula('|', Formula('~', left_converted), right_converted)
            right_impl = Formula('|', Formula('~', right_converted), left_converted)
            return Formula('&', left_impl, right_impl)
        
        elif f.root == '-&':
            return Formula('~', Formula('&', left_converted, right_converted))
        
        elif f.root == '-|':
            return Formula('~', Formula('|', left_converted, right_converted))
        
        else:
            raise ValueError(f"Unsupported operator: {f.root}")
    
    return convert(formula)

def to_not_and(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'`` and ``'&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'`` and ``'&'``.
    """
    # Task 3.6a

def to_nand(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'-&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'-&'``.
    """
    # Task 3.6b

def to_implies_not(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'~'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'~'``.
    """
    # Task 3.6c

def to_implies_false(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'F'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'F'``.
    """
    # Task 3.6d

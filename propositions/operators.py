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
    
    if is_variable(formula.root):
        return Formula(formula.root)
    
    if formula.root == 'T':
        p = Formula('p')
        return Formula('|', p, Formula('~', p))
    
    if formula.root == 'F':
        p = Formula('p')
        return Formula('&', p, Formula('~', p))
    
    if is_unary(formula.root):
        if formula.root == '~':
            return Formula('~', to_not_and_or(formula.first))
    
    if is_binary(formula.root):
        left = to_not_and_or(formula.first)
        right = to_not_and_or(formula.second)
        
        if formula.root == '&' or formula.root == '|':
            return Formula(formula.root, left, right)
        
        if formula.root == '->':
            return Formula('|', Formula('~', left), right)
        
        if formula.root == '+':
            part1 = Formula('&', left, Formula('~', right))
            part2 = Formula('&', Formula('~', left), right)
            return Formula('|', part1, part2)
        
        if formula.root == '<->':
            p_implies_q = Formula('|', Formula('~', left), right)
            q_implies_p = Formula('|', Formula('~', right), left)
            return Formula('&', p_implies_q, q_implies_p)
        
        if formula.root == '-&':
            return Formula('~', Formula('&', left, right))
        
        if formula.root == '-|':
            return Formula('~', Formula('|', left, right))
    
    return formula    

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

    formula_not_and_or = to_not_and_or(formula)
    
    if is_variable(formula_not_and_or.root):
        return formula_not_and_or
    
    if is_constant(formula_not_and_or.root):
        return formula_not_and_or
    
    if is_unary(formula_not_and_or.root):
        return Formula('~', to_not_and(formula_not_and_or.first))
    
    if is_binary(formula_not_and_or.root):
        left = to_not_and(formula_not_and_or.first)
        right = to_not_and(formula_not_and_or.second)
        
        if formula_not_and_or.root == '&':
            return Formula('&', left, right)
        
        if formula_not_and_or.root == '|':
            not_left = Formula('~', left)
            not_right = Formula('~', right)
            and_not = Formula('&', not_left, not_right)
            return Formula('~', and_not)
    
    return formula_not_and_or

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

    formula_not_and = to_not_and(formula)
    
    if is_variable(formula_not_and.root):
        return formula_not_and
    
    if is_unary(formula_not_and.root):
        inner = to_nand(formula_not_and.first)
        return Formula('-&', inner, inner)
    
    if is_binary(formula_not_and.root):
        if formula_not_and.root == '&':
            left = to_nand(formula_not_and.first)
            right = to_nand(formula_not_and.second)
            nand = Formula('-&', left, right)
            return Formula('-&', nand, nand)
    
    return formula_not_and

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

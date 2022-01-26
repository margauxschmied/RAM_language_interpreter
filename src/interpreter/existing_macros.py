
from src.interpreter.instruction import *


BIG_INT = pow(2, 64)

PUSH = Macro('push', ['x'],
             [RawInstruction(0, 'x'),
              RawInstruction(1, 'x'),
              RawInstruction(0, BIG_INT),
              RawInstruction(2, 'x', 2),
              RawInstruction(1, BIG_INT)])

POP = Macro('pop', ['x'],
            [RawInstruction(0, BIG_INT),
             RawInstruction(1, BIG_INT),
             RawInstruction(0, 'x'),
             RawInstruction(2, BIG_INT, 2),
             RawInstruction(1, 'x')])

COPY_X_IN_Y = Macro(
    'copy_x_in_y', ['x', 'y'],
    [RawInstruction(0, 'x'),
     RawInstruction(1, 'x'),
     RawInstruction(0, 1000),
     RawInstruction(2, 'x', 2),
     RawInstruction(1, 1000),
     RawInstruction(0, 'x'),
     RawInstruction(0, 'y'),
     RawInstruction(2, 1000, 3),
     RawInstruction(1, 'x'),
     RawInstruction(1, 'y')])

ADD = Macro(
    'add', ['x', 'y'],
    [RawInstruction(COPY_X_IN_Y.nom, ['x', 500]),
     RawInstruction(0, 500),
     RawInstruction(0, 'y'),
     RawInstruction(1, 500),
     RawInstruction(2, 500, 2),
     RawInstruction(1, 'y')])

SUB = Macro(
    'sub', ['x', 'y'],
    [RawInstruction(COPY_X_IN_Y.nom, ['y', 500]),
     RawInstruction(0, 500),
     RawInstruction(1, 'x'),
     RawInstruction(1, 500),
     RawInstruction(2, 500, 2),
     RawInstruction(0, 'x')])

MULT = Macro(
    'mult', ['x', 'y'],
    [RawInstruction(COPY_X_IN_Y.nom, ['y', 250]),
     RawInstruction(0, 250),
     RawInstruction(ADD.nom, ['x', 1]),
     RawInstruction(1, 250),
     RawInstruction(2, 250, 2),
     RawInstruction(SUB.nom, [1, 'x'])])


ADD_IN_Z = Macro(
    'add_in_z', ['x', 'y', 'z'],
    [RawInstruction(COPY_X_IN_Y.nom, ['x', 500]),
     RawInstruction(COPY_X_IN_Y.nom, ['y', 'z']),
     RawInstruction(0, 500),
     RawInstruction(1, 500),
     RawInstruction(0, 'z'),
     RawInstruction(2, 500, 2),
     RawInstruction(1, 'z')])

CLEAR = Macro(
    'clear', ['x'],
    [RawInstruction(1, 'x'),
     RawInstruction(2, 'x', 1)])

SUM_0_TO_N = Macro(
    'sum_0_to_n', ['x'],
    [RawInstruction(0, 'x'),
     RawInstruction(1, 'x'),
     RawInstruction(ADD.nom, ['x', 1]),
     RawInstruction(2, 'x', 2),
     RawInstruction(1, 'x')])

macro_list = [
    ADD, SUB, MULT,
    ADD_IN_Z, CLEAR, COPY_X_IN_Y,
    PUSH, POP, SUM_0_TO_N
]
macros = {i.nom: i for i in macro_list}

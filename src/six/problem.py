import operator as op
from typing import Any, Callable
from numbers import Number

class BaseProblem:

    def __init__(self, numbers: list[int], operator: Callable[[Number, Number], Number], starting_value: int):
        self.numbers = numbers
        self.operator = operator
        self.starting_value = starting_value

    def resolve_problem(self) -> int:        
        total = self.starting_value

        for number in self.numbers:
            total = self.operator(total, number)

        return total
        

class AdditionProblem(BaseProblem):
    def __init__(self, numbers: list[int]):
        super().__init__(numbers, op.add, 0)

class MultiplicationProblem(BaseProblem):
    def __init__(self, numbers: list[int]):
        super().__init__(numbers, op.mul, 1)

import unittest
from typing import List

class Solution:
    @staticmethod
    def evalRPN(tokens: List[str]) -> int:
        '''
        You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation. Evaluate the expression. Return an integer that represents the value of the expression.
        Note that:
        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.

        Example 1:
        Input: tokens = ["2","1","+","3","*"]
        Output: 9
        Explanation: ((2 + 1) * 3) = 9

        Example 2:
        Input: tokens = ["4","13","5","/","+"]
        Output: 6
        Explanation: (4 + (13 / 5)) = 6

        Example 3:
        Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        Output: 22
        Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22

        '''
        stack=[]
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i== "-":
                stack.append(-stack.pop()+stack.pop())
            elif i=="*":
                stack.append(stack.pop()*stack.pop())
            elif i=="/":
                first_pop=stack.pop()
                second_pop=stack.pop()
                stack.append(int(second_pop/first_pop))
            else:
                stack.append(int(i))
        return stack[0]
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        tokens = ["2","1","+","3","*"]
        self.assertEqual(9, Solution.evalRPN(tokens))

    def test_case_2(self):
        tokens = ["4","13","5","/","+"]
        self.assertEqual(6, Solution.evalRPN(tokens))

    def test_case_3(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        self.assertEqual(22, Solution.evalRPN(tokens))
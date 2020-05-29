from typing import List, Union

class Stack:
    """
    Stack Implementation based of python list (array)
    values are kept in as string to suite the implementation needs
    methods:
        pop: 
            pops out the last element of the stack and returns it
        push: 
            pushes an element to the top of the stack
        to_base_string: 
            Helper function to convert the stack to a string 
            representing the results after computation of bases
    """
    def __init__(self, content: List = None) -> None:
        self._stack = content or []

    def pop(self) -> Union[str, int]:
        """
        pop: pops out the last element of the stack and returns it
        """
        return self._stack.pop()

    def push(self, value: Union[str, int]) -> bool:
        """
        push: pushes an element to the top of the stack
        """
        self._stack.append(str(value))
        return True
    
    def to_base_string(self):
        """
        to_base_string: Helper function to convert the stack to a string 
                        representing the results after computation of bases
        """
        stack = self._stack[::-1]
        return ''.join(stack)
    
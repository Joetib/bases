
from typing import List, Dict, Any, Union   # used to provide type hinting



# Dictionary that maps numbers to their alphabet form
# This is used to quickly get these letters for bases higher than 10
num_to_letters: Dict = {
    
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: "K",
    21: 'L',
    22: 'M',
    23: 'N',
    24: 'O',
    25: 'P',
    26: 'Q',
    27: 'R'
}

# Dictionary that maps alphabets to their numeric form
# This is used to quickly get the correspondig values of
# such alphabets especially when converting from bases higher
# than 10 to other bases
letters_to_num: Dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    "L": 21,
    "M": 22,
    "N": 23,
    "O": 24,
    "P": 25,
    "Q": 26,
    "R": 27
}
class BaseStack:
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
    

class Converter:
    """
    Converter:
        Contains functions to do actual conversion numbers from one base to another.
        methods:
            convert(number: Union[str, int],to_base:int = 10, from_base: int=10)
            from_base_ten(number: Union[str, int],base: int) -> str
            to_base_ten(number: Union[str, int],base: int) -> str  
    """

    def convert(self, number: Union[str, int], to_base:int = 10, from_base: int = 10) -> str:
        """
        convert:
            description:
                Entry point to handle all kinds of conversions.
                
                It calls the appropriate (function from_base_ten or to_base_ten) to
                do the actual conversion depending on the arguments provided
                If none of the bases we are converting between is 10, we first convert
                to base 10 and then to the desired base.
                Leaving both to_base and from_base blank just results
                returning the value
            arguments:
                number: 
                    types: str, int
                    default: None
                to_base:
                    description: The base to convert to
                    types: int
                    default: 10
                from_base:
                    description: The base we are converting from
                    types: int
                    default: 10
            returns:
                type: str
            example:
                convert(number=10, to_base=2, from_base=10)
                    convert from base 10 to base 2
                convert(number=10, to_base=2) 
                    converts from base 10 to base 2
                convert(number=10, from_base=11) 
                    converts from base 11 to base 10
        """

        # Cannot convert to or from base 1 and below
        if from_base <= 1  or to_base <= 1:
            return

        if from_base != 10:
            number = self.to_base_ten(number, from_base)
        if to_base != 10:
            number = self.from_base_ten(number, to_base)
        return number


    def from_base_ten(self, number: Union[str,int], base: int) -> str:
        """
        from_base_ten:
            description:
                Converts a number from base ten to the specified base.
            arguments:
                number: 
                    types: str, int
                    default: None
                
                base:
                    description: The base we are converting to
                    types: int
                    default: None
            returns:
                type: str
            example:
                from_base_ten(number=10, base=2)
                    convert from base 10 to base 2
                
        """
        stack: BaseStack = BaseStack()
        decimals = ""
        number = str(number)
        # check if there is a decimal point in the number
        if '.' in number:
            decimals = f".{self._decimal_from_base_ten(str(number).split('.')[1], base)}"
        number = int(float(number)) # int(float()) required because in cannot convert strings like '0.5'
        while True:
            if number < base:
                # if the number is greater than 9, get its corresponding
                # letter and push to the stack else push the remainder to the
                # stack
                stack.push(num_to_letters.get(number, number))
                break
            else:
                number, remainder = number // base, number % base
                # if the remainder is greater than 9, get its corresponding
                # letter and push to the stack else push the remainder to the
                # stack
                stack.push(num_to_letters.get(remainder, remainder)) 
        return stack.to_base_string() + decimals


    def to_base_ten(self, number: Union[str, int], base) -> str:
        """
        to_base_ten:
            description:
                Converts a number from a given base to  base ten.
            arguments:
                number: 
                    types: str, int
                    default: None
                
                base:
                    description: The base we are converting the number from
                    types: int
                    default: None
            returns:
                type: str
            example:
                to_base_ten(number=10, base=2)
                    convert from base 2 to base 10
        """
        
        decimals = ""
        number = str(number)

        # check if there is a decimal point in the number
        if '.' in number: 
            decimals = f".{self._decimal_to_base_ten('.'+number.split('.')[-1], base)}"
        number = number.split('.')[0][::-1]
        result = 0
        for i in range(len(number)-1, -1, -1):
            # if the current character (ie. number[i]) is a letter, get its corresponding
            # numeric value for the calculation otherwise it is considered a number and used directly
            result += int(letters_to_num.get(number[i], number[i])) * base ** i
        

        return f'{result}{decimals}' 


    def _decimal_to_base_ten(self, number: str, base: int) -> str:
        """
        _decimal_to_base_ten:
            description:
                Converts the decimal part number from a given base to  base ten.
                As an example, if you pass in 10 base 2 you will get 0.5 base ten
                Thus it assumes the 10 based in came from a number of the format *.10 base 2,
                where * refers to the whole number part of the actual number.
                This function is not intended to be used directly but to be used by to_base_ten
            arguments:
                number: 
                    types: str, int
                    default: None
                
                base:
                    description: The base we are converting the number from
                    types: int
                    default: None
            returns:
                type: str
            example:
                _decimal_to_base_ten(number=10, base=2)
                    convert from base 2 to base 10
        """
        
        if not '.' in number:
            raise Exception('_decimal_to_base: number must contain "."')
        number = number.split('.')[1]
        result: int = 0
        for i in range(0, len(number)):
        
            current_char: str = number[i]
            result += int(letters_to_num.get(current_char, current_char)) * (base ** -(i+1))
        return str(result).split('.')[-1]
    

    def _decimal_from_base_ten(self, number: str, base: int) -> str:
        """
        _decimal_from_base_ten:
            description:
                Converts the decimal part number from  base ten to a given base.
                As an example, if you pass in 5 as number and base 10 you will get 1 base 2
                Keep in mind that alll these are floating point numbers.
                Thus it assumes the 5 based in came from a number of the format *.5 base 10,
                where * refers to the whole number part of the actual number.
                This function is not intended to be used directly but to be used by from_base_ten
            arguments:
                number: 
                    types: str, int
                    default: None
                
                base:
                    description: The base we are converting to
                    types: int
                    default: None
            returns:
                type: str
            example:
                _decimal_from_base_ten(number=5, base=2)
                    convert from base 10 to base 2 where number is allegedly from a source as *.5
                
        """
        stack: BaseStack = BaseStack()
        
        number = int(number)
        while True:
            
            number = float(number*base)
            if number.is_integer():

                # This is to remove trailing zeros betore pushing number to stack;
                if number != 0:
                    if str(number).endswith('0'):
                        number = number/10
                    stack.push(int(number))
                break
            whole = int(number)
            
            # if the remainder is greater than 9, get its corresponding
            # letter and push to the stack else push the remainder to the
            # stack
            stack.push(num_to_letters.get(whole, whole))
                
            # Substracting the whole number part was chosen for a few reasons
            number -= whole
                
        return stack.to_base_string()



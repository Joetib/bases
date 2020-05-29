from . import converter
from unittest import TestCase


class TestBases(TestCase):
    def test_convert_function(self):
        tests = [
            
            # conversion from base 10
            {
                'number': 2,
                'to_base': 2,
                'expected': '10',
                'from_base': 10
            },
            {
                'number': 4,
                'to_base': 3,
                'expected': '11',
                'from_base': 10
            },
            {
                'number': 11,
                'to_base': 9,
                'expected': '12',
                'from_base': 10
            },
            {
                'number': 10,
                'to_base': 11,
                'expected': 'A',
                'from_base': 10
            },
            {
                'number': 120,
                'to_base': 11,
                'expected': 'AA',
                'from_base': 10
            },
            # conversion to base 10
            {
                'number': 10,
                'from_base': 2,
                'to_base': 10,
                'expected': '2'
            },
            {
                'number': 11,
                'from_base': 3,
                'to_base': 10,
                'expected': '4'
            },
            {
                'number': 12,
                'from_base': 9,
                'to_base': 10,
                'expected': '11'
            },
            {
                'number': 'A',
                'from_base': 11,
                'to_base': 10,
                'expected': '10'
            },
            {
                'number': 'AA',
                'from_base': 11,
                'to_base': 10,
                'expected': '120'
            },
            {
                'number': 0.111,
                'from_base': 2,
                'to_base': 10,
                'expected': '0.875'
            },
            # Conversion to Any
            {
                'number': 0.5,
                'from_base': 10,
                'to_base': 2,
                'expected': '0.1',
            },
            {
                'number': 0.33,
                'from_base': 10,
                'to_base': 2,
                'expected': '0.010101000111101011100001010001111010111000010100011111',
            },
            {
                'number': 56.33,
                'from_base': 10,
                'to_base': 2,
                'expected': '111000.010101000111101011100001010001111010111000010100011111',
            },
            {
                'number': 56.34,
                'from_base': 8,
                'to_base': 2,
                'expected': '101110.0111',
            },
            {
                'number': '0.010101000111101011100001010001111010111000010100011111',
                'from_base': 2,
                'to_base': 10,
                'expected': '0.33',
            }
        ]
        for test in tests:
            
            self.assertEqual(
                converter.Converter().convert(
                    test['number'], test['to_base'], test['from_base']
                ),
                test['expected']
            )
    def test_base_10_to_base_2(self):
        tests = [
            {
                'number': 2,
                'base': 2,
                'expected': '10'
                
            },
            {
                'number': 4,
                'base': 3,
                'expected': '11'
            },
            {
                'number': 11,
                'base': 9,
                'expected': '12'
            },
            {
                'number': 10,
                'base': 11,
                'expected': 'A'
            },
            {
                'number': 120,
                'base': 11,
                'expected': 'AA'
            }
        ]
        for test in tests:
            self.assertEqual(
                converter.Converter().from_base_ten(test['number'], test['base']), 
                test['expected']
            )
    
    def test_to_base_2(self):
        tests = [
            {
                'number': 10,
                'base': 2,
                'expected': '2'
            },
            {
                'number': 11,
                'base': 3,
                'expected': '4'
            },
            {
                'number': 12,
                'base': 9,
                'expected': '11'
            },
            {
                'number': 'A',
                'base': 11,
                'expected': '10'
            },
            {
                'number': 'AA',
                'base': 11,
                'expected': '120'
            }
        ]
        for test in tests:
            self.assertEqual(
                converter.Converter().to_base_ten(test['number'], test['base']), 
                test['expected']
            )
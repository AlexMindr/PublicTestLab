import unittest
from unittest.mock import patch
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(1,"2"),3)
        with self.assertRaises(ValueError):
            calc.add(1, "abc")
        self.assertEqual(calc.add(1,[1,2]),[2,3])
        with self.assertRaises(ValueError):
            calc.add(1, [1,"abc"])
        self.assertEqual(calc.add(1,(1,2)),4)
        with self.assertRaises(ValueError):
            calc.add(1, (1,"abc"))
        self.assertEqual(calc.add(1, {'a':1,'b':2}), {'a':2,'b':3})
        with self.assertRaises(ValueError):
            calc.add(1, {'a':'abc', 'b':1})
        self.assertEqual(calc.add('1','2'), 3)
        with self.assertRaises(ValueError):
            calc.add("abc",'1')
        self.assertEqual(calc.add('1', [1,2,3]), [2,3,4])
        with self.assertRaises(ValueError):
            calc.add("abc", [1,2,3])
        self.assertEqual(calc.add('1', (1, 2, 3)), 7)
        with self.assertRaises(ValueError):
            calc.add("abc", (1, 2, 3))
        self.assertEqual(calc.add('1', {'a': 1, 'b': 2}), {'a': 2, 'b': 3})
        with self.assertRaises(ValueError):
            calc.add('abc', {'a': 'abc', 'b': 1})
        self.assertEqual(calc.add([1,1,1],[1,1,1]),[2,2,2])
        self.assertEqual(calc.add([1,1],[1,1,1]),5)
        with self.assertRaises(ValueError):
            calc.add(['abc'],[1,2,3])
        self.assertEqual(calc.add([1, 1, 1], (1, 1, 1)), [2, 2, 2])
        self.assertEqual(calc.add([1, 1], (1, 1, 1)), 5)
        with self.assertRaises(ValueError):
            calc.add(('abc'), [1, 2, 3])
        self.assertEqual(calc.add([1, 1], {1:2,2:2}), 6)
        with self.assertRaises(ValueError):
            calc.add(['abc'], {1:1, 2 :3})
        self.assertEqual(calc.add((1, 1, 1), (1, 1, 1)), [2, 2, 2])
        self.assertEqual(calc.add((1, 1), (1, 1, 1)), 5)
        with self.assertRaises(ValueError):
            calc.add(('abc'), (1, 2, 3))
        self.assertEqual(calc.add((1, 1), {1: 2, 2: 2}), 6)
        with self.assertRaises(ValueError):
            calc.add(('abc'), {1: 1, 2: 3})
        self.assertEqual(calc.add({1:1,2: 1,3: 1}, {1:1,2: '2',3: 1}), {1:2,2: 3,3: 2})
        self.assertEqual(calc.add({1:1,2: 1,3: 1}, {1:1,2:'2'}),6 )
        with self.assertRaises(ValueError):
            calc.add({1:1,2: 1,'2': 'abc'}, {1:1,2: 1,3: 1})

    def test_add2(self):
        with patch('calc.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            result=calc.add2(1,2)
            mocked_get.assert_called_with('http://127.0.0.1:5000/add/1+2')
            self.assertEqual(result, 'Success')

            mocked_get.return_value.ok = False

            result = calc.add2(1,'a')
            mocked_get.assert_called_with('http://127.0.0.1:5000/add/1+a')
            self.assertEqual(result, 'Bad Response!')


    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, -1), 0)
        self.assertEqual(calc.subtract(-1, 0), -1)
        self.assertEqual(calc.subtract(2, "2"), 0)
        with self.assertRaises(ValueError):
            calc.subtract(1, "abc")
        self.assertEqual(calc.subtract([1,2], 1), [0, 1])
        with self.assertRaises(ValueError):
            calc.subtract(1, [1, "abc"])
        self.assertEqual(calc.subtract(10, (1, 2)), 7)
        with self.assertRaises(ValueError):
            calc.subtract(1, (1, "abc"))
        self.assertEqual(calc.subtract( {'a': 1, 'b': 2},1), {'a': 0, 'b': 1})
        with self.assertRaises(ValueError):
            calc.subtract(1, {'a': 'abc', 'b': 1})
        self.assertEqual(calc.subtract('1', '2'), -1)
        with self.assertRaises(ValueError):
            calc.subtract("abc", '1')
        self.assertEqual(calc.subtract( [1, 2, 3],'1'), [0, 1, 2])
        with self.assertRaises(ValueError):
            calc.subtract("abc", [1, 2, 3])
        self.assertEqual(calc.subtract('10', (1, 2, 3)), 4)
        with self.assertRaises(ValueError):
            calc.subtract("abc", (1, 2, 3))
        self.assertEqual(calc.subtract( {'a': 1, 'b': 2},1), {'a': 0, 'b': 1})
        with self.assertRaises(ValueError):
            calc.subtract('abc', {'a': 'abc', 'b': 1})
        self.assertEqual(calc.subtract([1, 1, 1], [1, 1, 1]), [0, 0, 0])
        self.assertEqual(calc.subtract([2, 1], [1, 1, 1]), 0)
        with self.assertRaises(ValueError):
            calc.subtract(['abc'], [1, 2, 3])
        self.assertEqual(calc.subtract([1, 1, 1], (1, 1, 1)), [0, 0, 0])
        self.assertEqual(calc.subtract([1, 2], (1, 1, 1)), 0)
        with self.assertRaises(ValueError):
            calc.subtract(('abc'), [1, 2, 3])
        self.assertEqual(calc.subtract(['-1', 2], {1: 2, 2: 2}), -3)
        with self.assertRaises(ValueError):
            calc.subtract(['abc'], {1: 1, 2: 3})
        self.assertEqual(calc.subtract((1, 1, 1), (1, 1, 1)), [0, 0, 0])
        self.assertEqual(calc.subtract((1, 3), (1, 1, 1)), 1)
        with self.assertRaises(ValueError):
            calc.subtract(('abc'), (1, 2, 3))
        self.assertEqual(calc.subtract((1, 1), {1: 2, 2: 2}), -2)
        with self.assertRaises(ValueError):
            calc.subtract(('abc'), {1: 1, 2: 3})
        self.assertEqual(calc.subtract({1: 1, 2: 1, 3: 1}, {1: 1, 2: '1', 3: -1}), {1: 0, 2: 0, 3: 2})
        self.assertEqual(calc.subtract({1: 1, 2: 1, 3: 1}, {1: 1, 2: '2'}), 0)
        with self.assertRaises(ValueError):
            calc.subtract({1: 1, 2: 1, '2': 'abc'}, {1: 1, 2: 1, 3: 1})

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(1, "2"), 2)
        with self.assertRaises(ValueError):
            calc.multiply(1, "abc")
        self.assertEqual(calc.multiply(2, [1, 2]), [2, 4])
        with self.assertRaises(ValueError):
            calc.multiply(1, [1, "abc"])
        self.assertEqual(calc.multiply(2, (1, 2)), 4)
        with self.assertRaises(ValueError):
            calc.multiply(1, (1, "abc"))
        self.assertEqual(calc.multiply(2, {'a': 1, 'b': 2}), {'a': 2, 'b': 4})
        with self.assertRaises(ValueError):
            calc.multiply(1, {'a': 'abc', 'b': 1})
        self.assertEqual(calc.multiply('1', '2'), 2)
        with self.assertRaises(ValueError):
            calc.multiply("abc", '1')
        self.assertEqual(calc.multiply('2', [1, 2, 3]), [2, 4, 6])
        with self.assertRaises(ValueError):
            calc.multiply("abc", [1, 2, 3])
        self.assertEqual(calc.multiply('2', (1, 2, 3)), 12)
        with self.assertRaises(ValueError):
            calc.multiply("abc", (1, 2, 3))
        self.assertEqual(calc.multiply('2', {'a': 1, 'b': 2}), {'a': 2, 'b': 4})
        with self.assertRaises(ValueError):
            calc.multiply('abc', {'a': 'abc', 'b': 1})
        self.assertEqual(calc.multiply([1, 1, 1], [2, 3, 4]), [2, 3, 4])
        self.assertEqual(calc.multiply([1, 2], [1, 0, 1]), 0)
        with self.assertRaises(ValueError):
            calc.multiply(['abc'], [1, 2, 3])
        self.assertEqual(calc.multiply([1, 1, 2], (1, 2, '3')), [1, 2, 6])
        self.assertEqual(calc.multiply([1, 2], (1, -1, 1)), -2)
        with self.assertRaises(ValueError):
            calc.multiply(('abc'), [1, 2, 3])
        self.assertEqual(calc.multiply([1, 2], {1: 2, 2: 2}), 8)
        with self.assertRaises(ValueError):
            calc.multiply(['abc'], {1: 1, 2: 3})
        self.assertEqual(calc.multiply((1, 2, 3), (1, 2, -1)), [1, 4, -3])
        self.assertEqual(calc.multiply((1, 1), (1, 0, 1)), 0)
        with self.assertRaises(ValueError):
            calc.multiply(('abc'), (1, 2, 3))
        self.assertEqual(calc.multiply((1, 2), {1: 2, 2: 2}), 8)
        with self.assertRaises(ValueError):
            calc.multiply(('abc'), {1: 1, 2: 3})
        self.assertEqual(calc.multiply({1: 1, 2: 2, 3: 3}, {1: 1, 2: '2', 3: 1}), {1: 1, 2: 4, 3: 3})
        self.assertEqual(calc.multiply({1: 1, 2: 2, 3: 1}, {1: 1, 2: '2'}), 4)
        with self.assertRaises(ValueError):
            calc.multiply({1: 1, 2: 1, '2': 'abc'}, {1: 1, 2: 1, 3: 1})

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(2, "2"), 1)
        with self.assertRaises(ValueError):
            calc.divide(1, "abc")
        self.assertEqual(calc.divide(2, [4, 2]), [2, 1])
        with self.assertRaises(ValueError):
            calc.divide(1, [1, "abc"])
        self.assertEqual(calc.divide(8, (4, 2)), 1)
        with self.assertRaises(ValueError):
            calc.divide(1, (1, "abc"))
        self.assertEqual(calc.divide(2, {'a': 2, 'b': 4}), {'a': 1, 'b': 2})
        with self.assertRaises(ValueError):
            calc.divide(1, {'a': 'abc', 'b': 1})
        self.assertEqual(calc.divide('4', '2'), 2)
        with self.assertRaises(ValueError):
            calc.divide("abc", '1')
        self.assertEqual(calc.divide('2', [2, 4, 6]), [1, 2, 3])
        with self.assertRaises(ValueError):
            calc.divide("abc", [1, 2, 3])
        self.assertEqual(calc.divide('12', (1, 2, 3)), 2)
        with self.assertRaises(ValueError):
            calc.divide("abc", (1, 2, 3))
        self.assertEqual(calc.divide('2', {'a': 2, 'b': 4}), {'a': 1, 'b': 2})
        with self.assertRaises(ValueError):
            calc.divide('abc', {'a': 'abc', 'b': 1})
        self.assertEqual(calc.divide([2, 4, 6], [2, 2, 3]), [1,2, 2])
        self.assertEqual(calc.divide([3, 2], [2, 3, 1]), 1)
        with self.assertRaises(ValueError):
            calc.divide(['abc'], [1, 2, 3])
        self.assertEqual(calc.divide([1, 4, 9], (1, 2, '3')), [1, 2, 3])
        self.assertEqual(calc.divide([3, 4], (1, -1, 2)), -6)
        with self.assertRaises(ValueError):
            calc.divide(('abc'), [1, 2, 3])
        self.assertEqual(calc.divide([3, 2], {1: 2, 2: 3}), 1)
        with self.assertRaises(ValueError):
            calc.divide(['abc'], {1: 1, 2: 3})
        self.assertEqual(calc.divide((2, 12, 6), (2, 2, -1)), [1, 6, -6])
        self.assertEqual(calc.divide((1, 8), (2, 2,2 )), 1)
        with self.assertRaises(ValueError):
            calc.divide(('abc'), (1, 2, 3))
        self.assertEqual(calc.divide((3, 2), {1: 2, 2: 3}), 1)
        with self.assertRaises(ValueError):
            calc.divide(('abc'), {1: 1, 2: 3})
        self.assertEqual(calc.divide({1: 3, 2: 6, 3: 9}, {1: 1, 2: '2', 3: 9}), {1: 3, 2: 3, 3: 1})
        self.assertEqual(calc.divide({1: 1, 2: 2, 3: 3}, {1: 1, 2: '2'}), 3)
        with self.assertRaises(ValueError):
            calc.divide({1: 1, 2: 1, '2': 'abc'}, {1: 1, 2: 1, 3: 1})

        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, '0')
        with self.assertRaises(ValueError):
            calc.divide(0, [1,1])
        with self.assertRaises(ValueError):
            calc.divide(1, (0,1))
        with self.assertRaises(ValueError):
            calc.divide(0, {1:2})
        with self.assertRaises(ValueError):
            calc.divide(10, '0')
        with self.assertRaises(ValueError):
            calc.divide('0', [0,1])
        with self.assertRaises(ValueError):
            calc.divide('1', (0,1))
        with self.assertRaises(ValueError):
            calc.divide('0', {1:2})
        with self.assertRaises(ValueError):
            calc.divide([1,1,1], (0,1))
        with self.assertRaises(ValueError):
            calc.divide([1,1], {1:0})
        with self.assertRaises(ValueError):
            calc.divide((1,2), (0,1))
        with self.assertRaises(ValueError):
            calc.divide((1,2), {1:0})
        with self.assertRaises(ValueError):
            calc.divide({1:1}, {1:0})



if __name__ == '__main__':
    unittest.main()
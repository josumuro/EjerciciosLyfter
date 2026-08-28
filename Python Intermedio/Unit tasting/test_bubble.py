import unittest

from unit import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_short_list(self):
        #Arrange
        numbers=[5,2,3,9,7]
        expected=[2,3,5,7,9]
        #Act
        result = bubble_sort(numbers)
        #Assert
        self.assertEqual(result, expected)
       

    def test_long_list(self):
        #Arrange
        numbers=[5,2,9,1,5,6]
        expected=[1,2,5,5,6,9]
        #Act
        result = bubble_sort(numbers)
        #Assert
        self.assertEqual(result, expected)

        
    def test_100_elements(self):
        #Arrange
        numbers=list(range(105, 0, -1))
        expected=list(range(1, 106))
        #Act
        result = bubble_sort(numbers)
        #Assert
        self.assertEqual(result, expected)
       

    def test_empty_list(self):
        #Arrange

        #Act
        result = bubble_sort([])
        #Assert
        self.assertEqual(result, [])


    def test_is_not_list(self):
        #Arrange
        numbers=123

        #Act & Assert
        with self.assertRaises(TypeError):
            bubble_sort(123)


if __name__ == '__main__':unittest.main()
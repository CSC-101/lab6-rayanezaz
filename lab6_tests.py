import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def testSelectionSortBooks1(self):
        input = [data.Book(["Suzanne Collins"], "The Hunger Games"), data.Book(["Rick Riordan"], "Percy Jackson")]
        expected = [data.Book(["Rick Riordan"], "Percy Jackson"), data.Book(["Suzanne Collins"], "The Hunger Games")]
        result = lab6.selection_sort_books(input)
        self.assertEqual(expected, result)

    def testSelectionSortBooks2(self):
        input = [data.Book(["Diana Gabaldon"], "Outlander"), data.Book(["John Ronald Reuel Tolkien"], "The Lord of the Rings")]
        expected = [data.Book(["Diana Gabaldon"], "Outlander"), data.Book(["John Ronald Reuel Tolkien"], "The Lord of the Rings")]
        result = lab6.selection_sort_books(input)
        self.assertEqual(expected, result)

    def testSelectionSortBooks3(self):
        input = [data.Book(["Dr. Seuss"], "The Cat in the Hat"), data.Book(["Lincoln Peirce"], "Big Nate")]
        expected = [data.Book(["Lincoln Peirce"], "Big Nate"), data.Book(["Dr. Seuss"], "The Cat in the Hat")]
        result = lab6.selection_sort_books(input)
        self.assertEqual(expected, result)

    # Part 2
    def testSwapCase1(self):
        input = "LoLlApAlOoZa"
        expected = "lOlLaPaLoOzA"
        result = lab6.swap_case(input)
        self.assertEqual(expected, result)

    def testSwapCase2(self):
        input = "2435rOBOt"
        expected = "2435RoboT"
        result = lab6.swap_case(input)
        self.assertEqual(expected, result)

    def testSwapCase3(self):
        input = ""
        expected = ""
        result = lab6.swap_case(input)
        self.assertEqual(expected, result)

    # Part 3
    def testStrTranslate1(self):
        input = "lollipop"
        result = lab6.str_translate(input, "l", "x")
        expected = "xoxxipop"
        self.assertEqual(expected, result)

    def testStrTranslate2(self):
        input = "Cal Poly 2 - 0 Santa Barbara"
        result = lab6.str_translate(input, "a", "w")
        expected = "Cwl Poly 2 - 0 Swntw Bwrbwrw"
        self.assertEqual(expected, result)

    def testStrTranslate3(self):
        input = ""
        result = lab6.str_translate(input, "o", "p")
        expected = ""
        self.assertEqual(expected, result)

    # Part 4
    def testHistogram1(self):
        input = "My favorite food is pizza"
        expected = {"My": 1, "favorite": 1, "food": 1, "is": 1, "pizza": 1}
        result = lab6.histogram(input)
        self.assertEqual(expected, result)

    def testHistogram2(self):
        input = "My favorite food is pizza and pizza and is and my favorite and food"
        expected = {"My": 1, "favorite": 2, "food": 2, "is": 2, "pizza": 2, "and": 4, "my": 1}
        result = lab6.histogram(input)
        self.assertEqual(expected, result)

    def testHistogram3(self):
        input = ""
        expected = {}
        result = lab6.histogram(input)
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()

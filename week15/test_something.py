import unittest


class TestGreeter(unittest.TestCase):
    def test_number_can_be_used_in_greet(self):
        expected = "Hello, 42!"
        name = 42
        self.assertEqual(expected, greet(name))


name = "Tiffany"

def greet(name):
    if isinstance(name, (int)):
        name = str(name)

    return(f"Hello, {name.title()}!")

# should say "Hello, Tiffany!"

# def test():
#     # test 1
#     name = "tiffany"
#     expected = "Hello, Tiffany!"
#     assert expected == greet(name), f"{expected = }, got: {greet(name)}"
#
#     # test 2
#     name = 42
#     expected = "Hello, 42!"
#     assert expected == greet(name), f"{expected = }, got: {greet(name)}"
#     print("All tests pass!")
#
#     # test 3
#     try:
#         name = 42.0
#         expected = "Hello, 42.0!"
#         greet(name)
#     except (AttributeError, ValueError):
#         assert True
#     else:
#         assert False, "Attribute Error was not received!"
#     finally:
#         print("Finally always gets executed")
#     print("All tests pass!")


def main():
        print(greet(name))


if __name__ == '__main__':
    main()
    # test()

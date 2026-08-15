from greet import greet


def test_greet_with_name():
    assert greet("World") == "Hello, World!"


def test_greet_with_empty_name():
    assert greet("") == "Hello, !"

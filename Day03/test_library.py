from library import Library

def test_new_library_is_empty():
    """Tests that a newly created library starts with 0 books."""
    lib = Library("City Library")
    assert lib.count_books() == 0  # Assert means "I expect this to be true"

def test_add_book():
    """Tests that adding a book increases the count."""
    lib = Library("School Library")
    lib.add_book("Python Basics")
    assert lib.count_books() == 1
    assert lib.books[0] == "Python Basics"

def test_dunder_str():
    """Tests that printing the object gives the correct string."""
    lib = Library("Town Library")
    lib.add_book("AI Fundamentals")
    # We expect the string representation to match exactly what our __str__ method returns
    assert str(lib) == "Library 'Town Library' has 1 books."

#def test_intentional_failure():
    #lib = Library("Fake Library")
    #assert lib.count_books() == 5  # A new library has 0 books, so this is a lie!
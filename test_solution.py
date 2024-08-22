import solution;

def test_single():
    assert solution.spin_words("Welcome") == "emocleW"
    assert solution.spin_words("to") == "to"
    assert solution.spin_words("CodeWars") == "sraWedoC"

def test_multiple():
    assert solution.spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert solution.spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"
    assert solution.spin_words("This is another test") == "This is rehtona test"

def test_empty():
    assert solution.spin_words("") == ""
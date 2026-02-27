from palindrome import longest_palindromic_substring

# Testing the basic examples from the instructions
def test_babad():
    result = longest_palindromic_substring("babad")
    # Could be "bab" or "aba" - both are correct
    assert result == "bab" or result == "aba"

def test_cbbd():
    result = longest_palindromic_substring("cbbd")
    assert result == "bb"

def test_racecar():
    result = longest_palindromic_substring("racecar")
    assert result == "racecar"

# Testing edge cases
def test_single_letter():
    result = longest_palindromic_substring("a")
    assert result == "a"

def test_two_letters():
    result = longest_palindromic_substring("ac")
    # Either "a" or "c" is valid
    assert result == "a" or result == "c"

def test_empty():
    result = longest_palindromic_substring("")
    assert result == ""

def test_same_letters():
    result = longest_palindromic_substring("aaaa")
    assert result == "aaaa"

def test_no_long_palindrome():
    result = longest_palindromic_substring("abcdef")
    # Should return a single character
    assert len(result) == 1

def test_palindrome_beginning():
    result = longest_palindromic_substring("abaxyz")
    assert result == "aba"

def test_palindrome_end():
    result = longest_palindromic_substring("xyzaba")
    assert result == "aba"

def test_even_palindrome():
    result = longest_palindromic_substring("abba")
    assert result == "abba"

def test_odd_palindrome():
    result = longest_palindromic_substring("racecar")
    assert result == "racecar"

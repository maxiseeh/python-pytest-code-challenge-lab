from palindrome import longest_palindromic_substring

# Basic Cases
def test_palindrome_babad():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

def test_palindrome_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_palindrome_racecar():
    assert longest_palindromic_substring("racecar") == "racecar"

# Edge Cases
def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_two_different_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"

def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abcdef")
    assert len(result) == 1 and result in "abcdef"

def test_palindrome_at_start():
    assert longest_palindromic_substring("abaxyz") == "aba"

def test_palindrome_at_end():
    assert longest_palindromic_substring("xyzaba") == "aba"

def test_even_length_palindrome():
    assert longest_palindromic_substring("abba") == "abba"

def test_odd_length_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    # Handle empty string or single character
    if len(s) < 2:
        return s
    
    longest = ""
    
    # Check every possible substring
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            
            # Check if it's a palindrome
            if substring == substring[::-1]:
                # Keep track of the longest one
                if len(substring) > len(longest):
                    longest = substring
    
    return longest
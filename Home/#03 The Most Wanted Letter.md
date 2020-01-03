You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Example:

1 checkio("Hello World!") == "l"
2 checkio("How do you do?") == "o"
3 checkio("One") == "e"
4 checkio("Oops!") == "o"
5 checkio("AAaooo!!!!") == "a"
6 checkio("abe") == "a"

How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text. For example: we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear. This is interesting stuff for language experts!

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105
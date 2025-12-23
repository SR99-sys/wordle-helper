# wordle-helper
Helps guessing the WORDLE word of the day. Takes in the 1st guess, and G/Y/B values as input and iterates till failure.

The code tries to assist you in guessing the Wordle word of the day
It asks for the first word and feedback, and assumes that you go with the suggested word for the subsequent guesses, hence only prompting feedback from word/guess 2. The guess comes from a list of pre-loaded words, available online.

Example:
If the split for "AUDIO" is A=G(Green), U=B(Black), D=B(Black), I=B(Black), O=Y(Yellow), then you will enter "GBBBY". The code will then give you the best possible word for the 2nd entry. You then enter G/Y/B values for the 2nd entry (Feedback attained after enetering suggestion in Wordle), and it keeps looping till the feedback is "GGGGG", till all 6 turns are exhausted, or if there isn't a matching word in the list.

Constraint:
Although the list is really exhaustive, it might still miss some words. For instance, the word on December 21st, 2025 was "QUILT", which isn't present in the words list. However, it did help me arrive there, which is what the code aims to do.

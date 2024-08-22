# Word Spinner

Write a function that takes in a string of one or more words, and **returns the same string**, but with **all words that have five or more letters reversed**.

### Notes

Some things to keep in mind:

- _Only_ update the `solution.py` file. Any other files in this project should be left untouched.
- Strings passed in will consist of only letters and spaces.
- Spaces will be included only when more than one word is present.

### Hints

This may be a challenging exercise for some of you, so here are some clues to help point you in the right direction:

- To take a string with multiple words (such as `"Hello my friend"`) and break it up into an array (such as `["Hello","my","friend"]`), check out the [`split()` function](https://www.w3schools.com/python/ref_string_split.asp).
- Remember the `palindrome()` function in the code review exercise. The "slice statement" (`[::-1`) can be used. See [here for a detailed tutorial](https://www.w3schools.com/python/python_howto_reverse_string.asp).
- To combine an array _back_ into a string (such as `["The","Matrix","has","you"]` into `"The Matrix has you"`), check out the [`join()` function](https://www.w3schools.com/python/ref_string_join.asp).

### Examples

```
"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test"       --> "This is a test"
"This is another test" --> "This is rehtona test"
```

### Credit

This kata was borrowed from [Stop gninnipS My sdroW!](https://www.codewars.com/kata/5264d2b162488dc400000001) on [Codewars](https://https://codewars.com/).

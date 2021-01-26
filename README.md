# Coding exercise: Scrabble

Write a function that takes a string representing a list of letter tiles. Return the longest word that contains only the given tiles. Every tile does not have to be used, but every letter of the matching word must be a distinct tile: only the first example below matches "canary" since it has two A tiles.

Examples:
`scrabble("rancary")
=> canary`
`scrabble("rancry")
=> carry`

---

## `dict2array(path)`
Gets words from dictionary

### Parameters
`path : str` The file location of the dictionary
### Returns
`list` A list of string with all the words from dictionary

---

## `str2hash(str)`
Gets hash from string

### Parameters
`str : str` The string
### Returns
`dict` A dictionary of values and their counter 

---

## `hashScore(hash1, hash2)`
Get the score from comparison a 2 hashed string
### Parameters
`hash1 : dict` The hashed string
`hash2 : dict` The hashed string
### Returns
`int` A matched score 

---
## `scrabble(str)`
Gets the longest word that contains only the given tiles.
### Parameters
`str : str` The string
### Returns
`str` The longest word

---

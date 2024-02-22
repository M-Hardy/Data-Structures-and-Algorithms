"""
*LOCKED ON LEETCODE (and lintcode looks... sus)

Idea:
Prepend each word with:
1) Length of the word
2) A delimited separating the word length & the actual word
- E.g. ["apple", "banana"] -> "5$apple6$banana" -> ["apple", "banana"]


Explanation: 

The immediate problem with this question is that you need a way to 
separate each word in a given array to encode it as a single string, i.e.
you need to define a delimiter. However, nothing stops an input string
from containing our very own chosen delimiter, which presents problems 
when decoding the encoded string (using our delimiter) back to the original 
input - e.g:

Let's choose "$" as our delimiter":

["app$le"] -- ENCODED USING "$" (only one word) --> "app$le" -- DECODED USING "$" --> ["app", "le"], but should be ["app$le"]!

An encoded string could be composed by any number of substrings, and we 
can't tell what substrings compose the encoded string using a delimiter
because there's nothing that prevents them from containing our chosen 
delimiter in the first place!

What you need is a delimiter that (1) separates each substring, and (2) 
TELLS you how LONG each substring is, so that even if our chosen delimiter
is contained in a substring it is ignored it is within its length. For this 
to work, the delimiter must be PREPENDED to each substring so that we know 
in advance how many chars compose the next substring (i.e. how many chars we 
ignore interpreting our delimiter and treat it like a normal char in a 
substring). 

"""
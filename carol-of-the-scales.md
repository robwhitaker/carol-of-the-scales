*a.k.a. learning Python for Christmas*

## Intro

It's Christmas morning and you're opening Christmas gifts with the family. At least, that's what
you're supposed to be doing, but your boss called a half hour ago, excitedly shouting a series of
requests through the phone. They just had the *best* idea. Yeah, yeah, they know it's Christmas, but
it's a Christmas type idea. They just want you to write a program that can analyze Charles Dickens'
*A Christmas Carol* and figure out a couple stats about it. Then people could query the story
through *their car radios*! It's brilliant! Sales will soar!

Oh, and by the way, the program has to be written in Python because... well, your boss saw a funny
meme of a snake in a Santa Hat, and now they're convinced that snakes are the spirit animal of
Christmas and that all Christmas-themed programs must be written in "that snake language."

In the spirit of the holidays, they of course want to help you out so you can get back to your
family. That's why they sent you a [link to a free Python course][course] before hanging up the
phone.

## Problem 1

**The Boss recommends:** *Complete the [Python Course][course] from the beginning through
[Intermediate Strings][strings] before tackling this problem.*

To get started analyzing text, you'll need a handy way to break it down. And what better way to
break down text than into words! But you're still a bit lethargic from just waking up and still
a bit disgruntled from being pulled away from your stocking snacks, so better take it slow to start.

Write a Python function called `get_first_word` that takes in one argument--a string--and returns
the first word in that string. For the purposes of this problem, a word only consists of characters
in the alphabet (i.e. a-z, A-Z). If the function is given a string that does not start with a valid
word, it should just give up and return empty string.

For example:

```python
get_first_word("Christmas cookies are good.") == "Christmas"
get_first_word("Don't be a Scrooge") == "Don"
get_first_word("??? Wow") == ""
get_first_word("") = ""
```

## Problem 2

**The Boss recommends:** *Complete the file reading lessons from the [Python Course][course] before
tackling this problem:*

- *[Reading Files][files1]*
- *[Files as a Sequence][files2]*

Well, you have a function to split a sentence into words... sort of. It's time to give it a try on
your actual input. Download [A Christmas Carol][story], and save it inside your project folder as
`a-christmas-carol.txt`. Once you've done that, test your function by using it to get the first word
of the hundredth line in the text file.

What do you get? Does it match *the answer*[^ans2]?

## Problem 3

**The Boss recommends:** *No new recommendations.*

Huzzah! Your ability to break a sentence into words is... well, to be honest, it leaves something to
be desired. Maybe reporting "Hamlet" instead of "Hamlet\'s" isn't going to get you that pay raise,
but you'll have to get back to that later. Your boss just messaged you with a new requirement for
the project. It is absolutely imperative that drivers be able to query the number of paragraphs in
*A Christmas Carol*. This is now your top priority; never mind the `get_first_word` function!

Write a program that reads `a-christmas-carol.txt` and returns the number of paragraphs in it. For
this problem, a paragraph is defined as any consecutive series of non-blank lines.

For example:

```txt
It was the best of times.
It was the worst of times.

I don't know...






the rest of that story.
```

would be considered three (3) paragraphs.

What output does your program give? Does it match *the answer*[^ans3]?

## Problem 4

**The Boss recommends:** *Complete the lists lessons from the [Python Course][course] before
tackling this problem:*

- *[Python Lists][lists1]*
- *[Working with Lists][lists2]*
- *[Strings and Lists][lists3]*

Now that the urgent paragraph-counting issue is dealt with and drivers can easily find out the
number of paragraphs in *A Christmas Carol*, you can turn your attention back to the more interesting
matter of splitting a string into words. Clearly, taking only the first alphabetical characters you
see isn't quite getting you the right results. On top of that, having only the first word in
a string isn't particularly useful. It would be way better if you had a list containing ALL the
words in the string.

### 4a

Well, as it turns out, in the English language words tend to be separated by blank spaces. You can use
that! First, we'll want a better function for breaking a sentence into words. Write a `words`
function that splits up a string into a list of words. For this function, a word is defined as any
consecutive series of non-whitespace characters.

For example:

```python
words("Christmas cookies are good.") == ["Christmas", "cookies", "are", "good."]
words("Don't    be  a       Scrooge") == ["Don't", "be", "a", "Scrooge"]
words("??? Wow") == ["???", "Wow"]
words("") = []
```

**HINT:** You might want to take a look at the `split` function of the `str` class.

Now that you have your shiny new and improved `words` function, you ought to put that thing to use.
Using your `words` function, write a program that reads in `a-christmas-carol.txt` and outputs the
number of words on line 1457.

What output does your program give? Does it match *the answer*[^ans4a]?

### 4b

Oops! It looks like that `words` function was still a little bit naive. It ended up splitting:

"three\-\-had \'em up in their places\-\-four, five, six\-\-barred"

into

`["three--had", "'em", "up", "in", "their", "places--four,", "five,", "six--barred"]`

While it did a great job splitting up words by spaces, it didn't split on punctuation! Not only
that, but it left trailing commas in several of the words! You can just imagine drivers asking for
the words on line one thousand four hundred and fifty seven and the radio dumbly spitting out,
"three dash dash had 'em up in their places dash dash four comma five comma six dash dash barred!"
And never mind looking up the *meaning* of "three\-\-had." No car's gonna find *that* in the
dictionary. To fix this, you'll need to come up with a better definition of a word.

Rewrite your `words` function. For this final iteration, a word is defined as any consecutive series
of alphabetic characters, apostrophes, and hyphens where a hyphen cannot be at the beginning or end
of a word and must always be followed by an alphabetic character.

For example, the following are considered words:

- \'em
- ma\'am
- apple
- door-nail
- \'\'\'\'\'\'\'
- this-is-a\'\'\'silly-wo\'rd\'

... while these are not:

- 123
- apple-\'\'\'
- -something
- half-

With your new `words` function, the above line:

"three\-\-had \'em up in their places\-\-four, five, six\-\-barred"

should be split into:

`["three", "had", "'em", "up", "in", "their", "places", "four", "five", "six", "barred"]`

Now you can try again with this fanciest of `words` functions. How many words does it count on line
1457? Does it match *the answer*[^ans4b]?

## Problem 5

**The Boss recommends:** *Complete the dictionaries and tuples lessons from the [Python
Course][course] before tackling this problem:*

- *[Python Dictionaries][dict1]*
- *[Dictionaries: Common Applications][dict2]*
- *[Dictionaries and Loops][dict3]*
- *[The Tuples Collection][tuples1]*
- *[Comparing and Sorting Tuples][tuples2]*

With your new `words` function working as expected, you can now count words even more accurately
than Microsoft's online version of Word! Now you can really give those drivers some deep insights
about Charles Dickens' *A Christmas Carol*. For example, you could answer questions like, "What is
the seventh (7th) most common word in `a-christmas-carol.txt` and how many times does it occur?"

No, seriously, answer the question. The sooner your write a program to do it, the sooner you can get
back to your Christmas cookies!

What output does your program give? Does it match *the answer*[^ans5]?

## Problem 6

**The Boss recommends:** *Complete the objects lessons from the [Python
Course][course] before tackling this problem:*

- *[Python Objects][object1]*
- *[Objects: A Sample Class][object2]*
- *[Object Lifecycle][object3]*
- *[Objects: Inheritance][object4]*

You're just about to turn in your program to your boss *when your boss calls you*. They just had the
second best idea they've had all day (the first being to make you work on Christmas)! They've been
reading up on this hot new trend called Object Oriented Programming (you resist telling them that
it's not exactly a *new* trend) and that you absolutely *must* represent paragraphs as objects.
Customers love objects.

They were so excited about this idea that *they already wrote a program using the interface they had
in mind* and sent their program over (`objects_are_cool.py` in your project folder). You just have
to write a class to represent a paragraph according to their specs.

In your project folder, create a file called `paragraph.py`. Inside it, define a class called
`Paragraph`. Its constructor should take a string--the text of the paragraph--as a parameter. It
should also contain a method--`word_occurrences`--which takes a string (a word) and returns the
number of times that word occurs in the paragraph. This search should be case-insensitive.

**HINT:** You probably want to make use of functions you've already written.

When you have created the class, run your boss' program with `python3 objects_are_cool.py`. What
does this super cool program output? Is it the *right answer*[^ans6]?

## Merry Christmas

You've done it! You've completed your impromptu Christmas assignment and learned yourself some
Python for great good while you were at it!

**Now go eat some Christmas cookies :)**

[course]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/
[strings]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/intermediate-strings
[files1]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/reading-files
[files2]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/files-as-a-sequence
[story]: https://www.gutenberg.org/files/46/46-0.txt
[lists1]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/python-lists
[lists2]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/working-with-lists
[lists3]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/strings-and-lists
[dict1]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/python-dictionaries
[dict2]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/dictionaries-common-applications
[dict3]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/dictionaries-and-loops
[tuples1]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/the-tuples-collection
[tuples2]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/comparing-and-sorting-tuples
[object1]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/python-objects
[object2]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/objects-a-sample-class
[object3]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/object-lifecycle
[object4]: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/objects-inheritance

[^ans2]: "Hamlet"
[^ans3]: 786
[^ans4a]: 8
[^ans4b]: 11
[^ans5]: "it", occurs 531 times
[^ans6]: 2510116

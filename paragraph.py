import itertools # for an advanced solution

# Problem 1

def get_first_word(str):
    word = ""
    for char in str:
        if char.isalpha():
            word = word + char
        else:
            break
    return word

# Problem 2

def problem_2():
    handle = open('a-christmas-carol.txt', 'r')
    line_no = 0
    for line in handle:
        line_no = line_no + 1
        if line_no == 100:
            handle.close()
            return get_first_word(line)
    handle.close()

def problem_2_improved():
    # Using the "with" syntax takes care of closing the
    # file handle for us, and prevents unclosed handles
    # in case of error
    with open('a-christmas-carol.txt', 'r') as handle:
        # The use of "zip" and "itertools.count()" takes
        # care of tracking the line numbers for us, which
        # reduces the possible errors we could make by
        # manually increasing a counter
        for line_no, line in zip(itertools.count(), handle):
            if line_no == 99: # index 99 is the hundredth line
                return get_first_word(line)

# Problem 3

def problem_3():
    # Like problem 2, this solution could be improves by
    # using "with" syntax to manage the file handle
    handle = open('a-christmas-carol.txt', 'r')
    paragraph_count = 0
    last_line_was_blank = True
    for line in handle:
        # If the line is not blank
        if line != "" and not line.isspace():
            # ... and the last line was blank
            if last_line_was_blank:
                # ... this is a new paragraph, so add one
                #     to the count
                paragraph_count = paragraph_count + 1
            # Since this line wasn't blank, set the flag
            # to false
            last_line_was_blank = False
        else:
            # The line was blank, so set the flag to true
            last_line_was_blank = True
    handle.close()
    return paragraph_count

# Problem 4

def problem_4a():
    # See problem2_improved() above to see how this solution
    # could be written better
    handle = open('a-christmas-carol.txt', 'r')
    line_no = 0
    for line in handle:
        line_no = line_no + 1
        if line_no == 1457:
            handle.close()
            return len(line.split())
    handle.close()

# problem_4b
def words(line):
    words = []
    current_word = ""
    char_index = 0
    line_len = len(line)
    for char in line:
        # Figure out the next character to look ahead, in case of '--'. If there is
        # no next character, default to empty string.
        if char_index+1 < line_len:
            next_char = line[char_index+1]
        else:
            next_char = ""

        # If the current character is a letter or apostrophe, add it to the current
        # word.
        if char.isalpha() or char == "'":
            current_word = current_word + char

        # Only include a hyphen as part of the word if we are not at the beginning
        # of a word and the hyphen is followed by a letter.
        elif char == '-' and next_char.isalpha() and current_word != "":
            current_word = current_word + char

        # If this character is not part of a word but there is a current word,
        # add the current word to the list and clear the variable.
        elif len(current_word) >= 1:
            words.append(current_word)
            current_word = ""

        char_index = char_index + 1

    # If we still have a word stored in current_word,
    # add it to the word list
    if current_word != "":
        words.append(current_word)

    return words

def problem_4c():
    # See problem2_improved() above to see how this solution
    # could be written better
    handle = open('a-christmas-carol.txt', 'r')
    line_no = 0
    for line in handle:
        line_no = line_no + 1
        if line_no == 1457:
            handle.close()
            return len(words(line))
    handle.close()

# Problem 5

def second_element(tpl):
    return tpl[1]

def problem_5():
    word_counts = dict() # keep a counter for each word

    # See problem2_improved() above to see how this solution
    # could be written better
    handle = open('a-christmas-carol.txt', 'r')

    # Read the file and count the occurrences of each word
    for line in handle:
        for word in words(line):
            # Lower-case the word. Otherwise, for example,
            # "they", "They", and "THEY" would all count as
            # different words.
            word = word.lower()
            if word in word_counts:
                word_counts[word] = word_counts[word] + 1
            else:
                word_counts[word] = 1
    handle.close()

    # Turn the dictionary into a list of tuples
    word_counts_list = list(word_counts.items())
    # Sort the list according to the second element in the tuples
    # (the number of occurrences) and return it reversed (biggest
    # to smallest).
    word_counts_list.sort(key=second_element, reverse=True)
    # Return the third element in the list
    return word_counts_list[6]

# Problem 6

class Paragraph():
    def __init__(self, in_text):
        self.text = in_text

    def word_occurrences(self, search_word):
        count = 0
        for word in words(self.text):
            if word.lower() == search_word.lower():
                count = count + 1
        return count


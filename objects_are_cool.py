from paragraph import *
import itertools

with open('a-christmas-carol.txt', 'r') as handle:
    last_line_was_blank = True
    paragraphs = []
    current_paragraph = ""

    for line in handle:
        if line != "" and not line.isspace():
            current_paragraph = current_paragraph + line
            last_line_was_blank = False
        else:
            if not last_line_was_blank:
                paragraphs.append(Paragraph(current_paragraph))
                current_paragraph = ""
            last_line_was_blank = True

    ans = []
    ans.append(str(paragraphs[19].word_occurrences("door-nail")))
    ans.append(str(paragraphs[22].word_occurrences("scrooge")))
    ans.append(str(paragraphs[25].word_occurrences("O'CLOCK")))
    ans.append(str(paragraphs[154].word_occurrences("other")))
    ans.append(str(paragraphs[401].word_occurrences("cuffs")))
    ans.append(str(paragraphs[401].word_occurrences("as")))
    ans.append(str(paragraphs[402].word_occurrences("and")))
    print(''.join(ans))



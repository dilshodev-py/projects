def sort_words_by_numbers(text):
    words = text.split()
    wordsDq = {}
    for word in words:
        for char in word:
            if char.isdigit():
                wordsDq[int(char)] = word
                break
    sorted_words = [wordsDq[key] for key in sorted(wordsDq.keys())]
    return ' '.join(sorted_words)

input_text = "name2 is3 My1 John4 .5 you7 Are8 ?9"
output_text = sort_words_by_numbers(input_text)
print(input_text)
print(output_text)
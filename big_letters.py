"""Replace input with self-made big letters."""

big_letters = {
    "let_a": [" ,===, ", "||   ||", "||===||", "||   ||", "!!   !!"],
    "let_b": [", ===, ", "||   ||", "||===' ", "||   ||", "''===' "],
    "let_c": [" ,===,", "||    ", "||    ", "||    ", "''==='"],
    "let_d": [",====, ", "||   ||", "||   ||", "||   ||", "'====' "],
    "let_e": [",=====,", "||     ", "||===  ", "||     ", "'====='"],
    "let_f": [",=====,", "||     ", "||===  ", "||     ", "!!     "],
    "let_g": [" ,===, ", "||    '", "||  ,,,", "||   ||", " '===' "],
    "let_h": [",,   ,,", "||   ||", "||===||", "||   ||", "!!   !!"],
    "let_i": [",,", "||", "||", "||", "!!"],
    "let_j": ["   ,,", "   ||", "   ||", "   ||", "'==''"],
    "let_k": [",,  ,,", "|| // ", "||<(  ", "|| \\\\ ", "!!  \\\\"],
    "let_l": [",,    ", "||    ", "||    ", "||    ", "'===='"],
    "let_m": [",,    ,,", "||\\  /||", "||\\\\//||", "|| '' ||", "!!    !!"],
    "let_n": [",,,  ,,", "||\\  ||", "||\\\\ ||", "|| \\\\||", "!!  '!!"],
    "let_o": [" ,===, ", "||   ||", "||   ||", "||   ||", " '===' "],
    "let_p": [", ===, ", "||   ||", "||===' ", "||     ", "!!     "],
    "let_q": [" ,===,  ", "||   || ", "||   || ", "||   || ", " '==='=="],
    "let_r": [", ===, ", "||   ||", "||===.'", "||  || ", "!!   !!"],
    "let_s": [" ,====,", "||     ", " '===, ", "     ||", "'====' "],
    "let_t": ["==,==,==", "   ||   ", "   ||   ", "   ||   ", "   !!   "],
    "let_u": [",,   ,,", "||   ||", "||   ||", "||   ||", " '===' "],
    "let_v": [",,   ,,", "\\\\   //", " \\\\ // ", "  \\!/  ", "   v   "],
    "let_w": [",,    ,,", "||    ||", "||    ||", "|| || ||", " '=''=' "],
    "let_x": [",,   ,,", " \\\\ // ", "  :x:  ", " // \\\\ ", "!!   !!"],
    "let_y": [",,    ,,", " \\\\  // ", "  \\\\//  ", "   ||   ", "   !!   "],
    "let_z": [",====,", "   // ", "  //  ", " //   ", "'===='"],
    "let_ ": ["   ", "   ", "   ", "   ", "   "],
    "let_-": ["   ", "   ", "===", "   ", "   "],
    "let_~": ["|   |", " | | ", "  |  ", " | | ", "|   |"],
}


def capitalize(sentence, line_length):
    """Capitalize the input."""
    part_list = split_sentence(sentence, line_length)
    for part in part_list:
        # for every part of the sentence,
        for num in range(5):
            # 5 times,
            print(" ")
            # with newlines in between,
            for char in part:
                # for every character in the part,
                try:
                    print(big_letters["let_" + char.lower()][num], end=' ')
                    # print, from the dictionary big_letters, the xth item
                    # (num) of corresponding list; end with space instead
                    # of a new line
                except KeyError:
                    print(big_letters["let_~"][num], end=' ')
                    # but if no corresponding key is found for character,
                    # print 'let_!' from the dictionary, which is a big X


def split_sentence(sentence, line_length):
    """Split the sentence into parts to print out."""
    word_list = sentence.split()
    part_list = []
    current_part = ""
    for word in word_list:  # for every word in the word list,
        if len(current_part + word) <= int(line_length):
            # if length of current part + current word is less than allowed:
            current_part += word + " "  # add word and space to current_part
        elif len(word) > int(line_length):
            # else, if word length is longer than allowed:
            part_list.append(current_part[:-1])
            current_part = ""
            # add current_part to word_list (except last character, which
            # is a space) and make current_part an empty string
            for char in range(0, len(word), int(line_length)):
                # then, for every xth character in the word, starting at the
                # first character:
                current_part += word[char:char + int(line_length)]
                # make a slice, starting at current character, and ending
                # before the xth character, and put it in current_part
                if len(current_part) == int(line_length):
                    # if length of current_part is same as allowed length:
                    part_list.append(current_part)
                    # put current_part in part_list
                    current_part = ""
                else:
                    current_part += " "
        else:
            # but if length of current part + current word is longer than
            # allowed, and word length is shorter than allowed:
            part_list.append(current_part[:-1])
            current_part = ""
            current_part += word + " "
            # put current_part (except last character, which is a space),
            # in part_list, make current_part empty, and put word in
            # current_part
    part_list.append(current_part[:-1])
    return part_list


def update_history(history_list, sentence):
    """Update the history list."""
    history_list.append(sentence)
    if len(history_list) > 10:
        del history_list[0]


def run_program():
    """Run the program."""
    history_list = []
    while True:
        history_or_new = input("Would you like to write a new sentence (a), "
                               "or pick a previous sentence from the history "
                               "(b)? a/b: ")
        if history_or_new == "b":
            if history_list == []:
                print("History is currently empty! ")
                sentence = input("Type a sentence: ")
                update_history(history_list, sentence)
            else:
                for index, item in enumerate(history_list, start=1):
                    print(str(index) + ". " + item)
                choice = input("Choose a sentence: ")
                sentence = history_list[int(choice) - 1]
        else:
            sentence = input("Type a sentence: ")
            update_history(history_list, sentence)
        line_length = input("What is the max number of characters per line? ")
        capitalize(sentence, line_length)
        run_again = input("\n\nWould you like to run this program again? y/n: ")
        if run_again == "y":
            continue
        else:
            print("\nThank you for using this program!")
            break


run_program()

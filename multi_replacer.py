# This will work only whole words (or single characters) that are separated with white characters or punctuation marks.
# See what is stored under "omitted_characters" variable to check, what characters are being omitted.

def find_first_breakpoint(str, breakpoints):
    # print("str: ", str)
    for i in range(len(str)):
        ch = str[i]
        if ch in breakpoints:
            return i
    return len(str)


def main():
    input_filename = input("Enter the name of the INPUT file: ")
    output_filename = input("Enter the name of the OUTPUT file: ")

    replacements = {}
    entering_phrases = True
    while entering_phrases:
        to_replace = input("Content to be replaced: ")
        replace_with = input("The content that will be inserted instead: ")
        replacements[to_replace] = replace_with

        entering_phrases_user_answer = input("Continue? (ENTER / any other key)")
        if entering_phrases_user_answer != '':
            entering_phrases = False

    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')

    omitted_characters = "~`!@#$%^&*()-=+[]{}|\\;:'\",<.>/? \n\t"

    input_content_lines = input_file.readlines()
    for line in input_content_lines:
        i = 0
        new_line = ""
        while i < len(line):
            # print("i: ", i)
            breakpoint = find_first_breakpoint(line[i:-1], omitted_characters)
            if breakpoint == 0: # First character needs to be omitted
                new_line += line[i]
                i += 1
            else:
                # print("(0) breakpoint: ", breakpoint)
                word = line[i:breakpoint+i]
                # print("word: ", word)
                if word != '':
                    if word in replacements.keys():
                        new_line += replacements[word]
                    else:
                        new_line += word
                i += breakpoint
        # print("new_line: ", new_line)
        output_file.write(new_line)


if __name__ == "__main__":
    main()

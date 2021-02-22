# String analyser
# Reads all the words in a string and creates
# a dictionary of their frequencies

# Aurélien Ammeloot, 2021

import typing

# Analyse_string
def analyse_string(text: str) -> dict:

    # Create an empty dictionary
    result = {}

    individual_words = text.split(" ")
    # temporarily
    #print(text)
    #print(individual_words)

    # Loop all words in list
    for current_word in individual_words:
        # If it's already in dict just increment the counter
        if current_word in result.keys():
            result[current_word] += 1
        # Otherwise create the entry and set it to one
        else:
            result[current_word] = 1

    return result

# Analyse_file
def analyse_file(filename: str) -> dict:

    # Open the file as readonly
    fp = open(filename)

    # Import all the lines of text
    file_lines = fp.readlines()
    fp.close()

    # Create an empty dictionary
    result = {}

    # Make a line-by-line loop
    for single_line in file_lines:
        individual_words = single_line.split(" ")

        # Loop all words in list
        for current_word in individual_words:

            # Treat the word remove whitespace and all lowercase
            current_word = current_word.strip()
            current_word = current_word.lower()

            # Ensuring we only count "pure" words
            if current_word.isalpha():
                # If it's already in dict just increment the counter
                if current_word in result.keys():
                    result[current_word] += 1
                # Otherwise create the entry and set it to one
                else:
                    result[current_word] = 1

    return result



r = analyse_file("alice.txt")

# Create the CSV file
fp = open("output.csv", "w")

for k in r.keys():
    fp.write(k + "," + str(r[k]) + "\n")

fp.close()

    #print(k,":",r[k])





'''r = analyse_string("""Alice was beginning to get very tired of sitting by her sister on the
bank, and of having nothing to do: once or twice she had peeped into
the book her sister was reading, but it had no pictures or
conversations in it, “and what is the use of a book,” thought Alice
“without pictures or conversations?”""")

print("The words and their frequencies:")
for key in r.keys():
    print(key, "appears", r[key], "time(s)")'''


import typing

# Read the content of a text file
# 1 Open the text file

f = open("alice.txt")

# Lines of the text
l = f.readlines()

f.close()


# Display the first 10 lines of the text
for index in range(10):
    print(l[index])

lh = l[100]

# Split a line of text into a list of words
print(lh)
lhs = lh.split(" ")

# Work with the words, individually
for word in lhs:
    print(word)


# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as file:
        contents = file.read()
    return contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text= text.lower()
    text = text.split()
    text= [word.strip('.,?') for word in text]

    unique_words= []
    for word in text:
        if word not in unique_words:
            unique_words.append(word)

    new_dic= {}
    for word in unique_words:
        count= text.count(word)
        new_dic.update({word:count})
    return new_dic

# final_dictionary= count_words()

print(count_words())
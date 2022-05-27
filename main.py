# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from importlib.resources import contents


def read_file_content(filename):
    # [assignment] Add your code here 
    file = open (filename, 'r')
    f_content =file.read()

    return (f_content)
    

def count_words():
    texts = read_file_content("./story.txt")


    words = texts.split()
    dict_of_counts = {item:words.count(item) for item in words}
    print(dict_of_counts)
    
    # return {"as": 10, "would": 20}


    
count_words()
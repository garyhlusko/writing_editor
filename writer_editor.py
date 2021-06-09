# writer_editor.py

# returns word count in sentence 
def word_count(sentence):
    # sentence -> word string
    words = sentence.split(" ")
    return len(words)

# get length of words in each sentence
def sentence_length(paragraphs):
    sentence_array = []
    paragraphs_list = paragraphs.split(".")
    for sentence in paragraphs_list:
        sentence_array.append(word_count(sentence))
    print("here is a length of each sentence")
    for sentence in sentence_array:
        print("{} words".format(sentence))

# get start of the sentence
def start_of_sentence(paragraphs):
    pass 

# get if sentence is passive
def sentence_passive(paragraphs):
    pass

# common_words 
def get_common_words(paragraphs):
    pass 


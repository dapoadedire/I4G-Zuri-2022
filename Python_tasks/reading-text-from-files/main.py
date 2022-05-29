# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
     with open(filename, 'r') as f:
         contents = f.read()
         return contents
         f.close()


def count_words():
     text = read_file_content("./story.txt")
    # [assignment] Add your code here
     words = text.split()
     words_counter = {}
     for word in words:
          #filter punctuation and convert to lowercase
           import string
           word = word.translate(word.maketrans('', '', string.punctuation))
           
           if word in words_counter:
                words_counter[word] += 1
           else:
                words_counter[word] = 1
               
     return words_counter


#print(count_words())


word = "The cake is done, , , It is a big cake!"
word = word.strip(,)
print(word)
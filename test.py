#with open('more_used_keywords.txt', 'w') as most_used_keywords:
#    pass

def search_engine(**keyword):
    search_words= {}
    search_text = input('Tell you AI your mood with 3 words: ') 
    for word in search_text:
        search_words[search_text] = keyword
    print(search_words)
search_engine()


#def my_function(**kid):
#  print("His last name is " + kid["lname"])
#
#my_function(fname = "Tobias", lname = "Refsnes")
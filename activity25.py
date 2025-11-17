# Dictionary
programming_language = ['Java','C#','C++','python','Pearl','Go Lang','JavaScripyt']

print(programming_language[-1])
# INDEX                   0      1    2      3        4        5           6
proglang_dictionary = {'mahirap daw':'Java','ano ba yan':'C#','d ko alam':'C++','favorite':'python','mukang madali':'Pearl','mahirap ata':'Go Lang','sobrang hirap':'JavaScripyt'}

print(proglang_dictionary['favorite'])

proglang_dictionary['madali lang'] = 'html'

print(proglang_dictionary)

# DELETING VALUE IN DICTIONARY USING A KEY
proglang_dictionary.pop('mahirap daw')

print(proglang_dictionary)
# proglang_dictionary('keys')
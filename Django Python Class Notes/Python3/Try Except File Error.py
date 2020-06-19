# try: 
#     with open('Django Python Class Notes/file2.txt', 'r') as file:
#         file = file.read()
#         print(file)
# except FileNotFoundError:
#     print('file does not exist')  # file does not exist


# try:    #  corrected name error  I was ahead of the instructor  ******** he, he, he
#     with open('Django Python Class Notes/file.txt', 'r') as file:
#         file = file.read()
#         print(file)
# except FileNotFoundError:
#     print('file does not exist')  # hi


# try:   
#     with open('Django Python Class Notes/file.txt', 'r') as file:
#         file = file.read()
        
# except FileNotFoundError:
#     print('file does not exist')
    
# else:
#     words = file.split()
#     num_words = len(words)
#     print('the file ' + file + 'has about ' + str(num_words) + ' words')  # the file has about 0 words



# def count_words(filename):
#     """ count the number of words in the file """
#     try:
#         with open(filename) as file:
#             file = file.read()
#     except FileNotFoundError:
#         msg = 'Sorry, the file {} does not exist'.format(filename)
#         print(msg)
#     else:
#         """ count the number of words in the file """
#         word = file.split()
#         num_word = len(word)
#         print('the file {} words'.format(filename, num_word))
# filename = 'alice.txt'  # Sorry, the file alice.txt does not exist
# count_words(filename)



# def count_words(filename):
#     """ count the number of words in the file """
#     try:
#         with open(filename) as file:
#             file = file.read()
#     except FileNotFoundError:
#         msg = 'Sorry, the file {} does not exist'.format(filename)
#         print(msg)
#     else:
#         """ count the number of words in the file """
#         word = file.split()
#         num_word = len(word)
#         print('the file {} has about {} words'.format(filename, num_word))
# filename = 'Django Python Class Notes/file.txt'  # the file Django Python Class Notes/file.txt has about 2 words
# count_words(filename)


def count_words(filename):
    """ count the number of words in the file """
    try:
        with open(filename) as file:
            file = file.read()
    except FileNotFoundError:
        msg = 'Sorry, the file {} does not exist'.format(filename)
        print(msg)
    else:
        """ count the number of words in the file """
        word = file.split()
        num_word = len(word)
        print('the file {} has about {} words'.format(filename, num_word))
filenames = ['Django Python Class Notes/file.txt', 'Django Python Class Notes/carl.txt',  'Django Python Class Notes/carl1.txt', 'Django Python Class Notes/carl2.txt', 'Django Python Class Notes/rich.txt']

for filename in filenames:
    count_words(filename)
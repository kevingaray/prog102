import optparse

opts = optparse.OptionParser()

opts.add_option("-f", "--file", dest='fname', help="This is the file name that you would like to read")
opts.add_option("-w", "--word", dest='word', help="This is the word that you would like to search")
# run 'python  words.py -f romeo -w from'

(options, arguments) = opts.parse_args()

file = open(options.fname, 'r')
counter = 0

for line in file:
    words = line.split()
    for word in words:
        if word == options.word:
            counter += 1

print(counter)

# run 'python3 review_file.py -i "name"'
# example 'python3 review_file.py -i build0'

import optparse
opts = optparse.OptionParser()
opts.add_option("-i", "--interfaz", dest='interfaz', help="This is the interfaz name that you would like to read")

(options, arguments) = opts.parse_args()

file = open('full_walk.txt', 'r')

index = 0
# find index
for line in file:
    values = line.split()
    if values[0][0:20] == '.1.3.6.1.2.1.2.2.1.2' and values[-1] == options.interfaz:
        index = values[0][-1]
        break;

if int(index) > 0:
    print(f'{options.interfaz} have index {0}')
    results = []
    for line in file:
        values = line.split()
        if values[0][-1]==index:
            results.append(f'{values[0][0:20]} = {values[2]} {values[-1]}')

    for i in range(10):
        print(results[i])

else:
    print(f'{options.interfaz} not found')



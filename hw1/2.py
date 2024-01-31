
text = open(r'hw1\2text.txt', 'r')

for line in text:
    pr = line.replace(f'%%', '')
    if '##' in line:
        continue
    print(pr)
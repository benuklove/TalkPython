"""

  Created on 7/4/2017 by Ben

  benuklove@gmail.com
  
  

"""

data = []
with open('booklist.txt', 'r') as fin:
    for item in fin.readlines():
        item = item.strip()
        if item != '+' and item != '':
            data.append(item)

# print(data)

with open('ebooks.txt', 'w', encoding='utf-8') as fout:
    for idx, book in enumerate(data):
        fout.write('{}. {}'.format(idx, book) + '\n')

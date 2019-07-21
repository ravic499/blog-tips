search_fruit = 'apple'
fruit_box = ['banana', 'mango', 'apple', 'pineapple']

for fruit in fruit_box:
    if fruit == search_fruit:
        print('Found fruit : {}'.format(search_fruit))
        break
else:
    print('{} fruit not found'.format(search_fruit))

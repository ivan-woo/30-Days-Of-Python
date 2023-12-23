import random
import string

num_characteres = int(input('Input number of characters:'))
num_ids = int(input('Input number of IDs to generate:'))

def random_user_id():
    ids = []
    for num in range(num_ids):
        ids.append(''.join(random.choices(string.ascii_letters + string.digits, k=num_characteres)))
    return ids
print(random_user_id())

def rgb_color_gen():
    return f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
print(rgb_color_gen())

def list_of_hexa_colors(num):
    list = []
    for number in range(num):
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
        list.append(color)
    return list
print(list_of_hexa_colors(6))
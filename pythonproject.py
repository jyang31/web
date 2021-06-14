import matplotlib.pyplot as plt
from random import shuffle

hundred_words_file = open("100words.txt",encoding='utf8')
text = hundred_words_file.read()

def split_list(list):
    new_split_list = list.split('\n')
    new_character_list = []
    for word in new_split_list:
        for character in word:
            new_character_list.append(character)
    return new_character_list

list_of_characters = split_list(text)


def make_histogram_lists(characterlist):
    list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_of_a = []
    list_of_b = []
    list_of_c = []
    list_of_d = []
    list_of_e = []
    list_of_f = []
    list_of_g = []
    list_of_h = []
    list_of_i = []
    list_of_j = []
    list_of_k = []
    list_of_l = []
    list_of_m = []
    list_of_n = []
    list_of_o = []
    list_of_p = []
    list_of_q = []
    list_of_r = []
    list_of_s = []
    list_of_t = []
    list_of_u = []
    list_of_v = []
    list_of_w = []
    list_of_x = []
    list_of_y = []
    list_of_z = []
    for character in characterlist:
        if character == list_of_letters[0]:
            list_of_a.append(character)
        if character == list_of_letters[1]:
            list_of_b.append(character)
        if character == list_of_letters[2]:
            list_of_c.append(character)
        if character == list_of_letters[3]:
            list_of_d.append(character)
        if character == list_of_letters[4]:
            list_of_e.append(character)
        if character == list_of_letters[5]:
            list_of_f.append(character)
        if character == list_of_letters[6]:
            list_of_g.append(character)
        if character == list_of_letters[7]:
            list_of_h.append(character)
        if character == list_of_letters[8]:
            list_of_i.append(character)
        if character == list_of_letters[9]:
            list_of_j.append(character)
        if character == list_of_letters[10]:
            list_of_k.append(character)
        if character == list_of_letters[11]:
            list_of_l.append(character)
        if character == list_of_letters[12]:
            list_of_m.append(character)
        if character == list_of_letters[13]:
            list_of_n.append(character)
        if character == list_of_letters[14]:
            list_of_o.append(character)
        if character == list_of_letters[15]:
            list_of_p.append(character)
        if character == list_of_letters[16]:
            list_of_q.append(character)
        if character == list_of_letters[17]:
            list_of_r.append(character)
        if character == list_of_letters[18]:
            list_of_s.append(character)
        if character == list_of_letters[19]:
            list_of_t.append(character)
        if character == list_of_letters[20]:
            list_of_u.append(character)
        if character == list_of_letters[21]:
            list_of_v.append(character)
        if character == list_of_letters[22]:
            list_of_w.append(character)
        if character == list_of_letters[23]:
            list_of_x.append(character)
        if character == list_of_letters[24]:
            list_of_y.append(character)
        if character == list_of_letters[25]:
            list_of_z.append(character)
    list_of_lists = []
    list_of_lists.append(list_of_a)
    list_of_lists.append(list_of_b)
    list_of_lists.append(list_of_c)
    list_of_lists.append(list_of_d)
    list_of_lists.append(list_of_e)
    list_of_lists.append(list_of_f)
    list_of_lists.append(list_of_g)
    list_of_lists.append(list_of_h)
    list_of_lists.append(list_of_i)
    list_of_lists.append(list_of_j)
    list_of_lists.append(list_of_k)
    list_of_lists.append(list_of_l)
    list_of_lists.append(list_of_m)
    list_of_lists.append(list_of_n)
    list_of_lists.append(list_of_o)
    list_of_lists.append(list_of_p)
    list_of_lists.append(list_of_q)
    list_of_lists.append(list_of_r)
    list_of_lists.append(list_of_s)
    list_of_lists.append(list_of_t)
    list_of_lists.append(list_of_u)
    list_of_lists.append(list_of_v)
    list_of_lists.append(list_of_w)
    list_of_lists.append(list_of_x)
    list_of_lists.append(list_of_y)
    list_of_lists.append(list_of_z)
    list_of_numbers = []
    for listofletters in list_of_lists:
        list_of_numbers.append(len(listofletters))
    return list_of_numbers

big_list_of_lists = make_histogram_lists(list_of_characters)

def make_histogram(list_of_values):
    list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    plt.bar(list_of_letters, list_of_values)
    plt.title('Histogram of Most Common Letters in the Given List of Words')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.show()

make_histogram(big_list_of_lists)

def make_list_of_words(big_file):
    list_of_words = big_file.split('\n')
    return list_of_words

def make_scrambled_list(wordlist):
    scrambled_list = []
    for word in wordlist:
        word = list(word)
        shuffle(word)
        scrambled_list.append(word)
    newlist = []
    for element in scrambled_list:
        newelement = "".join(element)
        newlist.append(newelement)
    return newlist

list_of_words = make_list_of_words(text)
print(make_scrambled_list(list_of_words))




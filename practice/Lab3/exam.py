# change file to list
def get_words_list():
    l = []
    with open("/Users/a123/Desktop/words.txt", "r") as f1:
        for i in f1:
            words = i.strip()
            l.append(words)
    l.append("luoyinzhuo")
    return l


# compare two words
def is_anagram(s1, s2):
    s1 = list(s1)
    s1.sort()
    s2 = list(s2)
    s2.sort()
    if s1 == s2:
        return True
    else:
        return False


# add keys and values to dictionary
def get_all_sets(l):
    index = 0
    lis = []
    d = {}  # an ordinary dictionary
    for i in l:
        for j in l[l.index(i) + 1:]:
            if is_anagram(i, j):
                d.setdefault(i, []).append(j)
                l.remove(j)
    for i in d:
        k = [i]
        v = list(d[i])
        k.extend(v)
        lis.append(k)
    # sort list
    len_list = sorted(lis, key=lambda little_list: len(little_list), reverse=True)
    # return len_list
    for i in len_list:
        print(i)
        # return lis


r = get_words_list()
get_all_sets(r)

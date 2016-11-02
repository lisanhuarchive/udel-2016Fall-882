from queue import PriorityQueue as PQ
from math import log2

ngram = 5
window_length = 5
default_keyboard = ' .,?!;:-"\
qwertyuiop\
asdfghjkl$\
zxcvbnm*()\
1234567890\
&@\'%/[]{}#'


def get_from_dict(key, d: dict):
    if key not in d:
        return 0.5
    if d[key] == 0:
        return 0.5
    return d[key]


def try_training():
    file = open('SanhuLi.txt')
    text = ''.join(file.readlines())
    stat = {}
    print(text)
    training(text, stat)
    print(stat)


def get_char(text: str, index: int):
    if index in range(len(text)):
        return text[index].lower()
    return ''


def add_one_occ(d: dict, ch, key):
    ref = key + ch
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
    if ref in d:
        d[ref] += 1
    else:
        d[ref] = 1


def get_key(text):
    key = [get_char(text, len(text) - i - 2) for i in range(ngram)]
    key.reverse()
    key = ''.join(key)
    return key


def check_freq(text: str, statistics: dict, keyboard=default_keyboard):
    prob = 0
    # for i in range(len(text)):
    #     prob += get_freq(text[i], get_key(text), statistics)
    candidates = PQ()
    for c in keyboard:
        np = prob + get_freq(c, get_key(text + c), statistics)
        ele = -np, c
        candidates.put(ele)
    return candidates
    # if len(previous) >= ngram:
    #     del previous[0]
    # previous.append(current_c)
    # prev = ''.join(previous)
    # candidates = PQ()
    # for c in keyboard:
    #     if (c, prev) not in statistics:
    #         candidates.put((-0.5, c))
    #     else:
    #         candidates.put((-statistics[(c, prev)], c))
    # return candidates


def training(text: str, statistics: dict):
    for i in range(len(text)):
        key = [get_char(text, i - j - 1) for j in range(ngram)]
        key.reverse()
        key = ''.join(key)
        ch = text[i]
        add_one_occ(statistics, ch, key)
    return statistics


def get_wnd_from_pq(q: PQ):
    wnd = []
    while len(wnd) < window_length:
        ele = q.get_nowait()
        # print(ele)
        if ele[1] != ' ':
            wnd.append(ele[1])
    return wnd


def get_freq(ch: str, key: str, stats: dict):
    return log2(get_from_dict(key + ch, stats)) - log2(get_from_dict(key, stats))


def predict(text: str, stats: dict):
    candidates = check_freq('', stats)
    print(''.join(get_wnd_from_pq(candidates)))
    for i in range(len(text)):
        t = text[:i + 1]
        candidates = check_freq(t, stats)
        window = get_wnd_from_pq(candidates)
        print(''.join(window))

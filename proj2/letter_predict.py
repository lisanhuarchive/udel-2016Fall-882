from queue import PriorityQueue as PQ

ngram = 10
window_length = 5
default_keyboard = ' .,?!;:-"\
qwertyuiop\
asdfghjkl$\
zxcvbnm*()\
1234567890\
&@\'%/[]{}#'


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
    ref = ch, key
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
    if ref in d:
        d[ref] += 1
    else:
        d[ref] = 1


def check_freq(current_c, statistics: dict, keyboard=default_keyboard, previous=[]):
    if len(previous) >= ngram:
        del previous[0]
    previous.append(current_c)
    prev = ''.join(previous)
    candidates = PQ()
    for c in keyboard:
        if (c, prev) not in statistics:
            candidates.put((-0.5, c))
        else:
            candidates.put((-statistics[(c, prev)], c))
    return candidates


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


def predict(text: str, model: dict):
    window = []
    candidates = check_freq('', model)
    print(''.join(get_wnd_from_pq(candidates)))
    for c in text:
        candidates = check_freq(c, model)
        window = get_wnd_from_pq(candidates)
        print(''.join(window))
        window = []

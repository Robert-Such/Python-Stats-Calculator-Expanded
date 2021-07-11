from collections import Counter


def mode(data):
    array_length = len(data)

    CounterData = Counter(data)
    get_mode = dict(CounterData)
    mode = [k for k, v in get_mode.items() if v == max(list(CounterData.values()))]

    if len(mode) == array_length:
        get_mode = "No mode found"
    else:
        get_mode = mode[0]

    return(int(get_mode))
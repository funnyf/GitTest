from random import sample


def make_kfold_range(length, k):
    quotient, remainder = length // k, length % k
    trains, vals = [], []
    indices = sample(range(length), length)  # shuffle indices

    if k <= 1:
        return [(indices, [])]
    for num in range(k):
        start, end = 0, quotient
        tmp = []
        for cnt in range(k):
            if num == cnt:
                end += remainder
                vals.append(indices[start:end])
            else:
                tmp.extend(range(start, end))
            start, end = end, end + quotient
        r = [indices[idx] for idx in tmp]
        trains.append(r)
    return list(zip(trains, vals))

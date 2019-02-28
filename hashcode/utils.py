def load(filename):
    with open(filename) as f:
        l = f.readlines()
    entries = [x.split() for x in l[1:]]
    entries = [(x[0], set(x[2:])) for x in entries]


def score_two_slides(i, j, images):
    intersect = list(set(images[i]) & set(images[j]))
    tags1 = list(set(images[i]) - set(images[j]))
    tags2 = list(set(images[j]) - set(images[i]))
    return min(len(intersect), len(tags1), len(tags2))

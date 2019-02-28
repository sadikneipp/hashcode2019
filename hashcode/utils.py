def load(filename):
    with open(filename) as f:
        l = f.readlines()
    entries = [x.split() for x in l[1:]]
    entries = [(x[0], set(x[2:])) for x in entries]
    return entries


def score_tags(i, j):
    return min(len(i & j), len(i - j), len(j - i))


def score_two_slides(i, j, images):
    intersect = list(set(images[i]) & set(images[j]))
    tags1 = list(set(images[i]) - set(images[j]))
    tags2 = list(set(images[j]) - set(images[i]))
    return min(len(intersect), len(tags1), len(tags2))


def score_all(solution):
    assert all(x[0] == 'H' for x in solution)
    return sum(score_tags(a[1], b[1]) for a, b in zip(solution[::2], solution[1::2]))


def format_submission(photos, solution, filename):
    ref_to_index = {id(x): i for i, x in enumerate(photos)}
    with open(filename, 'w') as f:
        f.write('{}\n'.format(len(photos)))
        for x in solution:
            f.write('{}\n'.format(ref_to_index[id(x)]))
    print('Solution score: {} saved to {}'.format(score_all(solution), filename))

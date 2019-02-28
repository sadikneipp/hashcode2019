def load(filename):
    with open(filename) as f:
        l = f.readlines()
    entries = [x.split() for x in l[1:]]
    entries = [(x[0], i, set(x[2:])) for i, x in enumerate(entries)]
    return entries


def score_tags(i, j):
    return min(len(i & j), len(i - j), len(j - i))

def score_two_slides(i, j, images):
    intersect = list(set(images[i]) & set(images[j]))
    tags1 = list(set(images[i]) - set(images[j]))
    tags2 = list(set(images[j]) - set(images[i]))
    return min(len(intersect), len(tags1), len(tags2))


def score_all(solution):
    # assert all(x[0] == 'H' for x in solution)
    return sum(score_tags(a[2], b[2]) for a, b in zip(solution[::], solution[1::]))


def score_all_2(solution, second):
    # assert all(x[0] == 'H' for x in solution)
    return sum(score_tags(a[2] | c[2], b[2] | d[2]) for a, b, c, d in zip(solution[::], solution[1::], second[::], second[1::]))

def format_submission(solution, filename):
    with open(filename, 'w') as f:
        f.write('{}\n'.format(len(solution)))
        for x in solution:
            if x[0] == 'H':
                f.write('{}\n'.format(x[1]))
            else:
                f.write('{} {}\n'.format(x[1][0], x[1][1]))
    print('Solution score: {} saved to {}'.format(score_all(solution), filename))

    
def format_submission_2(photos, solution, filename):
    ref_to_index = {id(x): i for i, x in enumerate(photos)}
    with open(filename, 'w') as f:
        f.write('{}\n'.format(len(photos)))
        for x in solution:
            f.write('{}\n'.format(ref_to_index[id(x)]))
    print('Solution score: {} saved to {}'.format(score_all(solution), filename))

    
    
def format_submission_3(photos, solution, second, filename):
    ref_to_index = {id(x): i for i, x in enumerate(photos)}
    with open(filename, 'w') as f:
        f.write('{}\n'.format(len(photos)))
        for x, y in zip(solution, second):
            f.write('{} {}\n'.format(ref_to_index[id(x)], ref_to_index[id(y)]))
    print('Solution score: {} saved to {}'.format(score_all(solution), filename))
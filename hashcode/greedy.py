from collections import deque

from hashcode.utils import *


def delete_nth(d, n):
    # TODO optimize
    d.rotate(-n)
    d.popleft()
    d.rotate(n)


def solve(photos):
    assert all(x[0] == 'H' for x in photos)
    photos = deque(x[1] for x in photos)
    solution = [photos.popleft()]

    while photos:
        best = best_index = 0
        # best_index = max(range(len(photos)), key=score_tags(solution[-1], photos.__getitem__)))
        for i, photo in enumerate(photos):
            # score = max(photos, key=lambda x: score_tags(solution[-1], x))
            score = score_tags(solution[-1], photo)
            if score > best:
                best = score
                best_index = i
        print(best, len(photos), score_tags(solution[-1], photos[best_index]), len(solution[-1] & photos[best_index]), len(solution[-1] - photos[best_index]), len(photos[best_index] - solution[-1]))
        solution.append(photos[best_index])
        delete_nth(photos, best_index)
        if len(photos) % 20:
            print(len(photos))

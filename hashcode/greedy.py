from collections import deque

from hashcode.utils import *


def delete_nth(d, n):
    # TODO optimize
    d.rotate(-n)
    d.popleft()
    d.rotate(n)


def solve(input_photos):
    assert all(x[0] == 'H' for x in input_photos)
    photos = deque(x for x in input_photos)
    solution = [photos.popleft()]

    while photos:
        best = best_index = 0
        best_index = max(range(min(len(photos), 10)), key=lambda i: score_tags(solution[-1][1], photos[i][1]))
        # for i, photo in enumerate(photos):
        #     # score = max(photos, key=lambda x: score_tags(solution[-1], x))
        #     score = score_tags(solution[-1], photo)
        #     if score > best:
        #         best = score
        #         best_index = i
        # print(best, len(photos), score_tags(solution[-1][1], photos[best_index][1]), len(solution[-1][1] & photos[best_index][1]), len(solution[-1][1] - photos[best_index][1]), len(photos[best_index][1] - solution[-1][1]))
        solution.append(photos[best_index])
        delete_nth(photos, best_index)
        if not len(photos) % 500:
            print('Left: {} - score {}'.format(len(photos), score_all(solution)))
    format_submission(input_photos, solution, 'greedy.txt')

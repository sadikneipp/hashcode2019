from collections import deque

from hashcode.utils import *


def delete_nth(d, n):
    # TODO optimize
    d.rotate(-n)
    d.popleft()
    d.rotate(n)


def solve(input_photos):
    assert all(x[0] == 'H' for x in input_photos)
    photo_to_i = {id(x): i for i, x in enumerate(input_photos)}
    tags = {}
    for photo in input_photos:
        for tag in photo[2]:
            tags.setdefault(tag, [])
            tags[tag].append(photo)
    total = len(input_photos)
    photos = deque(x for x in input_photos)
    solution = [photos.popleft()]
    photo_to_i[id(solution[0])] = None

    while total != len(solution):
        possible_pairs = []
        for tag in solution[-1][-1]:
            possible_pairs = possible_pairs + tags[tag]
        best = 0
        best_photo = None
        for photo in possible_pairs:
            if photo_to_i[id(photo)] is None:
                continue
            score = score_tags(solution[-1][-1], photo[-1])
            if score > best:
                best = score
                best_photo = photo
        # print(best, len(photos), score_tags(solution[-1][1], photos[best_index][1]), len(solution[-1][1] & photos[best_index][1]), len(solution[-1][1] - photos[best_index][1]), len(photos[best_index][1] - solution[-1][1]))
        if not len(solution) % 2000:
            photos = deque(x for x in photos if photo_to_i[id(x)] is not None)
        if best_photo is None:
            best_photo = next(x for x in photos if photo_to_i[id(x)] is not None)
        solution.append(best_photo)
        photo_to_i[id(best_photo)] = None
        if not len(solution) % 500:
            print('{} - score {}'.format(len(solution), score_all(solution)))
    format_submission_2(input_photos, solution, 'greedy.txt')

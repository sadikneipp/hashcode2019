from collections import deque

from hashcode.utils import *


def delete_nth(d, n):
    # TODO optimize
    d.rotate(-n)
    d.popleft()
    d.rotate(n)


def solve(input_photos):
    #assert all(x[0] == 'H' for x in input_photos)
    photo_to_i = {id(x): i for i, x in enumerate(input_photos)}
    print(photo_to_i)
    tags = {}
    for photo in input_photos:
        for tag in photo[2]:
            tags.setdefault(tag, [])
            print("tag: ", tag)
            tags[tag].append(photo)
    photos = deque(x for x in input_photos)
    solution = [photos.popleft()] 

    while len(photos) != len(solution):
        possible_pairs = set()
        for tag in solution[-1]:
            print(solution[-1])
            possible_pairs = possible_pairs | set(tags[tag])
        best = 0
        for photo in possible_pairs:
            if photo_to_i[photo] is None:
                continue
            score = score_tags(solution[-1], photo)
            if score > best:
                best = score
                best_index = photo_to_i[photo]
        # print(best, len(photos), score_tags(solution[-1][1], photos[best_index][1]), len(solution[-1][1] & photos[best_index][1]), len(solution[-1][1] - photos[best_index][1]), len(photos[best_index][1] - solution[-1][1]))
        solution.append(photo)
        photo_to_i[photo] = None
        if not len(photos) % 500:
            print('Left: {} - score {}'.format(len(photos), score_all(solution)))
    format_submission(input_photos, solution, 'greedyC.txt')

from collections import deque

from hashcode.utils import *


def solve(input_photos):
    assert all(x[0] == 'V' for x in input_photos)
    used_photos = set()
    tags = {}
    for photo in input_photos:
        for tag in photo[2]:
            tags.setdefault(tag, [])
            tags[tag].append(photo)
    total = len(input_photos)
    photos = deque(x for x in input_photos)
    solution = [photos.popleft()]
    used_photos.add(id(solution[0]))

    print('Running...')
    print('Running...')
    print('Running...')
    while total // 2 != len(solution):
        possible_pairs = []
        for tag in solution[-1][-1]:
            possible_pairs = possible_pairs + tags[tag]
        best = 0
        best_photo = None
        for photo in possible_pairs[:5000]:
            if id(photo) in used_photos:
                continue
            score = score_tags(solution[-1][-1], photo[-1])
            if score > best:
                best = score
                best_photo = photo
        # print(best, len(photos), score_tags(solution[-1][1], photos[best_index][1]), len(solution[-1][1] & photos[best_index][1]), len(solution[-1][1] - photos[best_index][1]), len(photos[best_index][1] - solution[-1][1]))
        if not len(solution) % 2000:
            photos = deque(x for x in photos if id(x) not in used_photos)
        if best_photo is None:
            best_photo = next(x for x in photos if id(x) not in used_photos)
        solution.append(best_photo)
        used_photos.add(id(best_photo))
        if not len(solution) % 50:
            print('{} - score {}'.format(len(solution), score_all(solution)))
            
    second_solution = []
    photos = deque(x for x in photos if id(x) not in used_photos)
    while total // 2 != len(second_solution):
        best = -1
        best_photo = None
        possible_pairs = [x for x in photos if id(x) not in used_photos][:1000]
        for photo in possible_pairs:
            score = score_tags(solution[len(second_solution)][-1] | possible_pairs[-1][-1], photo[-1])
            if score > best:
                best = score
                best_photo = photo
        # print(best, len(photos), score_tags(solution[-1][1], photos[best_index][1]), len(solution[-1][1] & photos[best_index][1]), len(solution[-1][1] - photos[best_index][1]), len(photos[best_index][1] - solution[-1][1]))
        if not len(second_solution) % 2000:
            photos = deque(x for x in photos if id(x) not in used_photos)
        second_solution.append(best_photo)
        used_photos.add(id(best_photo))
        if not len(second_solution) % 50:
            print('{} - score {}'.format(len(solution), score_all_2(solution, second_solution)))
    format_submission_3(input_photos, solution, second_solution, 'greedy.txt')

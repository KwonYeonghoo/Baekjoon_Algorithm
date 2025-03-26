def solution(sizes):
    answer = 0
    curr_w, curr_h = 0, 0
    for width, height in sizes:
        if height > width:
            width, height = height, width
        curr_w, curr_h = max(curr_w, width), max(curr_h, height)
    answer = curr_w * curr_h
    return answer
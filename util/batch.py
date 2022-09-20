import math

def insert_batch(func, data_list, datetime):
    max = len(data_list)
    gap = 500

    if (max % gap) == 0.0:
        step = math.floor(max / gap)
    else:
        step = math.floor(max / gap) + 1
    
    start = 0

    for n in range(step):
        if n == (step - 1):
            end = max
        else:
            end = start + gap
        
        for i in range(start, end):
            func(data_list[i], datetime)

        start = end


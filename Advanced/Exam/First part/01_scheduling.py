def clock_cycles_to_complete(jobs:list, index):

    jobs_with_index = [(job, idx) for idx, job in enumerate(jobs)]
    sorted_jobs = sorted(jobs_with_index, key=lambda x: (x[0], x[1]))
    total_cycles = 0
    for job, idx in sorted_jobs:
        total_cycles += job
        if idx == index:
            break

    return total_cycles


jobs = [int(x) for x in input().split(", ")]
index = int(input())

result = clock_cycles_to_complete(jobs, index)
print(result)

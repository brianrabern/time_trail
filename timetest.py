import timeit

STUFF=[]
my_list= [('a',1),('b',2),('c',3),('d',4),('e',5),('f',6),('g',7),('h',8),('i',9)]

for i in range(1, 100):
	STUFF.append(my_list)

# time: 4.1176545527996495 seconds for 100000 iterations
def list_map_dictify():
     return list(map(dict, STUFF))

# time: 4.248024381231517 seconds for 100000 iterations
def comprehension_dictify():
     return [dict(x) for x in STUFF]

#time: 4.304789905413054 for 100000 iterations
def forloop_dictify():
    result = []
    for x in STUFF:
        result.append(dict(x))
    return result

num_iterations = 100000
num_trials = 5

list_map_times = []
comprehension_times = []
forloop_times = []


for _ in range(num_trials):
    list_map_times.append(timeit.timeit('list_map_dictify()', globals=globals(), number=num_iterations))
    comprehension_times.append(timeit.timeit('comprehension_dictify()', globals=globals(), number=num_iterations))
    forloop_times.append(timeit.timeit('forloop_dictify()', globals=globals(), number=num_iterations))


list_map_avg_time = sum(list_map_times) / num_trials
comprehension_avg_time = sum(comprehension_times) / num_trials
forloop_avg_time = sum(forloop_times) / num_trials


print(f'Number of iterations: {num_iterations}')
print(f'Number of trials: {num_trials}')
print(f'List map dictify (avg): {list_map_avg_time} seconds')
print(f'Comprehension dictify (avg): {comprehension_avg_time} seconds')
print(f'For loop dictify (avg): {forloop_avg_time} seconds')

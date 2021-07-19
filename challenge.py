from proyect import DATA
all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
all_Platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
all_Platzi_workers = list(map(lambda worker: worker['name'], all_Platzi_workers))
adults = [worker['name'] for worker in DATA if worker['age'] > 18]
old_people = [worker | {'old': worker['age'] > 70} for worker in DATA]
old_people = [worker['name'] for worker in old_people if worker['old'] == True]


# adults = [worker['name'] for worker in DATA if worker['age'] > 18]
# # older = [worker | {'old': worker['age'] > 70} for worker in DATA]
# print(adults)
print(all_python_devs)
print(all_Platzi_workers)
print(adults)
print(old_people)
#for worker in older:
    #print(older)
    
# oll_people = [worker | {"oll": worker['age'] > 70} for worker in DATA]

# for worker in oll_people:
#     print(worker)
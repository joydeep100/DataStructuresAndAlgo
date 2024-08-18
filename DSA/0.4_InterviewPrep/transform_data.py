from collections import defaultdict

data = {
    "list1": ['joy', 'deep'],
    "list2": ['emma', 'watson', 'joy']
}

res = defaultdict(list)

for list_name, items in data.items():
    for index, item in enumerate(items):
        '''
        if item not in res:        # able to skip this since we are using defaultdict
        res[item] = []
        '''
        res[item].append({'list': list_name, 'position': index})

print(res)
print(res['joy'])

''' res
{
    'joy': [{'list': 'list1', 'position': 0}, {'list': 'list2', 'position': 2}],
    'deep': [{'list': 'list1', 'position': 1}],
    'emma': [{'list': 'list2', 'position': 0}],
    'watson': [{'list': 'list2', 'position': 1}]
}

This way if we need to apply a search method, then it would be of much better time complexity
'''
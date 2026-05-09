data = {
    "list1": ['joy', 'deep'],
    "list2": ['emma', 'watson', 'joy']}

res = {}

for list_name, items in data.items():
    for index, item in enumerate(items):
        if item not in res:
            res[item] = []
        res[item].append({'list': list_name, 'position': index})

print(res)

''' res
Output:
{
    'joy': [{'list': 'list1', 'position': 0}, {'list': 'list2', 'position': 2}],
    'deep': [{'list': 'list1', 'position': 1}],
    'emma': [{'list': 'list2', 'position': 0}],
    'watson': [{'list': 'list2', 'position': 1}]
}
'''
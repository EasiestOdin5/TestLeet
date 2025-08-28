import json

fh = open("a.json")
data = json.load(fh)


def flatten_json(data, parent_key='', sep='.'):
    items = {}
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


output = flatten_json(data)
print(output)
print("--------------------------")




from collections import deque 

def bfs_flatten_json(data):

    queue = deque()
    queue.append((data, ''))
    result = {}

    while queue:

        current, current_key = queue.popleft()

        print("current:", current)
        print("current_key:", current_key)

        if isinstance(current, dict):
            for key, value in current.items():
                new_key = f"{current_key}.{key}" if current_key else key
                queue.append((value, new_key))

        elif isinstance(current, list):
            for index, value in enumerate(current):
                new_key = f"{current_key}.{index}" if current_key else str(index)
                queue.append((value, new_key))
        else:
            result[current_key] = current

    return result



def dfs_flatten_json(data):

    stack = []
    stack.append((data, ''))
    result = {}

    while stack:

        current, current_key = stack.pop()

        print("current:", current)
        print("current_key:", current_key)

        if isinstance(current, dict):
            for key, value in current.items():
                new_key = f"{current_key}.{key}" if current_key else key
                stack.append((value, new_key))

        elif isinstance(current, list):
            for index, value in enumerate(current):
                new_key = f"{current_key}.{index}" if current_key else str(index)
                stack.append((value, new_key))
        else:
            result[current_key] = current

    return result






output = bfs_flatten_json(data)
print(output)

print("-----------------------------------------")

output = dfs_flatten_json(data)
print(output)
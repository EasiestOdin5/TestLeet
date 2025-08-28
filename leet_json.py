import json

fh = open("a.json")
data = json.load(fh)



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



def dfsi_flatten_json(data):

    stack = []
    stack.append((data, ''))
    result = {}

    while stack:

        current, current_key = stack.pop()

        print("current:", current)
        print("current_key:", current_key)

        if isinstance(current, dict):
            #for key, value in current.items():
            for key, value in reversed(list(current.items())):
                new_key = f"{current_key}.{key}" if current_key else key
                stack.append((value, new_key))

        elif isinstance(current, list):
            for index, value in enumerate(current):
                new_key = f"{current_key}.{index}" if current_key else str(index)
                stack.append((value, new_key))
        else:
            result[current_key] = current

    return result


def dfs_flatten_json(data, parent_key=''):
    items = {}

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            items.update(dfs_flatten_json(value, new_key))
    elif isinstance(data, list):
        for index, value in enumerate(data):
            new_key = f"{parent_key}.{index}" if parent_key else index
            items.update(dfs_flatten_json(value, new_key))
    else:
        items[parent_key] = data
    return items




print("\n----- bfs -----")
output = bfs_flatten_json(data)
print(output)


print("\n----- dfs iter -----")
output = dfsi_flatten_json(data)
print(output)


print("\n----- dfs -----")
output = dfs_flatten_json(data)
print(output)


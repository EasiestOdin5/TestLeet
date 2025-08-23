"""
# 7776
# 1296
# 216
# 36
# 6


def generate_passwords(max_length):
    # Manually define the list of lowercase letters a-z
    #chars = [
    #    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    #    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    #    'u', 'v', 'w', 'x', 'y', 'z'
    #]

    chars =  [ 'a', 'b', 'c', 'd', 'e', 'f' ]

    
    passwords = []

    def backtrack(current):
        if 0 < len(current) <= max_length:
            passwords.append(''.join(current))
        if len(current) == max_length:
            return
        for i in range(len(chars)):
            current.append(chars[i])
            backtrack(current)
            current.pop()

    backtrack([])
    return passwords



result = generate_passwords(5)
print(result)
print(len(result))

"""




"""

def backtrack(current, max_length, passwords, chars):
    print("current:", current)
    if 0 < len(current) <= max_length:
        passwords.append(''.join(current))
    if len(current) == max_length:
        return
    for i in range(len(chars)):
        current.append(chars[i])
        backtrack(current, max_length, passwords, chars)
        current.pop()
    

def generate_passwords(max_length):
    chars =  [ 'a', 'b', 'c', 'd', 'e', 'f' ]
    passwords = []

    backtrack([], max_length, passwords, chars)
    return passwords



output = generate_passwords(4)
print(output)
print(len(output))

# 1296
# 216
# 36
# 6

"""



"""
def backtrack(current, sum_target, sum_found, num_list, start):
    print("current:", current)
    if sum(current) == sum_target:
        print("[+] Found:", current)
        sum_found.append(current[:])
        print("sum_found:", sum_found)
        return
    if sum(current) > sum_target:
        return

    for i in range(start, len(num_list)):
        current.append(num_list[i])
        backtrack(current, sum_target, sum_found, num_list, i)
        current.pop()


def find_sum(sum_target, num_list):
    sum_found = []
    backtrack([], sum_target, sum_found, num_list, 0)
    return sum_found




input1 = [2, 3, 6, 7]
target1 = 7

output = find_sum(target1, input1)

print(output)
"""



"""
from collections import deque

def bfs_password_generator(charset, max_len):
    queue = deque([""])
    #queue = [""]
    
    result = []

    while queue:
        current = queue.popleft()
        print(current)

        if 0 < len(current) <= max_len:
            result.append(current)

        if len(current) < max_len:
            for ch in charset:
                queue.append(current + ch)
    return result


charset = "abcdef"
max_len = 4
passwords = bfs_password_generator(charset, max_len)
print(passwords)
print(len(passwords))
"""

"""
data = {
    "name": "Alice",
    "info": {
        "age": 30,
        "skills": ["Python", "ML"],
        "education": {
            "degree": "MS",
            "year": 2020
        }
    },
    "projects": [
        {"title": "A", "status": "done"},
        {"title": "B", "status": "ongoing"}
    ]
}
"""


data = {
    "a": {
        "b": {
            "c": 1
        },
        "d": 2
    },
    "e": 3
}





from collections import deque


def bfs_json(data, path=""):
    queue = deque([(data, path)])
    result = []

    while queue:
        current, current_path = queue.popleft()
        if isinstance(current, dict):
            for key, value in current.items():
                new_path = f"{current_path}.{key}" if current_path else key
                queue.append((value, new_path))

        elif isinstance(current, list):
            for index, item in enumerate(current):
                new_path = f"{current_path}[{index}]"
                queue.append((item, new_path))

        else:
            print(f"{current_path} = {current}")

print("----- bfs -----")
bfs_json(data, path="")




def dfs_json(data, path=""):

    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            dfs_json(value, new_path)  # recursive call

    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{path}[{index}]"
            dfs_json(item, new_path)  # recursive call

    else:
        # Base case: value is primitive (int, str, etc.)
        print(f"{path} = {data}")

print("----- dfs -----")
dfs_json(data, path="")






def dfs_subsets(nums):
    result = []
    dfs_backtrack([], result, nums, 0)
    return result


def dfs_backtrack(current, result, nums, start):    
    #if start > len(nums):
    #    return
    
    result.append(current[:])

    for i in range(start, len(nums)):
        current.append(nums[i])
        dfs_backtrack(current, result, nums, i+1)
        current.pop()
    

print("----- dfs subset -----")

nums = [1,2,3]
output = dfs_subsets(nums)
print(output)



def bfs_subsets(nums):
    result = []
    queue = deque()
    queue.append(([], 0))

    while queue:
        current, index = queue.popleft()
        result.append(current[:])

        for i in range(index, len(nums)):
            new_subset = current + [nums[i]]
            queue.append((new_subset, i+1))

    return result


nums = [11,22,33]
output = bfs_subsets(nums)
print(output)




print("----------------------------------------------------------------------------------------------------")

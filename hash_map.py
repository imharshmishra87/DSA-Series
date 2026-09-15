def generate_hash_map(data: list) -> dict:
    dict = {}
    list = data
    for i in range(len(list)):
        if list[i] in dict:
            dict[list[i]] += 1
        else:
            dict[list[i]] = 1
    return dict


# print(generate_hash_map(data=[0]))


def generate_hash_map(data: list) -> dict:
    list = data
    hash_map = {}
    for i in range(len(list)):
        hash_map[list[i]] = hash_map.get(list[i], 0) + 1
    return hash_map


print(
    generate_hash_map(
        data=[0, 0, 0, 0, 0, 4, 5, 4, 8, 7, 8, 9, 4, 5, 2, 2, 2, 2, 1, 4, 8]
    )
)

"""Time complexity is o(n) and space complexity is o(n)"""

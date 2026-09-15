def hashing_problem(listA: list, listB: list) -> int:
    a, b = listA, listB
    hash_map_a = {}
    final_hash = {}
    for i in range(len(a)):
        hash_map_a[a[i]] = hash_map_a.get(a[i], 0) + 1
    for j in range(len(b)):
        final_hash[b[j]] = hash_map_a.get(b[j], 0)
    return final_hash


"""Time complexity is O(m+n) and space complexity is o(m+n)"""
print(
    hashing_problem(
        listA=[5, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 5, 5, 7, 5, 10],
        listB=[10, 111, 1, 95, 67, 2],
    )
)

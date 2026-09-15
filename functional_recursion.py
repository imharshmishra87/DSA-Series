"""SUM 1 to N, Time complexity is O(N) and space complexity is O(N) where N is stack space"""


def generate_sum(N):
    if N == 1:
        return 1
    return N + generate_sum(N - 1)


print(generate_sum(10))

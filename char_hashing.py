def char_hashing(val: str, input: list) -> dict:
    str_map = {}
    final_hash = {}
    for i in range(len(val)):
        str_map[val[i]] = str_map.get(val[i], 0) + 1
    for j in range(len(input)):
        final_hash[input[j]] = str_map.get(input[j], 0)

    return final_hash


print(char_hashing(val="Harsh", input=["H", "b", "c", "a"]))


def char_hashing_list(val: str, input: list) -> list:
    data = [0] * 26
    final_list = []

    for char in val:
        asci = ord(char)
        print(asci)
        index = abs(asci - 97)
        data[index] += 1

    for j in input:
        asci_code = ord(j)
        index = abs(asci_code - 97)
        final_list.append(data[index])
    return final_list


print(char_hashing_list(val="harsh", input=["H", "b", "c", "a"]))

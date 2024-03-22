# from collections import Counter

# def count_identical_pairs(strings):
#     identical_pairs = 0
#     for i, string1 in enumerate(strings):
#         for j, string2 in enumerate(strings):
#             if i < j:  # To avoid counting pairs twice (e.g., (A, B) and (B, A))
#                 if Counter(string1).keys() == Counter(string2).keys():
#                     identical_pairs += 1
#     return identical_pairs

# # Input list
input_list = ['good', 'god', 'yarn', 'abc', 'caab']
# identical_pairs_count = count_identical_pairs(input_list)
# print("Number of identical pairs:", identical_pairs_count)

def check_identical(word1,word2) -> str:
    flag = 1
    for i in word1:
        if i not in word2:
            flag = 0
    return flag

identical_pairs = 0
for i in range(len(input_list)):
    for j in range(len(input_list)):
        if i < j and check_identical(input_list[i],input_list[j]):
            identical_pairs += 1

print(identical_pairs)
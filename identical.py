# from collections import Counter

# def count_identical_pairs(strings):
#     identical_pairs = 0
#     for i, string1 in enumerate(strings):
#         for j, string2 in enumerate(strings):
#             if i < j:  # To avoid counting pairs twice (e.g., (A, B) and (B, A))
#                 if Counter(string1).keys() == Counter(string2).keys():
#                     identical_pairs += 1
#     return identical_pairs

# # Input list1
input_list1 = ['good', 'god', 'yarn', 'abc', 'caab']
# identical_pairs_count = count_identical_pairs(input_list1)
# print("Number of identical pairs:", identical_pairs_count)

def check_identical(word1,word2) -> str:
    flag = 1
    for i in word1:
        if i not in word2:
            flag = 0
    return flag

identical_pairs = 0
for i in range(len(input_list1)):
    for j in range(len(input_list1)):
        if i < j and check_identical(input_list1[i],input_list1[j]):
            identical_pairs += 1

print(identical_pairs)
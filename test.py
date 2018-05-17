import itertools
import operator
import time
from itertools import combinations

# # 예시 DATA 읽어오기(50만건)
# text_file = open("/home/hong/다운로드/버드뷰_500000x10.txt", "r")
# # lines = text_file.read().split('\n')
# # print(lines)
# # print(len(lines))
# array_total2 = []
# for number, line in enumerate(text_file.readlines()):
#     y = [value for value in line.split()]
#     p_name = 'p' + str(number)
#     p_hobby = p_name, y
#     # print(p_hobby)
#     array_total2.append(p_hobby)
# text_file.close()

HOBBY_COUNT = 10

# # 1.DATA 입력받기
# def get_user_hobby_data():
#     array_total = []
#     input_people_number = input('사람수를 입력해주세요(예:5):')
#
#     print('취미 데이터 예제: D T C F H M S O Y X')
#     for i in range(int(input_people_number)):
#         person_number = str(i + 1)
#         print(person_number + '번째 사람의 취미를 입력해주세요:')
#         input_array = input()
#         if len(input_array.split(' ')) != HOBBY_COUNT:
#             print('다시 입력해주세')
#             input_array = input()
#         array = 'p' + str(i + 1), input_array.split(' ')
#         array_total.append(array)
#     print(array_total)
#     print(type(array_total))
#     return array_total


array_total = [('1', ['N', 'W', 'S', 'V', 'X', 'P', 'E', 'A', 'G', 'O']),
               ('2', ['N', 'W', 'S', 'V', 'X', 'P', 'E', 'A', 'G', 'Q']),
               ('3', ['N', 'W', 'S', 'V', 'X', 'P', 'E', 'A', 'G', 'L']),
               ('4', ['M', 'W', 'S', 'V', 'X', 'P', 'E', 'A', 'G', 'B']),
               ('5', ['M', 'W', 'S', 'V', 'N', 'Z', 'E', 'A', 'Y', 'B'])]


def calculate_hobby_count_with_comparison(comblist):
    """
    2개의 array를 비교해서 같은 알파벳의 개수를 되돌려준다.
    :param arr1:
    :param arr2:
    :return:
    """
    count = 0
    first_list = list(comblist.values())[0]
    second_list = list(comblist.values())[1]
    for x in first_list:
        for y in second_list:
            if x == y:
                count += 1
    return count


def check_triple_relation(comblist):
    """
    삼각관계 정의
    - (p1,p2),(p1,p3),(p2,p3) 의 관계에서 3명의 일치하는 취미의 개수가 같은 경우
    :param comblist:
    :return:
    """

    comb_key = list(comblist.keys())
    comb_value = list(comblist.values())
    check_triple_set = []
    if comb_value[0] == comb_value[1] == comb_value[2]:
        for i in comb_key:
            for j in str(i):
                check_triple_set.append(j)
        if len(set(check_triple_set)) == 3:
            return True


def main_method():
    # hobby_list = get_user_hobby_data()
    hobby_list = array_total

    # 2.입력받은 사람에 대한 조합리스트 뽑기
    combination_list = list(map(dict, itertools.combinations(dict(hobby_list).items(), 2)))

    # 3.두 명이 가지고 있는 같은 알파벳 개수뽑기
    results = {}
    for combination in combination_list:
        person = int(str(list(combination.keys())[0] + list(combination.keys())[1]))
        results[person] = calculate_hobby_count_with_comparison(combination)

    # 4.특수상황 체크(1. 취미가 10개 일치하는 커플이 여러 커플 발생하는 경우 제외)
    print('특수상황1(취미가 10개 일치하는경우):', [(key, val) for key, val in results.items() if val == HOBBY_COUNT])
    results_without_ten_point = [(key, val) for key, val in results.items() if not val == HOBBY_COUNT]

    print('results_without_ten_point:', results_without_ten_point)

    # 4.특수상황 체크(2. 삼각관계인 경우 체크해서 제외)

    triple_rel_comblist = map(dict, itertools.combinations(dict(results_without_ten_point).items(), 3))
    for comb in list(triple_rel_comblist):
        if check_triple_relation(comb):
            print('특수상황2(삼각관계):', list(comb.keys()))
            for x in results_without_ten_point:
                if x[0] in list(comb.keys()):
                    print(x[0])
                    print(results_without_ten_point.)
                    # results_without_ten_point.remove(x[0])
    #어떻게 제외하지 results_with_out에서 comb.key()에 들어있는 key에 해당하는 것들을 지우고,
    # final_result에서 최대값을 뽑는다.``

    # final_result = [key for key, val in dict(results_without_ten_point).items()
    #                 if val == max(dict(results_without_ten_point).values())]
    # 5.가장 큰 커플 뽑기
    # print('커플매칭:', final_result)


main_method()

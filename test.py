import itertools

# 예시 DATA 읽어오기(50만건)
# def get_data_from_text_file():
#     text_file = open("/home/hong/다운로드/버드뷰_500000x10.txt", "r")
#
#     array_total2 = []
#     for number, line in enumerate(text_file.readlines()):
#         hobby = [value for value in line.split()]
#         p_name = str(number)
#         p_hobby = p_name, hobby
#         array_total2.append(p_hobby)
#     text_file.close()
#     return array_total2
#
# array_total = [('1', ['N', 'W', 'S', 'V', 'X', 'P', 'E', 'A', 'G', 'O']),
#                ('2', ['N', 'W', 'S', 'V', 'X', 'P', 'E', 'A', 'F', 'Q']),
#                ('3', ['N', 'W', 'S', 'V', 'X', 'P', 'F', 'A', 'G', 'L']),
#                ('4', ['M', 'W', 'S', 'V', 'X', 'Z', 'E', 'A', 'Y', 'B']),
#                ('5', ['M', 'W', 'S', 'V', 'X', 'Z', 'E', 'A', 'Y', 'F']),
#                ('6', ['N', 'W', 'S', 'V', 'X', 'P', 'F', 'A', 'G', 'L']),
#                ('7', ['M', 'W', 'S', 'V', 'X', 'Z', 'E', 'A', 'Y', 'F']),
#                ('8', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']),
#                ('9', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']),
#                ('10', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K'])]
HOBBY_COUNT = 10


def calculate_hobby_count_with_comparison(comblist):
    """
    2개의 array(comblist)를 비교해서 같은 알파벳의 개수를 COUNT.
    :param comblist:
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


def check_triangle_relation(comblist):
    """
    삼각관계 정의
    - (p1,p2),(p1,p3),(p2,p3) 의 관계에서 3명의 일치하는 취미의 개수가 같고,
    -   if 3명이름의 key의 set이 3이라면 -> 삼각관계
    -   else 3이 아니라면 -> 삼각관계가 아님.
    - 삼각관계가 여러 개 있는 경우 전부 출력한다.
    :param comblist:
    :return: True/False
    """
    comb_key_list = list(comblist.keys())
    comb_value_list = list(comblist.values())

    check_list_triangle = []

    if comb_value_list[0] == comb_value_list[1] == comb_value_list[2]:
        for i in comb_key_list:
            for j in str(i):
                if j != '-':
                    check_list_triangle.append(j)
        if len(set(check_list_triangle)) == 3:
            return True
        else:
            return False
    return False


def get_combinations(lists, num):
    """
    배열을 전달받아 num개 씩의 묶은 조합의 리스트를 return한다.
    :param lists:
    :param num:
    :return:
    """
    return list(map(dict, itertools.combinations(dict(lists).items(), num)))


def get_data_from_user_input():
    array_total = []
    input_people_number = int(input('사람수를 입력해주세요(예:5):'))

    condition = True
    while condition:
        print('1.데이터를 입력하는경우 / 2. 데이터를 복사하는 경우')
        select = int(input())
        if select == 1:
            for i in range(input_people_number):
                print(str(i + 1) + '번째 사람의 취미를 입력해주세요:')
                input_array = input()
                while len(input_array.split(' ')) != HOBBY_COUNT:
                    print('취미는 10개입니다. 다시 입력해주세요')
                    input_array = input()
                array = str(i + 1), input_array.split(' ')
                array_total.append(array)
            return array_total
        elif select == 2:
            print('데이터를 붙여넣어주세요')
            for i in range(input_people_number):
                lst = input().split(' ')
                array = str(i + 1), lst
                array_total.append(array)
            return array_total
        else:
            condition = True


def main_method():
    # 1.DATA 입력받기
    hobby_list = get_data_from_user_input()

    # 2.입력받은 사람의 취미에 대한 조합리스트 뽑기
    combination_list = get_combinations(hobby_list, 2)

    # 3.두 명이 가지고 있는 같은 알파벳 개수뽑기
    results = {}
    for combination in combination_list:
        person = str(list(combination.keys())[0] + '-' + list(combination.keys())[1])
        results[person] = calculate_hobby_count_with_comparison(combination)

    # 4.특수상황 체크(1. 취미가 10개 일치하는 커플이 여러 커플 발생하는 경우를 출력 후 리스트에서 제외)

    print('특수상황1(취미가 10개 일치하는경우):', [key for key, val in results.items() if val == HOBBY_COUNT])
    results_without_ten_point = [(key, val) for key, val in results.items() if not val == HOBBY_COUNT]

    # 4.특수상황 체크(2. 삼각관계인 경우 체크해서 출력 후 리스트에서 제외)
    combination_list_triangle = get_combinations(results_without_ten_point, 3)

    for comb in combination_list_triangle:
        if check_triangle_relation(comb):
            print('특수상황2(삼각관계):', list(comb.keys()))
            for x in results_without_ten_point[:]:
                if x[0] in list(comb.keys()):
                    results_without_ten_point.remove(x)

    final_result = [(key, str(val) + '개') for key, val in dict(results_without_ten_point).items()
                    if val == max(dict(results_without_ten_point).values())]
    # 5.가장 큰 커플 뽑기
    print('커플매칭:', final_result)


main_method()

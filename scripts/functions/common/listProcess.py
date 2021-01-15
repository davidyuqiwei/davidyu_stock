def continue_values_stat(input_list: list):
    """
    :param input_list: list to stat on the continue number
    :return:
    """
    keys = []
    continue_value = []
    tmp_data = []
    for i, element in enumerate(input_list):
        if i == 0:
            keys.append(element)
            tmp_data.append(element)
        else:
            if element == input_list[i - 1]:
                tmp_data.append(element)
            elif element != input_list[i - 1]:
                continue_value.append(len(tmp_data))
                keys.append(element)
                tmp_data = [element]
        if i == len(input_list) - 1:
            continue_value.append(len(tmp_data))
    return_data = {'keys': keys, 'continue_num': continue_value}
    return return_data
if __name__ == '__main__':
    a1 = [1, -1, -1, -1, 1, 1, 3, 3, 4, 4, 5]
    a2 = continue_values_stat(a1)
    print(a2.get("keys"))
    print(a2.get("continue_num"))  

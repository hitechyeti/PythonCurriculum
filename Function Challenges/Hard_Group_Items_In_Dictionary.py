def group_items(lst):
    groups = {}
    for index, item in enumerate(lst):
        if item not in groups:
            groups[item] = []
        groups[item].append(index)
    return groups


def group_items(lst):
    dict_idx = {}
    for key in lst:
        if key not in dict_idx.keys():
            list_idx = []
            idx = 0
            while idx<len(lst):
                if key == lst[idx]:
                    list_idx.append(idx)
                idx += 1
            dict_idx[key] = list_idx
    return dict_idx

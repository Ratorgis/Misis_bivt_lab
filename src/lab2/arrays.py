def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError('nums list is empty')
    else:
        return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if type(i) is not list and type(i) is not tuple:
            raise TypeError('строкоа не строка строк матрицы')
        for j in i:
            res.append(j)
    return res


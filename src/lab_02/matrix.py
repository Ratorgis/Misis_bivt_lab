def transpose(mat: list[list[float | int]]) -> list[list]:
    if not (all(len(mat[i]) == len(mat[0]) for i in range(len(mat)))):
        raise ValueError("Рваная матрица")
    elif len(mat) == 0:
        return []
    else:
        row, colum = len(mat), len(mat[0])
        res = [[0] * row for i in range(colum)]
        for i in range(row):
            for j in range(colum):
                res[j][i] = mat[i][j]
        return res


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not (all(len(mat[i]) == len(mat[0]) for i in range(len(mat)))):
        raise ValueError("Рваная матрица")
    else:
        row = len(mat)
        res = []
        for i in range(row):
            res.append(sum(mat[i]))
        return res


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not (all(len(mat[i]) == len(mat[0]) for i in range(len(mat)))):
        raise ValueError("Рваная матрица")
    else:
        colum = len(mat)
        row = len(mat[0])
        res = []
        for i in range(row):
            res.append(sum(mat[j][i] for j in range(colum)))
        return res

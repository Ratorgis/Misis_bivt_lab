def student_registration(fio: str, group: str, gpa: float) -> str:
    if type(fio) is not str:
        raise TypeError("Fio must to be str")
    elif len(fio.split()) == 1:
        raise ValueError("Too short fio")
    if type(group) is not str:
        raise TypeError("Group must to be str")
    if type(gpa) is not float:
        raise TypeError("GPA must to be float")
    gpa = round(gpa, 2)
    if len(fio.split()) == 2:
        fio = fio.split()
        short_name = f"{fio[0][0].upper() + fio[0][1:]} {fio[1][0].upper()}."
        return f"{short_name}, гр. {group}, GPA {gpa}"
    else:
        fio = fio.split()
        short_name = (
            f"{fio[0][0].upper() + fio[0][1:]} {fio[1][0].upper()}.{fio[2][0].upper()}."
        )
        return f"{short_name}, гр. {group}, GPA {gpa}"

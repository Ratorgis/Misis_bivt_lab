def student_registration(fio: str, group: str, gpa: float) -> tuple[str, str, float]:
    if type(fio) != type(''):
        raise TypeError('Fio must to be str')
    elif len(fio) == 1:
        raise ValueError('Too short fio')
    if type(group) != type(''):
        raise TypeError('Group must to be str')
    if type(gpa) != type(1.0):
        raise TypeError('GPA must to be float')
    return tuple([fio, group, gpa])

def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) != type(tuple()):
        raise TypeError('rec must to be tuple')
    else:
        fio = list(rec[0].split())
        if len(fio) == 3:
            return f'{fio[0][0].upper() + fio[0][1:]} {fio[1][0].upper()}.{fio[2][0].upper()}., гр. {tuple[1]}, GPA {round(rec[2], 2)}'
        else:
            return f'{fio[0][0].upper() + fio[0][1:]} {fio[1][0].upper()}., гр. {tuple[1]}, GPA {round(rec[2], 2)}'


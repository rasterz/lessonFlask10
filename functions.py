import json

with open('candidates.json', encoding="utf-8") as file:
    templates = json.load(file)


def load_candidates() -> str:
    """
    Возвращает данные из файла candidates.json
    :return: str
    """
    return templates


def get_all() -> None:
    """
    Выводит имена кандидатов
    Например: get_all()
    :return: None
    """
    for candidates in range(len(load_candidates())):
        print(templates[candidates]['name'])


def get_by_pk(pk) -> str:
    """
    Выводит имена кандидата по номеру
    Например: print(get_by_pk(7))
    :return: str
    """
    return templates[pk - 1]['name']


def get_position():
    for candidates in range(len(load_candidates())):
        return get_by_pk(1)[candidates]['position']


def get_by_skill(skill_name):
    """
    Выводит имена кандидатов по навыку
    Например: print(get_by_skill('python'))
    :return: str
    """
    base_list = []
    for candidates in range(len(load_candidates())):
        if skill_name in templates[candidates]["skills"]:
            base_list.append(templates[candidates]["name"])
    return ', '.join(base_list)



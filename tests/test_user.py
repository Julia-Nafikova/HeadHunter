from src.user import salary_range
from src.operations_on_vacancies import OperationsOnVacancies


def test_get_vacancies_by_salary_from(vacancies_objects):
    assert salary_range(vacancies_objects, 500000) == []
    assert salary_range(vacancies_objects, 100000) == [
        OperationsOnVacancies("Разработчик", "https://hh", "требования", "обязанности", 100000)]
    assert salary_range(vacancies_objects, 0) == vacancies_objects
    assert salary_range([], 1000000) == []
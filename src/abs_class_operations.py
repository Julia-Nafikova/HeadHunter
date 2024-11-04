from abc import ABC, abstractmethod


class Operations(ABC):
    """Класс для реализации операций над вакансиями"""
    @abstractmethod
    def adding_vacancies(self):
        pass

    @abstractmethod
    def get_inf(self):
        pass

    @abstractmethod
    def remove_inf(self):
        pass
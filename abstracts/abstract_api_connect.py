from abc import ABC, abstractmethod


class API(ABC):
	"""
	Абстрактный класс для шаблонизации запросов по API
	"""

	@abstractmethod
	def get_vacancies_out_of_api(self, vacancy_name):
		"""
		Получает список словарей вакансий из API
		"""
		pass

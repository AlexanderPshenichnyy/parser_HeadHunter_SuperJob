from abc import ABC, abstractmethod


class Saver(ABC):
	"""
	Абстрактный класс для сохранения файлов с информацией по отобранным вакансиям
	"""

	@abstractmethod
	def save_to_json(self, vacancy_data):
		"""
		Сохраняет список вакансий в json файл
		"""
		pass

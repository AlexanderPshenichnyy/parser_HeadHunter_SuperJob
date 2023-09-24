from abstracts.abstract_api_connect import API
from abstracts.abstract_saver import Saver
import os
import requests


class SuperJob(API):
	_base_url = 'https://api.superjob.ru/2.0/vacancies'
	_superj_api = os.getenv('SECRET_SJ')

	def __init__(self, page=0, count_page=1):
		self.page = page
		self.count_page = count_page

	def get_vacancies_out_of_api(self, vacancy_title):
		"""
		Получает название вакансии.
		Возвращает словарь с найденными вакансиями
		"""
		headers = {'X-Api-App-Id': self._superj_api}
		params = {
			"keyword": vacancy_title,
			"page": self.page,
			"count": self.count_page
		}
		response = requests.get(self._base_url, headers=headers, params=params)
		if response.status_code == 200:
			vacancies = response.json()['objects']
			if vacancies:
				return vacancies
		else:
			raise ConnectionError('Ошибка подключения')

	@property
	def base_url(self):
		return self._base_url

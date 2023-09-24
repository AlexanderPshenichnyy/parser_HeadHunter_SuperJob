from abstracts.abstract_saver import Saver
import json


class FormatSelection(Saver):
	def __init__(self, filename='vac.json'):
		self.filename = filename

	def save_to_json(self, vacancy_data):
		with open(self.filename, 'w', encoding='utf-8') as file:
			json.dump(vacancy_data, file, indent=2, ensure_ascii=False)

	def json_load(self):
		with open(self.filename, 'r', encoding='utf-8') as file:
			data = json.load(file)
		return data

	def json_to_instance(self, class_name):
		lst = []
		for i in self.json_load():
			lst.append(class_name(i))
		return lst

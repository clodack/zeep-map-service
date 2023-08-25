import sqlite3
import json
import string

class Objects():
	def get_list_Obj():
		conn = sqlite3.connect("/home/thekoddima/map/db.sqlite3")
		# получаем метаданные для таблицы
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM objects;")
 
		# выводим названия полей таблицы
		fields = cursor.fetchall()
		list = []
		for field in fields:
			list.append(field)
 
		# закрываем соединение с базой данных
		conn.close()
		#return json.dumps(list, sort_keys=True, indent=4)
		return list
	
	def get_Obj(id):
		conn = sqlite3.connect("/home/thekoddima/map/db.sqlite3")
		# получаем метаданные для таблицы
		cursor = conn.cursor()
		cursor.execute(f"SELECT * FROM map_object_info WHERE id = {id};")
 
		# выводим названия полей таблицы
		fields = cursor.fetchall()
		list = []
		for field in fields:
			list.append(field)
 
		# закрываем соединение с базой данных
		conn.close()
		#return json.dumps(list, sort_keys=True, indent=4)
		return list
class intro:
		def __init__(self):
			pass
		def personal_information(self,name,cnic):
			print(f'Personal Information:-  Name: "{name}" , CNIC: {cnic} ')
		def hobbies(self,hobby):
			print(f'HOBBIES:-  "{hobby}" ')	
			
Frnd_1=intro()
Frnd_1.personal_information("Asad ur Rehman",41304)
Frnd_1.hobbies("Reading")

Frnd_2=intro()
Frnd_2.personal_information("Aimon Sana",41304)
Frnd_2.hobbies("Overthinking")


class dinner:
	def __init__(self,name):
		print(f"{name} would like to have the following dishes in the dinner: ")
	
	def order_soup(self,name):
		print(f"Soup: {name}")
	def order_salad(self,name):
		print(f"Salad: {name}")
	def order_course(self,name):
		print(f"Course: {name}")
	def order_dessert(self,name):
		print(f"Desserts: {name}")
	def order_juice(self,name):
		print(f"Juices: {name}")

frnd_1=dinner("Asad")
frnd_1.order_soup("Chicken Corn Soup")
frnd_1.order_salad("Russian Salad")
frnd_1.order_course("Chicken Biryani")
frnd_1.order_dessert("Chocolate Mousse")
frnd_1.order_juice("Pina Colada")

frnd_2=dinner("Aimon")
frnd_2.order_soup("Chicken Corn Sou0")
frnd_2.order_salad("Coleslaw")
frnd_2.order_course("Karahi")
frnd_2.order_dessert("Lava Cake")
frnd_2.order_juice("Mango Shake")

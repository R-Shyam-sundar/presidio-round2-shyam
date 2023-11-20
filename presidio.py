'''
	Name: R Shyam Sundar
	Roll: CS20B1029
	College: Indian Institute of Information Techology, Design and Manufacturing, Kancheepuram
	Presidio Round 2
	Topic : Teacher Management Application (Console Based CRUD/Backend Problem)
'''

import os
import json

# Teacher class
class Teacher:
	def __init__(self, full_name, age, dob, num_classes):
		self.full_name = full_name
		self.age = age
		self.dob = dob
		self.num_classes = num_classes

	def to_dict(self):
		return {
			'full_name': self.full_name,
			'age': self.age,
			'dob': self.dob,
			'num_classes': self.num_classes
		}

	@classmethod
	def from_dict(cls, data):
		return cls(data['full_name'], data['age'], data['dob'], data['num_classes'])

# Management class
class TeacherManager:
	def __init__(self, file_name):
		self.file_name = file_name
		self.teachers = self.load_data()

	# load json file
	def load_data(self):
		if os.path.exists(self.file_name):
			with open(self.file_name, 'r') as file:
				data = json.load(file)
			list_of_teacher_objects = []
			for teacher_data in data:
				list_of_teacher_objects.append(Teacher.from_dict(teacher_data))
			return list_of_teacher_objects
		else:
			return []

	# save to json file
	def save_data(self):
		with open(self.file_name, 'w') as file:
			current_data = []
			for teacher in self.teachers:
				current_data.append(teacher.to_dict())
			json.dump(current_data, file, indent=2)

	# show all teachers
	def show_all_teachers(self):
		for teacher in self.teachers:
			self.print_teacher_info(teacher)

	# add a teacher
	def add_teacher(self):
		print('*' * 30)
		print("Please enter the following details of the teacher")
		full_name = input("Full name: ")
		age = input("Age: ")
		dob = input("Date of birth (YYYY-MM-DD): ")
		num_classes = int(input("Number of classes taken: "))
		teacher_object = Teacher(full_name, age, dob, num_classes)
		self.teachers.append(teacher_object)
		self.save_data()
		print("\nAdded sucessfully!\n")
		print('*' * 30)

	# filter by age
	def filter_teacher_by_age(self):
		age_criteria = int(input("Enter age to filter by: "))
		for teacher in self.teachers:
			if int(teacher.age) == int(age_criteria):
				self.print_teacher_info(teacher)
		pass

	# filter by class
	def filter_teacher_by_class(self):
		classes_criteria = int(input("Enter number of classes to filter by: "))
		for teacher in self.teachers:
			if teacher.num_classes == classes_criteria:
				self.print_teacher_info(teacher)
		pass

	# Filter by criteria -> age, class
	def filter_by_criteria(self):
		print("1. Filter by age")
		print("2. Filter by classes taken")
		choice = int(input("Your choice(1,2): "))
		if choice == 1:
			self.filter_teacher_by_age()
		elif choice == 2:
			self.filter_teacher_by_class()
		else:
			print("Invalid choice. Try again.")
		pass

	# search for teacher by name
	def search_teacher(self):
		name = input("Enter the full name of the teacher: ")
		for teacher in self.teachers:
			if teacher.full_name.lower() == name.lower():
				self.print_teacher_info(teacher)
		pass

	# update teacher records
	def update_teacher(self):
		name = input("Enter the Full Name of the teacher: ")
		found_similar = False

		for teacher in self.teachers:
			if teacher.full_name.lower() == name.lower():
				print("[Matched]")
				self.print_teacher_info(teacher)
				choice = input("Do you wish to update the above record(y/n): ")
				if choice == 'y':
					teacher.num_classes = int(input("Enter the updated number of classes:  "))
					self.save_data()
					print("Updated Successfully!")
				elif choice == 'n':
					print("Update cancelled.")
				else:
					print("Please enter a valid choice. Try again.")
				found_similar = True


		if found_similar == False:
			teacher_names = []
			for teacher in self.teachers:
				teacher_names.append(teacher.full_name)
			print("\nGiven Name doesn't match records. Please find the list of names given below and try again.\n")
			print(teacher_names)
		pass

	# delete record
	def delete_teacher(self):
		delete_name = input("Enter the full name of the teacher:  ")
		new_list_of_teachers = []
		for teacher in self.teachers:
			if teacher.full_name.lower() == delete_name.lower():
				self.print_teacher_info(teacher)
				choice = input("[Matched] Do you wish to delete the above record(y/n): ")
				if choice == 'y':
					print("Deleted Successfully")
					continue
				elif choice == 'n':
					print("Record retained")
					new_list_of_teachers.append(teacher)
					continue
				else:
					print("Enter a valid choice.")
			else:
				new_list_of_teachers.append(teacher)
		self.teachers = new_list_of_teachers
		self.save_data()
		pass

	# average classes calculation
	def average_classes(self):
		sum_of_classes = 0
		teacher_count = 0
		for teacher in self.teachers:
			sum_of_classes += teacher.num_classes
			teacher_count += 1
		if teacher_count == 0:
			print("No Teachers found!")
		else:
			avg = sum_of_classes/teacher_count
			print(f"Average number of classes: {avg}")

	# print teacher record
	def print_teacher_info(self, teacher):
		print('*' * 30)
		print(f"Full Name: {teacher.full_name}")
		print(f"Age: {teacher.age}")
		print(f"DoB: {teacher.dob}")
		print(f"Number of classes: {teacher.num_classes}")
		print('*' * 30)


# Main function
def main():
	teacher_manager = TeacherManager("teacher_records.json")

	while True:
		print("\nTeacher Management Application.\n")
		print("1. Show all teachers.")
		print("2. Add a teacher.")
		print("3. Filter teachers based on criteria.")
		print("4. Search for a teacher.")
		print("5. Update teacher's record.")
		print("6. Delete a teacher.")
		print("7. Average number of classes teachers take.")
		print("8. Exit application.")

		choice = input("\nYour choice: ")
		
		if choice == '1':
			teacher_manager.show_all_teachers()
		elif choice == '2':
			teacher_manager.add_teacher()
		elif choice == '3':
			teacher_manager.filter_by_criteria()
		elif choice == '4':
			teacher_manager.search_teacher()
		elif choice == '5':
			teacher_manager.update_teacher()
		elif choice == '6':
			teacher_manager.delete_teacher()
		elif choice == '7':
			teacher_manager.average_classes()
		elif choice == '8':
			break
		else:
			print("Please enter a valid choice.")

if __name__ == "__main__":
	main()
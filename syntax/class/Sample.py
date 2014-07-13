class Employee(object):
	'Common base class for all employees'
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name : ", self.name,  ", Salary: ", self.salary

if __name__ == "__main__":
	emp1 = Employee("one", 100)
	emp2 = Employee("two", 100)
	emp3 = Employee("three", 100)
	emp4 = Employee("four", 100)
	print Employee.empCount

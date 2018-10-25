class woman(object):
	def __init__(self,age):
		print"womaaan"


class man(object):
	def __init__(self,age):
		print"im a man"
		self.age = age

	def printer(self):
		print("SUPERCLASS METHOD")

	def printer(self,string):
		print (string)


class boy(man):
	def __init__(self,age):
		super(boy,self).__init__(age)




objects = [" " for x in range(4)]

for i in range(4):
	if i%2==0:
		objects[i] = boy(5)
	else:
		objects[i]=woman(20)

for obj in objects:
	if isinstance(obj,man):
		
		print"thats right"

objects[0].printer()
objects[0].printer("nihao")




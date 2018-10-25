import abc


class Weapon(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self,ranges,damage,owner):
		self.ranges = ranges
		self.effect = damage
		self.owner = owner 

	@abc.abstractmethod
	def action(posx,posy):
		return

	@abc.abstractmethod
	def enhance(self):
		return

	
class Cell():
	"""
	represents a singular cell
	"""
	def __init__(self,initial_state:bool = False):
		if type(initial_state) != bool:
			raise ValueError(f"Invalid initial_state {initial_state!r}")
		self.initial_state = initial_state
		self.state = initial_state
	def flip(self) -> bool:
		"""
		kills a living cell and unkills a dead cell
		returns new state
		"""
		self.state = not self.state
		return self.state
	def __bool__(self) -> bool:
		return self.state
	def __str__(self) -> str:
		return "X" if self.state else " "
	def __repr__(self):
		return f"<classes.Cell state={self.state}, initial_state={self.initial_state}>"
	def __format__(self, format_spec: str) -> str:
		return format_spec if self.state else " "
	def __eq__(self,other):
		if not isinstance(other,self.__class__):
			return False
		return self.state == other.state
	# __mod__ works identically to __format__
	__mod__ = __format__

class IFuckedUpException(Exception): pass
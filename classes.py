class Cell():
	"""
	represents a singular cell
	"""
	def __init__(self,initial_state:bool = False) -> None:
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
		"""
		convert Cell to 'X' by default
		"""
		return "X" if self.state else " "
	def __repr__(self) -> str:
		"""
		show more information in the repr than the str
		"""
		return f"<classes.Cell state={self.state}, initial_state={self.initial_state}>"
	def __format__(self, format_spec: str) -> str:
		"""
		allow using a character besides X for stringifying
		"""
		return format_spec if self.state else " "
	def __eq__(self,other) -> bool:
		"""
		do not compare initial_state
		"""
		if not isinstance(other,self.__class__):
			return False
		return self.state == other.state
	# __mod__ works identically to __format__
	__mod__ = __format__

class Board():
	def __init__(self,length,width) -> None:
		self.length = length
		self.width = width
		self._array = []

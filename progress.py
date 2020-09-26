from os import get_terminal_size

class Progress(object):
	"""You can make Progress Bars with this class"""
	def __init__(self, text="", max=0):
		"""Makes a new Progress Bar
		DON'T PRINT ANYTHING (including new Progress Bars) BEFORE CALLING end()"""
		if not 0 < max < get_terminal_size()[0]: max = get_terminal_size()[0]
		self.text = text[:max].ljust(max)
		self.value = 0
		self.max = max
		self.refresh()
	def next(self, steps=1):
		"""Next"""
		if self.value < self.max:
			self.value += steps
			self.refresh()
			return True
		else:
			return False
	def refresh(self):
		"""Refresh the Progress Bar
		YOU DON'T NEED TO USE THIS"""
		print(f"\033[7m{self.text[:self.value]}\033[0m{self.text[self.value:]}", end="\r")
	def end(self):
		"""Finish drawing Progress Bar
		USE THIS WHEN THE JOB IS DONE"""
		self.value = self.max
		self.refresh()
		print()

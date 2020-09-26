from os import get_terminal_size

class TitleBar(object):
	"""Easy Create Title Bars"""
	def __init__(self, title="", left="", right="", padding=0, width=0, centered=True, transparent=False):
		"""Create a new Title Bar
		call render() to print it"""
		self.title = str(title)
		self.left = str(left)
		self.right = str(right)
		self.padding = int(padding)
		self.width = width if 0 < width < get_terminal_size()[0] else get_terminal_size()[0]
		self.margin = (get_terminal_size()[0] - self.width) // 2
		self.centered = bool(centered)
		self.transparent = bool(transparent)
	def render(self):
		"""You can use this whenever you want"""
		bar  = "\033[7m" if not self.transparent else ""
		# left
		bar += self.padding * " "
		bar += self.left
		# title
		bar += "\033[1m"
		bar += self.title.center(self.width - self.padding * 2 - len(self.left + self.right))
		bar += "\033[0;7m" if not self.transparent else "\033[0m"
		# right
		bar += self.right
		bar += self.padding * " "
		bar += "\033[0m" if not self.transparent else ""
		if self.centered: print(" " * self.margin + bar)
		else: print(bar)

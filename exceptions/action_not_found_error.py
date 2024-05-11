
class ActionNotFoundError(Exception):
	def __init__(self, action):
		self.action = action
		self.message = f"Action '{action}' not found."
		super().__init__(self.message)

class TimelineNotFoundError(Exception):
	def __init__(self, message):
		self.message = message
		super().__init__(f"Timeline template {self.message} is not found.")
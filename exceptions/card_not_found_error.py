class CardNotFoundError(Exception):

	def __init__(self, card_template_name: str):
		self.card_template_name = card_template_name
		super().__init__(f"Card template {card_template_name} not found.")
from cards.base_card import BaseCard


class ExampleCard(BaseCard):

	def __init__(self):
		super().__init__()
		self.title = "Example Card"
		self.fetch = {
			"cardType": "EXTERNAL",
			"objectTypes": [
				{
					"name": "contacts",
					"propertiesToSend": [
						"email"
					]
				}
			],
			"targetUrl": "/webhook/cards/example",
		}
		self.display = {"properties": []}
		self.actions = {
			"baseUrls": []
		}

from hubspot.crm.extensions.cards import CardCreateRequest, CardPatchRequest


class BaseCard(CardCreateRequest):
	"""
	https://developers.hubspot.jp/docs/api/crm/extensions/custom-cards
	"""

	def __init__(self):
		super().__init__()

	def setFetchTargetUrlHost(self, host: str):
		self.fetch['targetUrl'] = host + self.fetch['targetUrl']

	def create_patch_instance(self) -> CardPatchRequest:
		"""
		Create a patch instance from the current instance.
		:return: CardCreateRequest
		"""

		return CardPatchRequest(
			fetch=self.fetch,
			display=self.display,
			title=self.title,
			actions=self.actions,
			local_vars_configuration=self.local_vars_configuration
		)

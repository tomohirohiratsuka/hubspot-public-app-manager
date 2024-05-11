from pprint import pprint

from hubspot import Client
from hubspot.crm.extensions.cards import ApiException

from cards.example_card import ExampleCard
from exceptions.card_not_found_error import CardNotFoundError


class CardCommand:
	hubspot_client: Client
	card_template_mapping = {
		'exampleCard': ExampleCard
	}

	def __init__(self, config):
		self.config = config
		self.hubspot_client = Client(api_key=config.hubspot_developer_api_key)

	def create(self, card_template_name: str):
		"""
		Create a new card in the app.
		:param card_template_name:
		:return:
		"""
		card_template = self.card_template_mapping.get(card_template_name)

		if not card_template:
			raise CardNotFoundError(card_template_name)

		card_template_instance = card_template()
		card_template_instance.setFetchTargetUrlHost(self.config.hubspot_public_app_webhook_host)
		card_template_instance.actions['baseUrls'].append(self.config.hubspot_public_app_webhook_host)
		try:
			res = self.hubspot_client.crm.extensions.cards.cards_api.create(
				app_id=self.config.hubspot_public_app_id,
				card_create_request=card_template_instance
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling cards_api->create: %s\n" % e)

	def delete(self, card_id: str):
		"""
		Delete a card from the app.
		:param card_id:
		:return:
		"""
		try:
			self.hubspot_client.crm.extensions.cards.cards_api.archive(
				app_id=self.config.hubspot_public_app_id,
				card_id=card_id
			)
			print(f'Card with id {card_id} has been deleted from the app({self.config.hubspot_public_app_id}).')
		except ApiException as e:
			print("Exception when calling cards_api->archive: %s\n" % e)

	def find(self, card_id: int):
		"""
		Find a card in the app.
		:param card_id:
		:return:
		"""
		try:
			res = self.hubspot_client.crm.extensions.cards.cards_api.get_by_id(
				app_id=self.config.hubspot_public_app_id,
				card_id=card_id
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling cards_api->get_by_id: %s\n" % e)

	def patch(self, card_id: int, card_template_name: str):
		"""
		Patch a card in the app.
		:param card_id:
		:param card_template_name:
		:return:
		"""
		card_template = self.card_template_mapping.get(card_template_name)

		if not card_template:
			raise CardNotFoundError(card_template_name)

		card_template_instance = card_template()
		card_template_instance.setFetchTargetUrlHost(self.config.hubspot_public_app_webhook_host)
		card_template_instance.actions['baseUrls'].append(self.config.hubspot_public_app_webhook_host)
		card_template_instance = card_template_instance.create_patch_instance()
		try:
			res = self.hubspot_client.crm.extensions.cards.cards_api.update(
				app_id=self.config.hubspot_public_app_id,
				card_id=card_id,
				card_patch_request=card_template_instance
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling cards_api->patch: %s\n" % e)

	def list(self):
		"""
		List all cards in the app.
		:return:
		"""
		try:
			res = self.hubspot_client.crm.extensions.cards.cards_api.get_all(
				app_id=self.config.hubspot_public_app_id
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling cards_api->list: %s\n" % e)

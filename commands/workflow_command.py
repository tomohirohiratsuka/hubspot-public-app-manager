from pprint import pprint
from typing import Union, Literal, Optional

from hubspot import Client
from hubspot.automation.actions import ApiException, PublicActionDefinitionPatch

from actions.example_send_message_action import ExampleSendMessageAction
from config.settings import Config
from exceptions.action_not_found_error import ActionNotFoundError


class WorkflowCommand:
	hubspot_client: Client
	action_template_mapping = {
		"exampleSendMessage": ExampleSendMessageAction,
	}

	def __init__(self, config: Config):
		self.config = config
		self.hubspot_client = Client(api_key=config.hubspot_developer_api_key)

	def create(self, action_template_name: str):
		"""
		Create a new action definition in the app.
		:param action_template_name:
		:return:
		"""
		action_template = self.action_template_mapping.get(action_template_name)

		if not action_template:
			raise ActionNotFoundError(action_template_name)

		action_template_instance = action_template()
		action_template_instance.setWebhookHostForActionUrl(self.config.hubspot_public_app_webhook_host)
		action_template_instance.setWebhookHostForInputFields(self.config.hubspot_public_app_webhook_host)
		try:
			res = self.hubspot_client.automation.actions.definitions_api.create(
				app_id=self.config.hubspot_public_app_id,
				public_action_definition_egg=action_template_instance
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling definitions_api->create: %s\n" % e)

	def delete(self, definition_id: int):
		"""
		Delete an action definition from the app.
		:param definition_id:
		:return:
		"""
		try:
			self.hubspot_client.automation.actions.definitions_api.archive(
				app_id=self.config.hubspot_public_app_id,
				definition_id=definition_id
			)
			print(
				f"Action definition with id {definition_id} has been deleted from app({self.config.hubspot_public_app_id}).")
		except ApiException as e:
			print("Exception when calling definitions_api->delete: %s\n" % e)

	def list(self, limit: Optional[int] = None, after: Optional[str] = None):
		"""
		List all action definitions in the app.
		:param limit:
		:param after:
		:return:
		"""
		try:
			res = self.hubspot_client.automation.actions.definitions_api.get_page(
				app_id=self.config.hubspot_public_app_id,
				archived=False,
				limit=limit,
				after=after,
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling definitions_api->get_all: %s\n" % e)

	def find(self, definition_id: int):
		"""
		Find an action definition by id.
		:param definition_id:
		:return:
		"""
		try:
			res = self.hubspot_client.automation.actions.definitions_api.get_by_id(
				app_id=self.config.hubspot_public_app_id,
				definition_id=definition_id
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling definitions_api->get_by_id: %s\n" % e)

	def patch(self, definition_id: int, action_template_name: str):
		"""
		Update an action definition in the app.
		:param definition_id:
		:param action_template_name:
		:return:
		"""
		action_template = self.action_template_mapping.get(action_template_name)

		if not action_template:
			raise ActionNotFoundError(action_template_name)

		action_template_instance = action_template()
		action_template_instance.setWebhookHostForActionUrl(self.config.hubspot_public_app_webhook_host)
		action_template_instance.setWebhookHostForInputFields(self.config.hubspot_public_app_webhook_host)
		action_template_instance = action_template_instance.create_patch_instance()
		try:
			res = self.hubspot_client.automation.actions.definitions_api.update(
				app_id=self.config.hubspot_public_app_id,
				definition_id=definition_id,
				public_action_definition_patch=action_template_instance
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling definitions_api->update: %s\n" % e)

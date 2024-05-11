from hubspot.automation.actions import PublicActionDefinitionEgg, PublicActionDefinitionPatch


class BaseAction(PublicActionDefinitionEgg):
	"""
	https://developers.hubspot.jp/docs/api/automation/custom-workflow-actions
	"""
	def __init__(self):
		super().__init__()

	def setWebhookHostForInputFields(self, webhook_host: str):
		"""
		Set the webhook host for the input fields.
		:param webhook_host:
		:return:
		"""
		input_fields = self.input_fields
		for input_field in input_fields:
			has_options_url = "optionsUrl" in input_field["typeDefinition"]
			if has_options_url:
				input_field["typeDefinition"]["optionsUrl"] = webhook_host + input_field["typeDefinition"]["optionsUrl"]

	def setWebhookHostForActionUrl(self, webhook_host: str):
		"""
		Set the webhook host for the action url.
		:param webhook_host:
		:return:
		"""
		self.action_url = webhook_host + self.action_url

	def create_patch_instance(self) -> PublicActionDefinitionPatch:
		"""
		Create a patch instance from the current instance.
		:return: PublicActionDefinitionPatch
		"""

		return PublicActionDefinitionPatch(
			input_fields=self.input_fields,
			output_fields=self.output_fields,
			action_url=self.action_url,
			input_field_dependencies=self.input_field_dependencies,
			published=self.published,
			execution_rules=self.execution_rules,
			object_types=self.object_types,
			object_request_options=self.object_request_options,
			labels=self.labels
		)

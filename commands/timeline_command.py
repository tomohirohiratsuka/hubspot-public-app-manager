from pprint import pprint

from hubspot import Client
from hubspot.crm.timeline import ApiException

from exceptions.timeline_not_found_error import TimelineNotFoundError
from timelines.example_timeline import ExampleTimeline


class TimelineCommand:
	hubspot_client: Client
	timeline_template_mapping = {
		"example": ExampleTimeline,
	}

	def __init__(self, config):
		self.config = config
		self.hubspot_client = Client(api_key=config.hubspot_developer_api_key)

	def create(self, timeline_template_name: str):
		"""
		Create a new timeline definition in the app.
		:param timeline_template_name:
		:return:
		"""
		timeline_template = self.timeline_template_mapping.get(timeline_template_name)

		if not timeline_template:
			raise TimelineNotFoundError(timeline_template_name)

		timeline_template_instance = timeline_template()
		if timeline_template_instance.should_replace_url():
			timeline_template_instance.replace_url(self.config.hubspot_public_app_webhook_host)

		try:
			res = self.hubspot_client.crm.timeline.templates_api.create(
				app_id=self.config.hubspot_public_app_id,
				timeline_event_template_create_request=timeline_template_instance
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling create: %s\n" % e)

	def delete(self, template_id: str):
		"""
		Delete a timeline definition in the app.
		:param template_id:
		:return:
		"""
		try:
			res = self.hubspot_client.crm.timeline.templates_api.archive(
				app_id=self.config.hubspot_public_app_id,
				event_template_id=template_id
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling delete: %s\n" % e)

	def update(self, template_id: str, timeline_template_name: str):
		"""
		Update a timeline definition in the app.
		:param template_id:
		:param timeline_template_name:
		:return:
		"""
		timeline_template = self.timeline_template_mapping.get(timeline_template_name)
		if not timeline_template:
			raise TimelineNotFoundError(timeline_template_name)
		timeline_template_instance = timeline_template()
		if timeline_template_instance.should_replace_url():
			timeline_template_instance.replace_url(self.config.hubspot_public_app_webhook_host)
		update_instance = timeline_template_instance.create_update_instance(template_id)
		try:
			res = self.hubspot_client.crm.timeline.templates_api.update(
				app_id=self.config.hubspot_public_app_id,
				event_template_id=template_id,
				timeline_event_template_update_request=update_instance
			)
			pprint(res)
		except ApiException as e:
			print("Exception when calling update: %s\n" % e)

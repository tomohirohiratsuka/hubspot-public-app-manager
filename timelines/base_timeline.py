from hubspot.crm.timeline import TimelineEventTemplateCreateRequest, TimelineEventTemplateUpdateRequest


class BaseTimeline(TimelineEventTemplateCreateRequest):
	"""
	https://developers.hubspot.jp/docs/api/crm/timeline
	"""

	def __init__(self):
		super().__init__()

	def should_replace_url(self) -> bool:
		"""
		Whether to replace the target URL or not.
		:return: bool
		"""
		return False

	def replace_url(self, host: str):
		"""
		Replace the target URL.
		:param host:
		:return:
		"""
		pass

	def create_update_instance(self, id: str) -> TimelineEventTemplateUpdateRequest:
		"""
		Create an update instance from the current instance.
		:return: TimelineEventTemplateUpdateRequest
		"""
		return TimelineEventTemplateUpdateRequest(
			detail_template=self.detail_template,
			name=self.name,
			tokens=self.tokens,
			id=id,
			header_template=self.header_template,
		)

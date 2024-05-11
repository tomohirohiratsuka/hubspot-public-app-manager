from dotenv import dotenv_values


class Config:
	hubspot_developer_api_key: str
	hubspot_public_app_id: str
	hubspot_public_app_webhook_host: str

	def __init__(self, env=None):
		env_mapping = {
			None: '.env',
			'local': '.env.local',
			'staging': '.env.staging',
			'production': '.env.production'
		}
		env_file = env_mapping.get(env, '.env')
		config = dotenv_values(env_file)
		self.hubspot_developer_api_key = config.get("HUBSPOT_DEVELOPER_API_KEY", "")
		self.hubspot_public_app_id = config.get("HUBSPOT_PUBLIC_APP_ID", "")
		self.hubspot_public_app_webhook_host = config.get("HUBSPOT_PUBLIC_APP_WEBHOOK_HOST", "")

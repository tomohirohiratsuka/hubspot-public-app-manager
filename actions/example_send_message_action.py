from actions.base_action import BaseAction


class ExampleSendMessageAction(BaseAction):

	def __init__(self):
		super().__init__()
		self.input_fields = [
			{
				"typeDefinition": {
					"name": "targetEmail",
					"type": "string",
					"fieldType": "text"
				},
				"supportedValueTypes": [
					"OBJECT_PROPERTY"
				],
				"isRequired": True
			},
			{
				"typeDefinition": {
					"name": "targetMessageTemplateId",
					"type": "enumeration",
					"fieldType": "select",
					"optionsUrl": "/api/webhook/options/templates"
				},
				"supportedValueTypes": [
					"STATIC_VALUE"
				],
				"isRequired": False
			},
			{
				"typeDefinition": {
					"name": "firstPlainMessage",
					"type": "string",
					"fieldType": "textarea"
				},
				"supportedValueTypes": [
					"STATIC_VALUE"
				],
				"isRequired": False
			},
			{
				"typeDefinition": {
					"name": "secondPlainMessage",
					"type": "string",
					"fieldType": "textarea"
				},
				"supportedValueTypes": [
					"STATIC_VALUE"
				],
				"isRequired": False
			},
			{
				"typeDefinition": {
					"name": "thirdPlainMessage",
					"type": "string",
					"fieldType": "textarea"
				},
				"supportedValueTypes": [
					"STATIC_VALUE"
				],
				"isRequired": False
			}
		]
		self.output_fields = [
			{
				"typeDefinition": {
					"name": "to",
					"type": "string",
					"fieldType": "text",
					"description": "The email address of the recipient."
				},
				"supportedValueTypes": [
					"STATIC_VALUE"
				]
			},
			{
				"typeDefinition": {
					"name": "from",
					"type": "string",
					"fieldType": "text",
					"description": "The email address of the sender."
				},
				"supportedValueTypes": [
					"STATIC_VALUE"
				]
			},
			{
				"typeDefinition": {
					"name": "messages",
					"type": "string",
					"fieldType": "text",
					"description": "The messages sent to a user."
				},
				"supportedValueTypes": [
					"STATIC_VALUE"
				]
			}
		]
		self.functions = []
		self.action_url = "/api/webhook/actions/send-message"
		self.published = True
		self.execution_rules = []
		self.object_types = [
			"CONTACT"
		]
		self.labels = {
			"en": {
				"actionName": "Send Message",
				"actionDescription": "This action will send a message to the user.",
				"inputFieldLabels": {
					"targetEmail": "Target Email",
					"targetMessageTemplateId": "Target Message Template",
					"firstPlainMessage": "First plain message",
					"secondPlainMessage": "Second plain message",
					"thirdPlainMessage": "Third plain message"
				},
				"inputFieldDescriptions": {
					"targetEmail": "Set the email address of the recipient.",
					"targetTemplateId": "Select a message template.",
					"firstPlainMessage": "First plain message. Maximum 500 characters.",
					"secondPlainMessage": "Second plain message. Maximum 500 characters.",
					"thirdPlainMessage": "Third plain message. Maximum 500 characters."
				}
			},
			"ja": {
				"actionName": "メッセージ送信",
				"actionDescription": "このアクションはユーザーにメッセージを送信します。",
				"inputFieldLabels": {
					"targetEmail": "送信先メールアドレス",
					"targetMessageTemplateId": "メッセージテンプレート",
					"firstPlainMessage": "1つ目のプレーンメッセージ",
					"secondPlainMessage": "2つ目のプレーンメッセージ",
					"thirdPlainMessage": "3つ目のプレーンメッセージ"
				},
				"inputFieldDescriptions": {
					"targetEmail": "受信者のメールアドレスを設定します。",
					"targetMessageTemplateId": "メッセージテンプレートを選択します。",
					"firstPlainMessage": "1つ目のプレーンメッセージ。最大500文字。",
					"secondPlainMessage": "2つ目のプレーンメッセージ。最大500文字。",
					"thirdPlainMessage": "3つ目のプレーンメッセージ。最大500文字。"
				}
			}
		}
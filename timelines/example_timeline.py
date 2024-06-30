from timelines.base_timeline import BaseTimeline


class ExampleTimeline(BaseTimeline):

  def __init__(self):
    super().__init__()
    self.object_type = 'contacts'
    self.name = '予約ログ'
    self.header_template = '{{appointmentEvent}}'
    self.detail_template = """### {{appointmentEvent}}
[予約詳細を確認]({{appointmentDetailUrl}})
### 予約情報
 - 予約メニュー: {{appointmentMenuName}}
 - 予約日時: {{appointmentStart}} ~ {{appointmentEnd}}

### オプション
{{#each extraData.selectedOptions}}
  - {{label}}
{{/each}}

### フォーム回答
{{#each extraData.formAnswers}}
  - **{{label}}**: {{value}}
{{/each}}
"""
    self.tokens = [
      {
        "name": "appointmentEvent",
        "type": "string",
        "label": "予約イベント",
      },
      {
        "name": "appointmentMenuName",
        "type": "string",
        "label": "予約メニュー",
      },
      {
        "name": "appointmentStart",
        "type": "string",
        "label": "予約開始日時",
      },
      {
        "name": "appointmentEnd",
        "type": "string",
        "label": "予約終了日時",
      },
    ]

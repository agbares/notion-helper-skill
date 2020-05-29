from mycroft import MycroftSkill, intent_file_handler


class NotionHelper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('helper.notion.intent')
    def handle_helper_notion(self, message):
        self.speak_dialog('helper.notion')


def create_skill():
    return NotionHelper()


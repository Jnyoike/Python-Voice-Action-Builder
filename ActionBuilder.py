from Action import Action
from Actions import Say, GetDigits, Play

class ActionBuilder():
	def __init__(self):
		self.xml = "<Response>"
		self.actions = []
	def build(self):
		xml = self.xml
		for action in self.actions:
			xml += action.build()
		xml += "</Response>"
		return xml

	def action(self, action):
		self.actions.append(action)
		return self


def main():
	act = ActionBuilder()
	xml_string = act.action(Say("Hi")).action(GetDigits(Play("url.com"))).build()
	print(str(xml_string))

main()

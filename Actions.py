from Action import Action
class GetDigits(Action):
	def __init__(self, say = None, attributes={}):
		children = []
		if say is not None:
			children.append(say)
		Action.__init__(self, tag= "GetDigits", children = children)

class Play(Action):
	def __init__(self):
		Action.__init__(self, "Play")

class Say(Action):
	def __init__(self, text, voice="woman", playBeep="false"):
		attributes = {'voice': voice, 'playBeep':playBeep}
		Action.__init__(self, tag = "Say", text = text, attributes = attributes)

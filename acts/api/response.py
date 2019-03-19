class GetCategoryActResponse(object):
	def __init__(self, actId,username, timestamp,caption, upvotes, imgb64):
		self.actId = actId
		self.username = username
		self.timestamp = timestamp
		self.caption = caption
		self.upvotes = upvotes
		self.imgb64 = imgb64
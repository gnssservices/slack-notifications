# -*- coding: utf-8 -*-

import json
from urllib.parse import urlencode
import urllib.request as urlrequest

class Slack():

	def __init__(self, url=""):
		self.url = url
		self.opener = urlrequest.build_opener(urlrequest.HTTPHandler())

	def notify(self, **kwargs):
		return self.send(kwargs)

	def send(self, payload):
		data = urlencode({"payload": json.dumps(payload)})
		req = urlrequest.Request(self.url)
		response = self.opener.open(req, data.encode('utf-8')).read()
		return response.decode('utf-8')


# -*- coding:utf-8 -*-

try:
	import setuptools
	from setuptools import setup
except ImportError:
	print("Please install setuptools.")

setup_options = dict(
	name         = "slacknotifications",
	description  = "Slack notifications for incomming webhook",
	author       = "Wayne Guo",
	author_email = "wayne.guo@gnss.services",
	license      = "MIT License",
	url          = "https://github.com/gnssservices/slack-notifications",
	classifiers  = [
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"License :: OSI Approved :: MIT License"
	]
)
setup_options["version"] = "0.0.1"
setup_options.update(dict(
	packages         = ['slacknotifications'],
))

setup(**setup_options)
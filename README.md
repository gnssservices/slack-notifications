# Slack Notifications
Slack notifications for incomming webhook. ![python](https://img.shields.io/badge/python-3.3%2C3.4%2C3.5%2C3.6-brightgreen.svg)



## Installation

From source:
```
git clone https://github.com/gnssservices/slack-notifications.git
cd slack-notifications
python setup.py install
```

## Basic Usage

Get a token of slack webhook on [slack page](https://my.slack.com/services/new/incoming-webhook/).

Instantiate:
```
import slacknotifications
slack = slacknotifications.Slack(url="https://hooks.slack.com/services/T00000000/000000000/000000000000000000")
```

Send a simple message:

```
slack.notify(text="Slack Notifications!")
```

Send a custom message:

```
slack.notify(text="Slack Notifications!", username="Notifications", icon_emoji=":satellite:")
```

Use richly-formatted massages:

```
attachments = []
attachment = {"title": "GNSS Test Status", "pretext": "*Notifications* for test ID: 01", "text": "Test *Pass!*", "mrkdwn_in": ["text", "pretext"]}
attachments.append(attachment)
slack.notify(attachments=attachments)
```

More detail description of message formatting, refer according pages:

- [Message Formatting](https://api.slack.com/docs/formatting)
- [Attachments](https://api.slack.com/docs/attachments)
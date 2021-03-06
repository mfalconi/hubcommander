"""
.. module: hubcommander.bot_components.slack_comm
    :platform: Unix
    :copyright: (c) 2017 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.

.. moduleauthor:: Mike Grima <mgrima@netflix.com>
"""
import json

from hubcommander import bot_components

# A nice color to output
WORKING_COLOR = "#439FE0"


def say(channel, attachments, text=None):
    """
    Sends a message (with attachments) to Slack. Use the send_* methods instead.
    :param channel:
    :param attachments:
    :param raw:
    :return:
    """
    if text is None:
        bot_components.SLACK_CLIENT.api_call("chat.postMessage", channel=channel, text=" ",
                                             attachments=json.dumps(attachments), as_user=True)
    else:
        bot_components.SLACK_CLIENT.api_call("chat.postMessage", channel=channel, text=text,
                                             attachments=json.dumps(attachments), as_user=True)


def send_error(channel, text, markdown=False):
    """
    Sends an "error" message to Slack.
    :param channel:
    :param text:
    :param markdown: If True, then look for markdown in the message.
    :return:
    """
    attachment = {
        "text": text,
        "color": "danger",
    }

    if markdown:
        attachment["mrkdwn_in"] = ["text"]

    say(channel, [attachment])


def send_info(channel, text, markdown=False):
    """
    Sends an "info" message to Slack.
    :param channel:
    :param text:
    :param markdown: If True, then look for markdown in the message.
    :return:
    """
    attachment = {
        "text": text,
        "color": WORKING_COLOR,
    }

    if markdown:
        attachment["mrkdwn_in"] = ["text"]

    say(channel, [attachment])


def send_success(channel, text, markdown=False):
    """
    Sends an "success" message to Slack.
    :param channel:
    :param text:
    :param image: A choice of "awesome", "yougotit".
    :param markdown: If True, then look for markdown in the message.
    :return:
    """
    attachment = {
        "text": text,
        "color": "good",
    }

    if markdown:
        attachment["mrkdwn_in"] = ["text"]

    say(channel, [attachment])


def send_raw(channel, text):
    """
    Sends an "info" message to Slack.
    :param channel:
    :param text:
    :return:
    """

    say(channel, None, text)


def get_user_data(data):
    """
    Gets information about the calling user from the Slack API.
    NOTE: Must be called after get_tokens()

    :param data:
    :return:
    """
    result = bot_components.SLACK_CLIENT.api_call("users.info", user=data["user"])
    if result.get("error"):
        return None, result["error"]

    else:
        return result["user"], None


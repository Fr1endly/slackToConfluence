class Bot:
    channel = None

    # Create a constant that contains the default text for the message
    MESSAGE_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Reading tables"
            ),
        },
    }

    def __init__(self, channel):
        self.channel = channel

    def getMessage(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.MESSAGE_BLOCK
            ]
        }
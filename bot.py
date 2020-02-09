# Standard imports
import logging
import logging.config
import os

# Third Party imports
import discord

# Application imports
import config


LOGGER = logging.getLogger(__name__)
logging.basicConfig()


class Client(discord.Client):
    async def on_ready(self):
        LOGGER.info("Logged on as {}!".format(self.user))

    async def on_message(self, message):
        LOGGER.debug("Message from {0.author}: {0.content}".format(message))
        if message.author == client.user:
            return  # Ignore our own messages

        commands = message.content.split(" ")

        if commands[0] != "!{}".format(config.APP["name"]):
            return  # Not one our commands, skip

        if len(commands) == 1:
            return  # We weren't asked to do anything, skip

        if commands[1] == "help":
            await self.help(message)

    async def help(self, message):
        # TODO: Send this to the user in a private message
        list_of_commands = (
            "List of available commands and their actions:\n"
            + "Version {}\n".format(config.APP["version"])
            + "help - gives this, don't act surprised, what did you expect?\n"
            + "add_twitch_notification (post to channel) (twitch user) "
            + "(message to send)\n"
        )

        if message.content.startswith("!{}".format(config.APP["name"])):
            await message.channel.send(list_of_commands)

    async def logout(self):
        # Whatever is needed to close the feedwithout breaking the whole damn
        # thing
        pass


DEBUG = os.sys.argv[-1] == "--debug"
if DEBUG:
    LOGGER.setLevel(logging.DEBUG)
else:
    LOGGER.setLevel(logging.INFO)

client = Client()
config.load_config()
logging.config.dictConfig(config.LOGGING)

if DEBUG:
    LOGGER.debug("In debug mode")
else:
    try:
        client.run(config.APP["token"])
    except KeyboardInterrupt:
        client.logout()

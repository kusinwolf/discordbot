# Standard imports
import logging

# Third Party imports
import yaml


LOGGER = logging.getLogger(__name__)
APP = {}
DATABASE = {}
LOGGING = {}


def load_config(location="./config.yaml"):
    """
    Loads the config from config.yaml and inserts the configs in the specific
    global config variables

    :returns: Nothing
    :rtype: None
    """
    global APP
    global DATABASE
    global LOGGING

    try:
        with open(location, "r") as _file:
            config = yaml.load(_file)

        LOGGER.debug("Using config: {}".format(config))

        APP = config.pop("app")
        DATABASE = config.pop("database")
        LOGGING = config.pop("logging")

        with open(DATABASE.pop("salt_file"), "r") as _file:
            config["salt"] = _file.read()

    except IOError as error:
        LOGGER.error("Could not find/open file '{}'".format(error))
    except KeyError as error:
        LOGGER.error("Missing key in configs: '{}'".format(error))
    except Exception as error:
        LOGGER.exception("Encountered unknown error: '{}'".format(error))

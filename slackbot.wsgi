#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/slackbot/")
sys.path.insert(0,"/var/www/slackbot/slackbot/")

import logging
logging.basicConfig(stream=sys.stderr)

from slackbot import app as application

# coding=utf-8
from core import JediTool
from core import JediCollection


class EvilURL(JediTool):
    TITLE = "EvilURL"
    DESCRIPTION = "Generate unicode evil domains for IDN Homograph Attack " \
                  "and detect them."
    INSTALL_COMMANDS = ["git clone https://github.com/UndeadSec/EvilURL.git"]
    RUN_COMMANDS = ["cd EvilURL;python3 evilurl.py"]
    PROJECT_URL = "https://github.com/UndeadSec/EvilURL"


class IDNHomographAttackTools(JediCollection):
    TITLE = "IDN Homograph Attack"
    TOOLS = [EvilURL()]

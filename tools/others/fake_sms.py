# coding=utf-8
from core import JediTool
from core import JediCollection


class FakeSms(JediTool):
    TITLE = "Fake SMS"
    DESCRIPTION = " A Simple Script to send SMS anonymously."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/machine1337/fake-sms",
        "cd fake-sms;sudo chmod 755 run.sh"
    ]
    RUN_COMMANDS = ["cd fake-sms;sudo ./run.sh"]
    PROJECT_URL = "https://github.com/machine1337/fake-sms"


class FakeSmsTools(JediCollection):
    TITLE = "Fake SMS Tools"
    TOOLS = [FakeSms()]

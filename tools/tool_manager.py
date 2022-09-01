# coding=utf-8
import os
from time import sleep

from core import JediTool
from core import JediCollection


class UpdateTool(JediTool):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update JediTool", self.update_ht)
        ], installable = False, runnable = False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/jedicode/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/jedicode/;"
                  "mkdir jedicode;"
                  "cd jedicode;"
                  "git clone https://github.com/Z4nzu/jedicode.git;"
                  "cd jedicode;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(JediTool):
    TITLE = "Uninstall JediTool"
    DESCRIPTION = "Uninstall JediTool"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("jedicode started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/jedicode/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/jedicode/;")
        print("\nJediTool Successfully Uninstalled..")
        print("Happy Hacking..!!")
        sleep(1)


class ToolManager(JediCollection):
    TITLE = "Update or Uninstall | JediTool"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]

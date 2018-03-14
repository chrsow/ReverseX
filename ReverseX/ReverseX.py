#! /usr/bin/env python3
import fire
import platform
import subprocess
from utils import chrome, firefox, safari
from utils.constants import *

class ReverseX(object):
    """
    Tool for extract source code of browsers extension/add-on.
    """

    def __init__(self):
        # user's operating system  
        self.os = platform.system()

        if self.os == 'Windows':
            pass
        elif self.os == 'Linux':
            pass
        elif self.os == 'Darwin':
            self.ls_extension = MAC_SAFARI_LS_EXTENSION
            self.extension_format = MAC_SAFARI_EXTENSION_FORMAT
        else:
            print('[-] Your operating system is not supported from now.')
            exit(1)
        
        # TODO add only browser user has
        self.chrome = chrome.Chrome(self.ls_extension, self.extension_format)
        self.firefox = firefox.Firefox(self.ls_extension, self.extension_format)
        self.safari = safari.Safari(self.ls_extension, self.extension_format)


    def __check_browsers():
        """
        Check all browsers user has
        """
        browsers = []
        (out, err) = subprocess.Popen('', shell=True)
        status_code = out.status_code()
        return browsers

    def run(self):
        self.chrome.run()
        self.firefox.run()
        self.safari.run()
        self.brave.run()

def main():
    print("""
    __________                                       ____  ___
    \______   \ _______  __ ___________  ______ ____ \   \/  /
    |       _// __ \  \/ // __ \_  __ \/  ___// __ \ \     / 
    |    |   \  ___/\   /\  ___/|  | \/\___ \\  ___/ /     \ 
    |____|_  /\___  >\_/  \___  >__|  /____  >\___  >___/\  \\
            \/     \/          \/           \/     \/      \_/
    """)
    fire.Fire(ReverseX)

if __name__ == '__main__':
    main()
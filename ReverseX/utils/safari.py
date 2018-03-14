import subprocess
import os

from .browser import Browser
from .constants import *

class Safari(Browser):  
    # def ls(self):
    #     try:
    #         (out, err) = subprocess.Popen(self.ls_extention, stdout=subprocess.PIPE, shell=True).communicate()
    #         extensions = [
    #             i.split(self.extension_format)[0] 
    #             for i in out.decode('utf8').split('\n') 
    #             if i.endswith(self.extension_format) ]
    #         return extensions
    #     except:
    #         print('[-] Something wrong.')
    #         exit(1)   ]
    
    def extract(self, extension_name, data_dir = '{}{}'.format(os.getcwd(), SAFARI_DATA_DIRECTORY)):            
        extension_file_path = '{}{}{}'.format(MAC_SAFARI_EXTENSION_PATH, extension_name, MAC_SAFARI_EXTENSION_FORMAT)

        try: 
            subprocess.Popen('xar -xf {} -C {}'.format(extension_file_path, data_dir), shell=True)
        except:
            print('[-] Something wrong when reversing ' + extension_name)
            exit(1)
        
        print('[+] Success reversing {}, reversed file is on {}'.format(extension_name, data_dir))


            
        


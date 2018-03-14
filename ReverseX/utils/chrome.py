import os
from .browser import Browser

class Chrome(Browser):  

    def extract(self, extension_name, data_dir = os.getcwd() + '/Data/Safari/'):
        print(123)
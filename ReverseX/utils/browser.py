import subprocess
import os

class Browser(object):
    def __init__(self, ls_extention, extension_format):
        self._ls_extention = ls_extention
        self._extension_format = extension_format
    
    # def ls(self, ls_extention, extension_format):
    def __ls(self):
        """
        lists browser's extensions or lists all browsers user has and return the value
        """
        try:
            (out, err) = subprocess.Popen(self._ls_extention, stdout=subprocess.PIPE, shell=True).communicate()
            extensions = [
                i.split(self._extension_format)[0] 
                for i in out.decode('utf8').split('\n') 
                if i.endswith(self._extension_format) ]
            return extensions
        except:
            print('[-] Something wrong.')
            exit(1)   

    def ls(self):
        """
        lists browser's extensions or lists all browsers user has and print the value
        """
        # raise NotImplementedError()        
        extensions = self.__ls()
        print(extensions)


    def reverse(self, extension_name, data_dir = os.getcwd() + '/Data/Safari/'):        
        raise NotImplementedError()
    
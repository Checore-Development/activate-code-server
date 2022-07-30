from . import base

class encrypt(object):
    def __init__(self, *args, **kwargs):
        self.code_format = kwargs.get('code_format')
        self.encrypt_method = kwargs.get('encrypt_method')
        self.encrypt_key = kwargs.get('encrypt_key')
        
    def encrypted_function(self, *args, **kwargs):
        token = args[0]
        encrypt_method = kwargs.get('encrypt_method')
            
        if encrypt_method == "base16":
            return base.base16(token)
        elif encrypt_method == "base32":
            return base.base32(token)
        elif encrypt_method == "base64":
            return base.base64(token)
        elif encrypt_method == "base85":
            return base.base85(token)
        else:
            return
                
    def encode(self, *args, **kwargs):
        token = args[0]
        encrypt_method = kwargs.get('encrypted')
            
        if encrypt_method == 'False':
            return token
            
        encrypted = self.encrypted_function(token, encrypt_method=encrypt_method)
        
        if encrypted is None:
            return
        else:
            return encrypted.encode
                
    def decode(self, *args, **kwargs):
        token = args[0]
        encrypt_method = kwargs.get('encrypted')
            
        if encrypt_method == 'False':
            return token

        encrypted = self.encrypted_function(token, encrypt_method=encrypt_method)
        
        if encrypted is None:
            return
        else:
            return encrypted.decode
import random
import secrets
import numpy as np

class generate_code(object):
    def __init__(self, *args, **kwargs):
        self.code_format = kwargs.get('code_format')
        self.digits = '1234567890'
        self.small_strings = 'abcdefghijklmnopqrstuvwxyz'
        self.big_strings = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @property
    def lists(self):
        return ''.join([self.digits, self.small_strings, self.big_strings])
    
    def generate(self, seed=None):
        random_code = []

        if seed is None:
            for _ in range(self.code_format.count('x')):
                random_code.append(secrets.choice(self.lists))
        else:
            random.seed(seed)
            random_code.extend(random.choices(self.lists, k=self.code_format.count('x')))
            
        return random_code
    
    def token(self, seed=None):
        token = ''
        random_code = self.generate(seed)
        
        if seed is None:
            reload_count = np.random.randint(1, 10000)
            for _ in range(reload_count):
                np.random.shuffle(random_code)
        else:
            np.random.seed(seed)
            reload_count = np.random.randint(1, 10000)
            for _ in range(reload_count):
                np.random.seed(seed)
                np.random.shuffle(random_code)
            
        for code in self.code_format:
            if code == 'x':
                token += random_code[0]
                random_code.pop(0)
            else:
                token += code
                
        return token
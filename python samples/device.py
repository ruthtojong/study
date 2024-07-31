class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add
    def getdesc(self):
        '''return a formatted description of the router'''
        desc = (f'Router Model             :{self.model}\n'
                f'Software Version         :{self.swversion}\n'
                f'Router Management Address:{self.ip_add}')
        return desc
class Switch(Router):
    def getdesc(self):
        '''return a formatted description of the switch'''
        desc = (f'Switch Model             :{self.model}\n'
                f'Software Version         :{self.swversion}\n'
                f'Switch Management Address:{self.ip_add}')
        return desc

class Color(object):

    def __init__(self):
        self.font_color = {
            'black' : '\033[30m',
            'red' : '\033[31m',
            'green' : '\033[32m',
            'yellow' : '\033[33m',
            'blue' : '\033[34m',
            'magneta' : '\033[35m',
            'cyan' : '\033[36m',
            'white' : '\033[37m',
            'default' : '\033[39m'
        }
        self.background = {
            'black' : '\033[40m',
            'red' : '\033[41m',
            'green' : '\033[42m',
            'yellow' : '\033[43m',
            'blue' : '\033[44m',
            'magenta' : '\033[45m',
            'cyan' : '\033[46m',
            'white' : '\033[47m',
            'default' : '\033[49m'
        }

        self.special = {
            #special functions can be started either with 'name' or 'name_on' as both will return the same
            'bold' : '\033[1m',
            'bold_on' : '\033[1m',
            'bold_off' : '\033[22m',
            'italics' : '\033[3m',
            'italics_on' : '\033[3m',
            'italics_off' : '\033[23m',
            'underline' : '\033[4m',
            'underline_on' : '\033[4m',
            'underline_off' : '\033[24m',
            'inverse' : '\033[7m',
            'inverse_off' : '\033[27m',
            'strikethrough' : '\033[9m',
            'strikethrough_on' : '\033[9m',
            'strikethrough_off' : '\033[29m',
            'blink' : '\033[5m',
            'blink_on' : '\033[5m',
            'blink_off' : '\033[25m',
            'reset' : '\033[0m'
        }
    def background_color(self, colorname):
        if self.background[colorname]:
            return self.background[colorname]
        else:
            raise KeyError("%s is not a defined background color"%colorname)
            
        
    def foreground_color(self, colorname):
        if self.foreground[colorname]:
            return self.special[colorname]
        else:
            raise KeyError("%s is not a defined foreground color"%colorname)

        
    def special_action(self, action):
        if self.special[action]:
            return self.special[action]
        else:
            raise KeyError("%s is not a defined action"%action)
        


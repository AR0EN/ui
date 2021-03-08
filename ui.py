import readline

class UI:
    def __init__(self):
        self.__func_handler_map = {}
        self.__func_desc_map = {}

    # _handler: a callable which accept one parameter
    # The parameter is a list-like object (maybe empty)
    def register(self, _fc, _handler, _desc):
        if (not callable(_handler)):
            print('Failed to register function code: {}'.format(_fc))
            print('* Reason: 2nd parameter ({}) is not callable'.format(_handler))
            return

        if (_fc is None):
            print('Failed to register function code: {}'.format(_fc))
            return

        if (type(_fc) is not str):
            print('Failed to register function code: {}'.format(_fc))
            print('* Reason: 1st parameter (function code) must be a string!')
            return

        if (_fc in self.__func_handler_map):
            print('Function code "{}" does exists -> its handler will be overridden!')

        self.__func_desc_map[_fc] = _desc
        self.__func_handler_map[_fc] = _handler

        print('Registered {}->{}: {}!'.format(_fc, _handler, _desc))

    def process(self):
        icmd = input()
        if (icmd is None):
            print('Invalid input!')
            return

        tokens = icmd.split()
        fc = tokens[0]
        if (fc not in self.__func_handler_map):
            print('Unexpected function code: "{}"'.format(fc))
            self.print_help()
            return

        if (1 < len(tokens)):
            args = tokens[1:]
        else:
            args = None

        handler = self.__func_handler_map[fc]
        try:
            handler(args)
        except TypeError:
            print('Handler ({}) of function code "{}" does not accept a list-like object as the only parameter!'.
                    format(handler, fc)
                 )
            print('-> Function code "{}" will be removed from database!'.format(fc))
            self.__func_handler_map.pop(fc)
            self.__func_desc_map.pop(fc)

            self.print_help()

    def print_help(self):
        print('Supported function codes:')
        for fc in self.__func_desc_map:
            print('* {}: {}'.format(fc, self.__func_desc_map[fc]))

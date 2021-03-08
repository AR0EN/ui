from ui import UI

def h0(args):
    if (args):
        print('h0() has been called with the following parameters:')
        for arg in args:
            print('\t{}'.format(arg))
    else:
        print('h0() has been called without parameter!')

def h1():
    print('h1() has been called!')

def h2(args):
    print('Terminating')
    exit()

m_ui = UI()

m_ui.register('h0', h0, 'h0 function')
m_ui.register('h1', h1, 'h1 function')
m_ui.register(0, 'xx', 'this one should be rejected!')
m_ui.register('x', h2, 'terminating function')

while (True):
    m_ui.process()

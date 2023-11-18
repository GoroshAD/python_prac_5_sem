def objcount(cls):
    class classss(cls):
        counter = 0
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            classss.counter += 1
        def __del__(self):
            classss.counter -= 1
            try:
                super().__del__()
            except:
                pass
    return classss

import sys
exec(sys.stdin.read())

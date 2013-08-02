from logging import (Logger, 
                     getLogger, 
                     basicConfig,
                     addLevelName)
from datetime import datetime
import inspect

basicConfig()

# Set level info
TRACE = 15
addLevelName(TRACE, 'TRACE')

# Set default name
NAME = '_RubberBullet'

class Tracer(Logger):
    def __init__(self, name, level=TRACE):
        super(Tracer, self).__init__(name, level)
        self._lastCalled = datetime.now()

    def trace(self, *args, **kwargs):
        # Get the frame which called trace()
        frame = inspect.currentframe().f_back
        info = inspect.getframeinfo(frame)
        if isinstance(self, ColorTracer):
            msg = ' Elapsed: %ss %s:%s'
        else:
            msg = ' Elapsed: %ss %s:%s'
        # Calculate last-called time
        now = datetime.now()
        elapsed = now - self._lastCalled
        self._lastCalled = now
        
        # Output a debug message
        self._log(TRACE, msg, (elapsed.seconds, info.filename, info.lineno), 
                  **kwargs)

def getTracer(name=NAME, color=True):
    Tracer.manager.setLoggerClass(Tracer)
    return ColorTracer.manager.getLogger(name)

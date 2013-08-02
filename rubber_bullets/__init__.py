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
        msg = ' Elapsed: %sms %s:%s'
        # Calculate last-called time
        now = datetime.now()
        elapsed = now - self._lastCalled
        elapsedMilliseconds = elapsed.seconds * 1000 + float(elapsed.microseconds)/1000
        self._lastCalled = now
        
        # Output a debug message
        self._log(TRACE, msg, (elapsedMilliseconds, info.filename, info.lineno), 
                  **kwargs)

def getTracer(name=NAME, color=True):
    Tracer.manager.setLoggerClass(Tracer)
    return Tracer.manager.getLogger(name)

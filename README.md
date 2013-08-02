Rubber Bullets
==============

A port of the simple (but brilliant) [``tracer_bullets``][1] for Ruby. 
_Rubber Bullets_ extends Python's ``logging`` library to calculate the elapsed 
time between successive ``trace()`` calls. Pepper your code with traces,
and figure out where things are slowing down--no fancy profiling required!
 
Usage
-----

```
import rubber_bullets

tracer = rubber_bullets.getTracer()
tracer.trace()
... # Some more code
tracer.trace()
```

Should output:
```
TRACE:_RubberBullet: Elapsed: 3.045ms example.py:4
TRACE:_RubberBullet: Elapsed: 523.365ms example.py:6
```

TODO
----

Better formatting/support for colorizing output



[1]: https://github.com/n8/tracer_bullets

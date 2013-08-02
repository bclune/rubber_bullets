import rubber_bullets
import time

tracer = rubber_bullets.getTracer()

if __name__ == "__main__":
    tracer.trace()
    time.sleep(3)
    tracer.trace()


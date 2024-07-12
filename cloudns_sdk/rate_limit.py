import time
import threading

def rate_limited(max_per_second):
    min_interval = 1.0 / max_per_second
    lock = threading.Lock()
    last_time_called = [0.0]

    def decorator(func):
        def rate_limited_function(*args, **kwargs):
            with lock:
                elapsed = time.perf_counter() - last_time_called[0]
                left_to_wait = min_interval - elapsed
                if left_to_wait > 0:
                    time.sleep(left_to_wait)
                last_time_called[0] = time.perf_counter()
                return func(*args, **kwargs)
        return rate_limited_function
    return decorator
import time
import threading

def rate_limited(max_per_second):
    """
    Decorator function to limit the rate of calls to the decorated function.

    Args:
        max_per_second (int): Maximum number of calls allowed per second.

    Returns:
        callable: Decorator function that applies rate limiting to another function.

    Usage:
        Apply this decorator to functions that need to be rate-limited to a specified maximum calls per second.
        It uses threading.Lock to synchronize access and time.sleep to enforce rate limiting.

    Example:
        @rate_limited(10)  # Limits to 10 calls per second
        def my_function():
            # Function code here
            pass
    """
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
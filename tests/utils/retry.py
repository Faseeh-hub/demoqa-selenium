# tests/utils/retry.py
import time
from functools import wraps

def retry(max_retries=3, delay=1):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*a, **kw):
            for i in range(1, max_retries+1):
                try:
                    return fn(*a, **kw)
                except Exception as e:
                    print(f"[retry] attempt {i} failed: {e}")
                    if i == max_retries:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

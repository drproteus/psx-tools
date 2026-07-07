import os
import json
from functools import wraps

CACHE_DIR = ".cache"


def cache_request(fn, *args, **kwargs):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not os.path.exists(CACHE_DIR):
            os.mkdir(CACHE_DIR)
        cache_name = os.path.join(
            CACHE_DIR, "+".join([fn.__name__, str(args), str(kwargs)]) + ".json"
        )
        try:
            if os.path.exists(cache_name):
                with open(cache_name, "r") as f:
                    return json.load(f)
        except Exception:
            # Couldn't write, possible bad filename.
            pass
        data = fn(*args, **kwargs)
        if data:
            try:
                with open(cache_name, "w") as f:
                    json.dump(data, f)
            except Exception:
                # Couldn't write, possible bad filename.
                pass
        return data

    return wrapped

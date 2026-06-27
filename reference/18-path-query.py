"""Reference — 18 path-query. Check AFTER attempting."""

_MISSING = object()


def _step(node, segment):
    """Descend one segment; raises KeyError/IndexError/ValueError/TypeError on a miss."""
    if isinstance(node, list):
        return node[int(segment)]
    if isinstance(node, dict):
        return node[segment]
    raise KeyError(segment)  # can't descend into a scalar


def get_path(data, path, default=_MISSING):
    current = data
    try:
        for segment in path.split("."):
            current = _step(current, segment)
    except (KeyError, IndexError, ValueError, TypeError):
        if default is _MISSING:
            raise KeyError(path)
        return default
    return current


def set_path(data, path, value):
    segments = path.split(".")
    current = data
    for segment in segments[:-1]:
        if isinstance(current, list):
            current = current[int(segment)]
        elif isinstance(current, dict):
            if segment not in current or not isinstance(current[segment], (dict, list)):
                current[segment] = {}
            current = current[segment]
        else:
            raise KeyError(segment)
    last = segments[-1]
    if isinstance(current, list):
        current[int(last)] = value
    else:
        current[last] = value
    return data

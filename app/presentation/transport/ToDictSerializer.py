def _to_dict(object):
    if isinstance(object, list):
        return [_to_dict(obj) for obj in object]
    else:
        attributes = object.__dict__

        for key in attributes:
            if hasattr(attributes[key], '__dict__'):
                attributes[key] = _to_dict(attributes[key])

        return attributes

from datetime import datetime

from business.entities.Identifier import Identifier


def _to_dict(object):
    if isinstance(object, list):
        return [_to_dict(obj) for obj in object]
    else:
        attributes = object.__dict__

        for key in attributes:
            if isinstance(attributes[key], datetime):
                attributes[key] = attributes[key].isoformat()
            if isinstance(attributes[key], Identifier):
                attributes[key] = repr(attributes[key])
            elif hasattr(attributes[key], '__dict__'):
                attributes[key] = _to_dict(attributes[key])

        return attributes

import json
import sys

from typing import Optional, Iterable, List

from algoliasearch.exceptions import MissingObjectIdException


def get_items(dictionary=None):
    # type: (Optional[dict]) -> Iterable

    if dictionary is None:
        items = []  # type: Iterable
    elif sys.version_info >= (3, 0):
        items = dictionary.items()
    else:
        items = dictionary.iteritems()

    return items


def assert_object_id(objects):
    # type: (List[dict]) -> None

    for obj in objects:
        if 'objectID' not in obj:
            raise MissingObjectIdException(
                'Missing `objectID` in: ' + json.dumps(obj), obj)


def build_raw_response_batch(action, objects):
    # type: (str, list) -> dict

    requests = []
    for obj in objects:
        requests.append({
            'action': action,
            'body': obj
        })

    return {'requests': requests}

import json

from log import logger
import settings


contact_schema = {
    # this is not a real schema, just a helper for the ContactModel.match method
    "type" : "object",
    "properties" : {
        "job_history" : {
            "type" : "array",
            "items": {"type": "string"},
        },
        "company" : {"type" : "string"},
        "email" : {"type" : "string"},
        "city" : {"type" : "string"},
        "name" : {"type" : "string"},
        "country" : {"type" : "string"},
    },
}

class ContactModel:
    """
    Poor man's Elastic Search
    """
    db = json.load(open("src/glowing-journey/aux/database.json")) # Well technically, it CAN be considered a db...

    def _list(self, size):
        return self.db

    def match_any(self, search_string):
        matches = []
        for item in self.db:
            for key, value in item.items():
                if type(item[key]) == str and search_string in item[key]:
                    matches.append(item)
                    break
                elif type(item[key]) == list and any([ search_string in string for string in item[key] ]):
                    matches.append(item)
                    break
        return matches

    def match(self, search_payload=None, size=10):
        if not search_payload:
            return self._list(size)

        _any = search_payload.pop("any", None)
        if _any:
            return self.match_any(_any)

        matches = []
        for item in self.db:
            for key, value in search_payload.items():
                if key not in contact_schema["properties"]:
                    raise KeyError("key `{}` does not exist in contact model".format(key))
                if contact_schema["properties"][key]["type"] == "string":
                    if value not in item[key]:
                        break
                elif contact_schema["properties"][key]["type"] == "array":
                    if not any([ value in string for string in item[key] ]):
                        break
                else:
                    break
            else:
                matches.append(item)
        return matches

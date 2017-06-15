import os


class dotdict(dict):
    """
    dot.notation access to dictionary attributes
    http://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


api = dotdict({
    "host": '0.0.0.0',
    "port": '8000',
})

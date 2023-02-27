import fnmatch
import os


def deepfiles(path):
    """
     Return a list of files in `path` starting with "deep".
     """
    return fnmatch.filter(os.listdir(path), 'deep*')


print(deepfiles('.\\images'))

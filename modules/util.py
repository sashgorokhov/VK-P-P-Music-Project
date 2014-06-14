from PySide import QtCore

__author__ = 'sashgorokhov'
__email__ = 'sashgorokhov@gmail.com'

import threading, re

def showmessage(msg):
    print(str(msg))

def getValidFilename(filename):
    regexp = re.compile(r"[0-9a-zA-ZА-Яа-я\-\(\)\.\' ]")
    return ''.join(i for i in filename if re.match(regexp, i))[:100]

class VkAudio:
    def __init__(self, audioobject):
        self.__object = audioobject
        self.owner_id = None

    def id(self):
        return self.__object['id']

    def getObject(self):
        return self.__object

    def artist(self):
        return self.__object['artist']

    def title(self):
        return self.__object['title']

    def url(self):
        return self.__object['url']

    def duration(self, parsed=False):
        if parsed:
            mins = (self.__object['duration'] // 60)
            secs = self.__object['duration']-60*(self.__object['duration'] // 60)
            return (mins, secs)
        return self.__object['duration']

    def __getattr__(self, item):
        return self.__object[item]

    def __str__(self):
        return '[{0}] {} - {}'.format(':'.join(self.duration(True)), self.artist(), self.title())

#колеса
class Buffer:
    def __init__(self):
        self.__lock = threading.Lock()
        self.__buffer = dict()

    def get(self, key):
        with self.__lock:
            return self.__buffer[key]

    def put(self, key, value):
        with self.__lock:
            self.__buffer[key] = value

    def remove(self, key):
        with self.__lock:
            return self.__buffer.pop(key)

    def __contains__(self, item):
        with self.__lock:
            return item in self.__buffer


class ThreadedWorker(QtCore.QThread):
    def __init__(self, **kwargs):
        super().__init__()
        self._result = None
        self._lock = threading.Lock()
        self._kwargs = kwargs

    def run(self):
        with self._lock:
            self._result = self._workfunc()

    def _workfunc(self):
        raise NotImplementedError

    def get_result(self):
        with self._lock:
            return self._result

if __name__ == '__main__':
    print(getValidFilename("D. Guetta ft. Lil Wayne - my bombs (jetty's remix)"))
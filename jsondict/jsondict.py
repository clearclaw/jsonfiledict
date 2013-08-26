#! /usr/bin/env python

import json, os
from logtool import log_func

class JsonDict (dict):
  @log_func
  def __init__ (self, fname, *args):
    self.__cache = None
    self.__loaded = False
    self.fname = os.path.abspath (fname) if fname else None
    if fname:
      self.file_time = None
    self.load ()
    dict.__init__ (self, *args)
    self.save ()

  @log_func
  def __stale (self):
    return (self.fname
            and (not os.path.isfile (self.fname) or
                 (os.path.isfile (self.fname)
                  and self.file_time != os.path.getmtime (self.fname))))

  @log_func
  def load (self, force = False):
    if self.__stale () or force:
      if os.path.isfile (self.fname):
        with file (self.fname)  as f:
          dict.update (
            self, json.loads (f.read ()))
        self.file_time = os.path.getmtime (self.fname)

  @log_func
  def save (self, force = False):
    if str (self) == self.__cache and not force:
      return
    if self.fname:
      with open (self.fname, "w") as f:
        f.write (json.dumps (self, indent = 2))
      self.file_time = os.path.getmtime (self.fname)
    self.__cache = str (self)

  @log_func
  def __getitem__ (self, key):
    if not self.__loaded:
      self.load ()
    return dict.__getitem__ (self, key)

  @log_func
  def __setitem__ (self, key, val, **kwargs):
    if not self.__loaded:
      self.load ()
    dict.__setitem__ (self, key, val, **kwargs)
    self.save ()

  @log_func
  def __getattribute__ (self, name):
    attr = object.__getattribute__ (self, name)
    if hasattr (attr, '__call__'): # It it callable?
      def wrapper (*args, **kwargs):
        was_loaded = self.__loaded
        if not self.__loaded:
          self.__loaded = True
          self.load ()
        rc = attr (*args, **kwargs)
        if was_loaded != self.__loaded:
          self.save ()
        self.__loaded = was_loaded
        return rc
      return wrapper
    else:
      return attr

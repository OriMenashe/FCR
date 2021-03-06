#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from __future__ import absolute_import
import six
from thrift.util.Recursive import fix_spec
from thrift.Thrift import *
from thrift.protocol.TProtocol import TProtocolException



import pprint
import warnings
from thrift import Thrift
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.protocol import THeaderProtocol
try:
  from thrift.protocol import fastproto
except:
  fastproto = None
all_structs = []
UTF8STRINGS = bool(0) or sys.version_info.major >= 3

__all__ = ['UTF8STRINGS', 'fb_status']

class fb_status:
  """
  Common status reporting mechanism across all services
  """
  DEAD = 0
  STARTING = 1
  ALIVE = 2
  STOPPING = 3
  STOPPED = 4
  WARNING = 5

  _VALUES_TO_NAMES = {
    0: "DEAD",
    1: "STARTING",
    2: "ALIVE",
    3: "STOPPING",
    4: "STOPPED",
    5: "WARNING",
  }

  _NAMES_TO_VALUES = {
    "DEAD": 0,
    "STARTING": 1,
    "ALIVE": 2,
    "STOPPING": 3,
    "STOPPED": 4,
    "WARNING": 5,
  }

fix_spec(all_structs)
del all_structs

#!/usr/bin/python

from barista import Barista
from barista.constants import *
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport

'''
@author: anant bhardwaj
@date: Mar 24, 2014

Sample Python client
'''

try:
  transport = TSocket.TSocket('localhost', 9000)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = Barista.Client(protocol)
  transport.open()

  print client.get_version()

  transport.close()
except Exception, e:
    print 'Something went wrong : %s' % (e)
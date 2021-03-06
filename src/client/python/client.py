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

Sample Python client for Barista
'''

try:
  transport = TSocket.TSocket('128.52.161.243', 9000)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = Barista.Client(protocol)

  transport.open()

  con_params = ConnectionParams(
    user="postgres", password="postgres", database="postgres", client_id="client_python", seq_id="1")

  con = client.open_connection(con_params)
  con.seq_id="2"
  res = client.execute_sql(con=con,
      query="SELECT 6.824 as id, 'Distributed Systems' as name",
      query_params=None)
  
  print "\t".join(res.field_names)
  for t in res.tuples:
    print "\t".join(t.cells)

  transport.close()
except Exception, e:
    print 'Something went wrong : %s' % (e)

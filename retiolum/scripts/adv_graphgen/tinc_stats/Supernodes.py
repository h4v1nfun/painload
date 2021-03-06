#!/usr/bin/python3

def find_potential_super(path="/etc/tinc/retiolum/hosts"):
  import os
  import re

  needle_addr = re.compile("Address\s*=\s*(.*)")
  needle_port = re.compile("Port\s*=\s*(.*)")
  for f in os.listdir(path):
    with open(path+"/"+f) as of:
      addrs = []
      port = "655"

      for line in of.readlines():

        addr_found = needle_addr.match(line)
        if addr_found:
          addrs.append(addr_found.group(1))

        port_found = needle_port.match(line)
        if port_found:
          port = port_found.group(1)
      
      if addrs : yield (f ,[(addr ,int(port)) for addr in addrs])

def try_connect(addr):
  try:
    from socket import socket,AF_INET,SOCK_STREAM
    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(2)
    s.connect(addr)
    s.settimeout(None)
    s.close()
    return addr
  except Exception as e:
    pass
    #return ()

def check_one_super(ha):
    host,addrs = ha
    valid_addrs = []
    for addr in addrs:
      ret = try_connect(addr)
      if ret: valid_addrs.append(ret)
    if valid_addrs: return (host,valid_addrs)

def check_all_the_super(path="/etc/tinc/retiolum/hosts"):
  from multiprocessing import Pool
  p = Pool(20)
  return filter(None,p.map(check_one_super,find_potential_super(path)))



if __name__ == "__main__":
  """
  usage
  """
  for host,addrs in check_all_the_super():
    print("%s %s" %(host,str(addrs)))

import os,sys
import libvirt
import json

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from client import build_vm_status 

ret = build_vm_status("sn1", "qemu:///system")
print json.dumps(ret)

#print ret

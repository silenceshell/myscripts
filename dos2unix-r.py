import os

path="/root/ovs"


xx = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn]
for i in xx :
    cmd="dos2unix " + i
    os.system(cmd)

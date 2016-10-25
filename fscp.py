#!/usr/bin/python
# -*- coding: utf-8 -

import pexpect
import sys

if len(sys.argv) != 3:
    print "Usage: fscp local_file user@addr:/dst_dir"

# We have many servers that use the same password. When scp files to them, it is boring to
# enter these complict characters. Use fscp will auto enter the password for these svs.
# Change the "XXX" to the correct password.
passwd="XXX"

src_file = sys.argv[1]
dst_host = sys.argv[2]
ssh = pexpect.spawn("scp %s %s" % (src_file, dst_host))
ret = 1024
try:
    res0 = ssh.expect(['password:', 'connecting (yes/no)?'], timeout=30)
    if res0 == 0:
        ssh.sendline(passwd)
        res1 = ssh.expect(['password:'], timeout=30)
        if res1 == 0:
            print "Password incorrect, fscp failed."
            ret = -1
    elif res0 == 1:
        ssh.sendline('yes\n')
        res1 = ssh.expect(['password:'], timeout=30)
        if res1 == 0:
            n = ssh.sendline(passwd)
except pexpect.EOF:
    print "Send %s succeed." % src_file
    ssh.close()
    ret = 0
except pexpect.TIMEOUT:
    ssh.close()
    ret = -2

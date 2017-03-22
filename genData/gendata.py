import sys
import string
import json
import random
import time
from fnmatch import fnmatch, fnmatchcase
import re

staticChars = string.ascii_letters+string.digits
staticCharLen = len(staticChars)

index_base = 1
index_new = False

bigint_max = sys.maxint
bigint_maxisset = False

def GenBoolean():
    return str(random.randint(0, 1))
def GenBigInt():
    return str(random.randint(0, sys.maxint))

def GenDouble():
    return str(random.uniform(0, sys.maxint))
def GenStaticStr(length):
    return ''.join([random.choice(staticChars) for i in range(length)])
def GenStr():
    length = random.randint(1, 10)  #you can edit here.
    return GenStaticStr(length)
def GenVarchar(ctype):
    repat = re.compile(r'VARCHAR\((\d+)')
    search_res = repat.search(ctype)
    if (search_res != None):
        length = int(repat.search(ctype).group(1))
        return GenStaticStr(length)
def GenDate():
    return time.strftime("%Y-%m-%d", time.localtime(random.uniform(0,time.time())))
def GenDateTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(random.uniform(0,time.time())))
def GenNull():
    return "";
def GenIndexIncr(ctype):
    global index_new
    global index_base
    if (index_new != True):
        repat = re.compile(r'INDEX\((\d+)')
        search_res = repat.search(ctype)
        if (search_res != None):
            index_base = int(repat.search(ctype).group(1))
        index_new = True
    else:
        index_base = index_base+1
    return str(index_base)
def GenBigIntByMax(ctype):
    global bigint_max
    global bigint_maxisset
    if bigint_maxisset != True:
        repat = re.compile(r'INTEGER\((\d+)')
        search_res = repat.search(ctype)
        if (search_res != None):
            bigint_max = int(repat.search(ctype).group(1))
            bigint_maxisset = True
    return str(random.randint(0, bigint_max))
funcs = {
    "BOOLEAN": GenBoolean,
    "BIGINT" : GenBigInt,
    "DOUBLE" : GenDouble,
    "STRING" : GenStr,
    "DATETIME" : GenDateTime,
    "DATE" : GenDate,
    "NULL" : GenNull
}

def GenData(ctype):
    newtype = ctype.upper().strip()
    if fnmatch(newtype, 'VARCHAR(*') == True:
        return GenVarchar(newtype)
    elif fnmatch(newtype, 'INDEX(*') == True:
        return GenIndexIncr(newtype)
    elif fnmatch(newtype, 'INTEGER(*') == True:
        return GenBigIntByMax(newtype)
    else:
        return funcs[newtype]()

def main():
    f = file("cfg.json")
    jscfg = json.load(f)

    lines = int(jscfg[u'table'][u'lines'])
    columes = str(jscfg[u'table'][u'columes']).split(',')

    filep = file(jscfg[u'filename'], 'w')
    while lines > 0:
        lines -= 1
        length = len(columes)
        length_end = len(columes)-1
        for i in range(length):
            filep.write(GenData(columes[i]))
            if (i != length_end):
                filep.write(',')
        filep.write('\n')
    filep.close()

if __name__ == "__main__":
    main()
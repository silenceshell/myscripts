# genData
A python script to generate data file on your disk.
- cfg.json : the configure file
- gendata.py :  the python script

It is very easy to use.

1. edit the configure file.
Now column types support BOOLEAN, BIGINT, DOUBLE, STRING, DATE, DATATIME, VCHAR(LEN), NULL, INDEX(BASE)
- STRING, u'll get a string which length is 1-10.
- VARCHAR(100), u'll get a string which length is 100.
- INDEX(1002), this column will be 1002,1003,1004,...

2. run gendata.py, you'll find a new file in the same dir.

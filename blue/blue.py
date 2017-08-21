#!/usr/bin/python
# coding=utf8

import argparse
import xml.etree.cElementTree as ET

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--xml', required=True, help='specify the xml file path')

args = parser.parse_args()
tree = ET.ElementTree(file=args.xml)


class Column:
    def __init__(self, name, type, value, description):
        self.name = name
        self.type = type
        self.value = value
        self.description = description

    def schema(self):
        return self.name + ' ' + self.type

    def strv(self):
        if self.type == "varchar(256)":
            return "\"" + self.value + "\""
        else:
            if self.value == "":
                return "0"
            else:
                return str(self.value)

    def __str__(self):
        return self.name + '(' + self.type + ')' + 'value is: ' + self.value + '(' + self.description + ')'


def convert_to_mysql(type):
    int_types = ['uint32', 'uint16', 'uint8', 'sint32']
    bigint_types = ['uint64']

    if type == 'string':
        return 'varchar(256)'
    elif type in int_types:
        return "int"
    elif type in bigint_types:
        return "bigint"
    else:
        return type


tables = {}

with open("output.sql", 'w+') as foutput:
    root = tree.getroot()
    for Component in root:
        classname = Component.attrib['Classname']
        key = Component.attrib['Key']
        columns = []
        for Property in Component:
            c_name = Property.attrib['NAME']
            c_type = convert_to_mysql(Property.attrib['TYPE'])

            value = ""
            display = ""
            for i in Property:
                if i.tag == "VALUE":
                    value = i.text if i.text else ""
                elif i.tag == "DisplayValue":
                    display = i.text if i.text else ""
            columns.append(Column(c_name.strip(), c_type.strip(), value.strip(), display.strip()))

        if classname not in tables:
            schema = ', '.join(c.schema() for c in columns)
            sql = "create table if not exists {classname} ({schema});".format(classname=classname, schema=schema)
            tables[classname] = sql
            # print sql
            foutput.write(sql + '\r\n')

        values = ', '.join(c.strv() for c in columns)
        insert_sql = "insert into {classname} values({values});".format(classname=classname, values=values)
        # print insert_sql
        foutput.write(insert_sql + '\r\n')

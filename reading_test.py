#!/usr/bin/env python3
from datetime import date

var1 =  str(date.today())
disallowed_characters = ".-!"

for characters in disallowed_characters:
    var1=var1.replace(characters,"")
log_file = f'{var1}.txt'
with open(log_file) as f:
    lines = f.readlines()

print (lines)
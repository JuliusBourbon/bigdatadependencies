#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    clean_line = re.sub(r'[.,;!?"\'-]', '', line)
    words = clean_line.strip().split()
    for word in words:
        print "%s\t1" % word
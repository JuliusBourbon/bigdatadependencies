import sys
import re

for line in sys.stdin:
    clean_line = re.sub(r'[.,;!?"\'-]', '', line).lower()
    words = clean_line.strip().split()
    for word in words:
        print(f"{word}\t1")
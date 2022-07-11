import sys
import re

new_spread = re.compile("^\d+$")

def clean_subs(path):
    with open(path) as f:
        last_line_a_number = False
        for line in f:
            clean_line = line.strip()
            if new_spread.match(clean_line):
                last_line_a_number = True
            elif last_line_a_number:
                last_line_a_number = False
            elif not clean_line:
                pass
            else:
                print(re.sub('<[^<]+?>', '', clean_line))


if __name__ == "__main__":
    clean_subs(sys.argv[1])
  

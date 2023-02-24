import sys
import re

new_spread = re.compile("^\d+$")

def read_subs(path):
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
                yield re.sub('<[^<]+?>', '', clean_line).strip()


def clean_subs(path):
    line_so_far = None
    for line in read_subs(path):
        if not line_so_far:
            line_so_far = line
        else:
            line_so_far = " ".join([line_so_far, line])
        if re.search("[.!?]”?$", line):
            yield line_so_far
            line_so_far = None


if __name__ == "__main__":
    srt = sys.argv[1]
    for line in clean_subs(sys.argv[1]):
        print(line)

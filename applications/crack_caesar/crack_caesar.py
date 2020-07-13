# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open('foo.txt', 'r') as f:
    f_contents=f.read()
    # print(f_contents)


def print_letter_count(s):
    counts = {}

    for c in s:
        # c = c.lower()  # case insensitive
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    items = list(counts.items())
    items.sort(key=lambda e: e[1])

    print(items)

# print_letter_count(f_contents)



encode_table = {
    'E': 'W',
    'T': 'J',
    'A': 'M',
    'O': 'X',
    'H': 'C',
    'N': 'D',
    'R': 'K',
    'I': 'I',
    'S': 'N',
    'D': 'U',
    'L': 'S',
    'W': 'O',
    'U': 'G',
    'G': 'Q',
    'F': 'B',
    'B': 'Y',
    'M': 'E',
    'Y': 'F',
    'C': 'A',
    'P': 'Z',
    'K': 'P',
    'V': 'H',
    'Q': 'V',
    'J': 'T',
    'X': 'L',
    'Z': 'R'
}

decode_table = {}


def build_decode_table():
    for key, value in encode_table.items():
        decode_table[value] = key

def decode(s):
    r = ""

    for c in s:
        if c in decode_table:
            r += decode_table[c]
        else:
            r += c

    return r

build_decode_table()


print(decode(f_contents))











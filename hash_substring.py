# python3

def read_input():
    input_type = input().rstrip().upper()
    if input_type == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        with open("sample.txt", "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hashes = [hash(text[i:i+p_len]) for i in range(t_len - p_len + 1)]
    return [i for i, h in enumerate(t_hashes) if h == p_hash]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))



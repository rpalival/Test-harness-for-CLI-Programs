#!/opt/homebrew/bin/python3
import argparse
import sys

#parsing file logic
def count_content(contents, count_lines, count_words, count_chars):
    lines = contents.splitlines() if count_lines else []
    words = contents.split() if count_words else []
    chars = len(contents) if count_chars else 0
    return len(lines), len(words), chars

#printing it this way for flag extension behavior
def print_counts(lines, words, chars, count_lines, count_words, count_chars, label=""):
    counts = []
    if count_lines:
        counts.append(f"{lines:8}")
    if count_words:
        counts.append(f"{words:8}")
    if count_chars:
        counts.append(f"{chars:8}")
    print(' '.join(counts) + f" {label}".rstrip())

def main():
    #initializing a argparse and keeping nargs=* so that my parser accepts multiple arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    #giving additional arguments for EXTENSION #2: allowing flag behavior of wc utility
    parser.add_argument('-l', '--lines', action = 'store_true')
    parser.add_argument('-w', '--words', action = 'store_true')
    parser.add_argument('-c', '--chars', action = 'store_true')
    args = parser.parse_args()

    # If no flags are provided, count everything
    if not (args.lines or args.words or args.chars):
        args.lines, args.words, args.chars = True, True, True

    total_lines, total_words, total_chars = 0, 0, 0
    error_occurred = False

    #this for loop is for EXTENSION #1: allowing multiple filenames behavior of wc utility
    for filename in args.filenames:
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                lines, words, chars = count_content(contents, args.lines, args.words, args.chars)
                total_lines += lines
                total_words += words
                total_chars += chars
                print_counts(lines, words, chars, args.lines, args.words, args.chars, filename)
        except Exception as e:
            print(f"Error processing {filename}: {e}", file=sys.stderr)
            error_occurred = True

    if len(args.filenames) > 1:
        print_counts(total_lines, total_words, total_chars, args.lines, args.words, args.chars, "total")

    #this if is to read stdin input
    if not args.filenames:
        try:
            contents = sys.stdin.read()
            lines, words, chars = count_content(contents, args.lines, args.words, args.chars)
            print_counts(lines, words, chars, args.lines, args.words, args.chars)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            error_occurred = True
            
    #exit status
    sys.exit(1 if error_occurred else 0)

if __name__ == "__main__":
    main()
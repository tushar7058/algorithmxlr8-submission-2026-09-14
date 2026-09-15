def main():
    n = int(input())
    s = list(input())
    removed = 0
    # repeatedly scan for a matching neighbor pair and remove one stone
    i = 1
    while i < len(s):
        if s[i] == s[i - 1]:
            del s[i]
            removed += 1
            # stay at the same position, the next stone shifted into it
        else:
            i += 1
    print(removed)


if __name__ == "__main__":
    main()
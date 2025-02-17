def len_word(word):
    if len(word) % 2 == 0:
        return True


words = input().split()
filtered_words = [x for x in words if len_word(x)]
print("\n".join(filtered_words))

#   -------------------------------------------------------------------------------
#                           TEXT ANALYSIS
#   -------------------------------------------------------------------------------

text = input(" Inter a Text :\n")

# Clear the text
clean = text.lower()
for ch in ".,!?;:\"()[]{}":
    clean = clean.replace(ch, " ")

words = clean.split()

# Statistic
total_words = len(words)
unique_words = set(words)
total_unique = len(unique_words)
avg_len = sum(len(w) for w in words) / total_words if words else 0

# Count per word repeat
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

# Sort by repetition (descending)
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("\n--- Text Statistics ---")
print(f"Total all words: {total_words}")
print(f"Unique words: {total_unique}")
print(f"Average word length: {avg_len:.2f}")

print("\n--- 5 most frequent words ---")
for word, count in sorted_freq[:5]:
    print(f"{word:15} → {count} times")

# Repeated letters
letters = [c for c in clean if c.isalpha()]
letter_freq = {}
for c in letters:
    letter_freq[c] = letter_freq.get(c, 0) + 1

top_letter = max(letter_freq, key=letter_freq.get)
print(f"\n Must repeated word: '{top_letter}' ({letter_freq[top_letter]} times)")
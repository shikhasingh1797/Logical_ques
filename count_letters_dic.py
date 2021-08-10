test_str="shikha"
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(all_freq)
print(all_freq.keys())
print(all_freq.values())
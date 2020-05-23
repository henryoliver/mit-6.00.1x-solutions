print('------------------')

s = 'azcbobobegghakl'
longestSubstring = ''

for i in range(len(s) - 2):
    substring = s[i]

    n = i

    while True:
        if n <= len(s) - 2 and s[n] <= s[n + 1]:
            substring += s[n + 1]
            n += 1
        else:
            break

    if len(longestSubstring) < len(substring):
        longestSubstring = substring

print('Longest substring in alphabetical order is: ' + str(longestSubstring))



def count_sort_letters(array, size, col, base, max_len):
  """ Helper routine for performing a count sort based upon column col """
  output = [0] * size
  count = [0] * (base + 1) # One addition cell to account for dummy letter
  min_base = ord('a') - 1 # subtract one too allow for dummy character

  for item in array: # generate Counts
    # get column letter if within string, else use dummy position of 0
    letter = ord(item[col]) - min_base if col < len(item) else 0
    count[letter] += 1

  for i in range(len(count)-1):   # Accumulate counts
      count[i + 1] += count[i]

  for item in reversed(array):
    # Get index of current letter of item at index col in count array
    letter = ord(item[col]) - min_base if col < len(item) else 0
    output[count[letter] - 1] = item
    count[letter] -= 1

  return output


def radix_sort_letters(array, max_col = None):
  """ Main sorting routine """
  if not max_col:
    max_col = len(max(array, key = len)) # edit to max length

  for col in range(max_col-1, -1, -1): # max_len-1, max_len-2, ...0
    array = count_sort_letters(array, len(array), col, 26, max_col)

  return array


def sorts1s2(s1, s2):
    #Create 3-grams
    s12 = []
    for s in s1:

        s12.append(s[0:3])
    for s in s2:
        s12.append(s[0:3])
    s12 = radix_sort_letters(s12)





if __name__ == "__main__":
    sequence = "mississippi"
    s0 = []
    s1 = []
    s2 = []

    # Create S0,S1,S2
    for i in range(len(sequence)):
        if i % 3 == 0:
            s0.append([sequence[i:], i, 0])
        elif i % 3 == 1:
            s1.append([sequence[i:], i, 0])
        else:
            s2.append([sequence[i:], i, 0])
    print(s0)
    print(s1)
    print(s2)

    s12 = []
    for s in s1:
        s12.append(s[0][0:3])
    for s in s2:
        s12.append(s[0][0:3])
    s12_sorted = radix_sort_letters(s12)
    print(s12_sorted)
    sorted_keys = []
    for i in s12_sorted:
        found = 0
        for item in s1:
            if item[0][0:3] == i and item[2] == 0:
                item[2] = 1
                sorted_keys.append(item[1])
                found = 1
                break

        if found == 0:
            for item in s2:
                if item[0][0:3] == i and item[2] == 0:
                    item[2] = 1
                    sorted_keys.append(item[1])
                    found = 1
                    break
    print(sorted_keys)
    for i in range(len(s12_sorted)-1):
        if s12_sorted[i] == s12_sorted[i+1]:
            pair = [sequence[sorted_keys[i]:], sequence[sorted_keys[i+1]:]]
            pair2 = radix_sort_letters(pair)
            if pair != pair2:
                mem = sorted_keys[i]
                sorted_keys[i] = sorted_keys[i+1]
                sorted_keys[i+1] = mem
    print(sorted_keys)

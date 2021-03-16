
def partition(arr, low, high, item):
    i = (low - 1)         # index of smaller element
    pivot = arr[high][item]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j][item] <= pivot:

            # increment index of smaller element
            i = i+ 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high, item):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high,item)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1,item)
        quickSort(arr, pi + 1, high, item)

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
    sequence = "abbbcccaaacacacaabababcbcbcaaaagggggtttgtgtgtgtgtgtbgbgbgbgbgbgagagagagagaacaccabcbcbcbgbgbggrgrgrgtgtgtgt"
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
    for i in range(len(s12_sorted)):
        found = 0
        for item in s1:
            if item[0][0:3] == s12_sorted[i] and item[2] == 0:
                item[2] = 1
                s12_sorted[i] = [s12_sorted[i], item[1], 1]
                sorted_keys.append(item[1])
                found = 1
                break

        if found == 0:
            for item in s2:
                if item[0][0:3] == s12_sorted[i] and item[2] == 0:
                    item[2] = 1
                    s12_sorted[i] = [s12_sorted[i], item[1], 2]
                    sorted_keys.append(item[1])
                    found = 1
                    break
    #TODO do quick sort inst4ead of swap
    print(sorted_keys)
    for i in range(len(s12_sorted)-1):
        if s12_sorted[i][0] == s12_sorted[i+1][0]:
            pair = [sequence[sorted_keys[i]:], sequence[sorted_keys[i+1]:]]
            pair2 = radix_sort_letters(pair)
            if pair != pair2:
                mem = sorted_keys[i]
                sorted_keys[i] = sorted_keys[i+1]
                sorted_keys[i+1] = mem
    print(sorted_keys)


    #sort s0
    #TODO sort
    c1 = []
    s0_altered = []
    for i in range(len(s0)):
        if len(s1) <= i:
            s0_altered.append([s0[i][0][0:1], "*"])
        else:
            s0_altered.append([s0[i][0][0:1], s1[i][1]])
    for i in range(len(s0_altered)-1):
        if s0_altered[i][0] == s0_altered[i+1][0]:
            for key in sorted_keys:
                if s0_altered[i][1] == key:
                    break
                if s0_altered[i+1][1] == key:
                    mem = s0_altered[i]
                    s0_altered[i] = s0_altered[i+1]
                    s0_altered[i+1] = mem
                    break

    c1 = s0_altered.copy()
    for item in range(len(c1)):
        c1[item] = [c1[item][0], c1[item][1], 0]
    for item in c1:
        if item[1] == "*":
            item[2] = -1
            break
        for i in range(len(sorted_keys)):
            if item[1] == sorted_keys[i]:
                item[2] = i
                break
    quickSort(c1, 0, len(c1)-1, 0)
    for i in range(len(c1)):
        j = i
        while c1[i][0] == c1[j][0]:
            j += 1
            if j==len(c1):
                break
        if j>i+1:
            quickSort(c1, i, j - 1, 2)

    c2 = []
    i = 0
    for item in c1:
        if item[1] != "*" and len(s1[int((item[1]-1)/3)][0][0:1]) != 0:
            element = [item[0]+s1[int((item[1]-1)/3)][0][0:1], item[1]+1, 0]
            c2.append(element)
        else:
            c2.append([item[0], "**", 0])
            # c2.append([s0[i][0][0:1], "**", 0])


    for item in c2:
        if item[1] == "**":
            item[2] = -1
            continue
        for i in range(len(sorted_keys)):
            if item[1] == sorted_keys[i]:
                item[2] = i
                break
    #change s12 sorted
    for item in range(len(s12_sorted)):
        if s12_sorted[item][2] == 1:
            gram = s12_sorted[item][0][0:1]
            for i in range(len(sorted_keys)):
                if sorted_keys[i] == s12_sorted[item][1]+1:
                    gram = gram+str(i)
                    break
            if gram == s12_sorted[item][0][0:1]:
                gram = gram+str(-1)
            s12_sorted[item] = [gram, s12_sorted[item][1], s12_sorted[item][2]]

        if s12_sorted[item][2] == 2:
            gram = s12_sorted[item][0][0:2]
            for i in range(len(sorted_keys)):
                if sorted_keys[i] == s12_sorted[item][1]+2:
                    gram = gram+str(i)
                    break
            if gram == s12_sorted[item][0][0:2]:
                gram = gram+str(-1)
            s12_sorted[item] = [gram, s12_sorted[item][1], s12_sorted[item][2]]
    quickSort(s12_sorted,0, len(s12_sorted)-1, 0)

    #change C1 and C2:
    for i in range(len(c1)):
        c1[i][0] = c1[i][0]+str(c1[i][2])
        c2[i][0] = c2[i][0]+str(c2[i][2])
    for i in range(len(c1)):
        if c1[i][1] != "*":
            c1[i][1] = c1[i][1] - 1
            c2[i][1] = c2[i][1] - 2

        else:
            c1[i][1] = max(sorted_keys) + 1
            c2[i][1] = max(sorted_keys) + 1

    #sort C1 and C2
    size_1 = len(s12_sorted)
    size_2 = len(c1)

    res = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if s12_sorted[i][2] == 1:
            if s12_sorted[i][0]<c1[j][0]:
                res.append(s12_sorted[i][1])
                i+=1
            else:
                res.append(c1[j][1])
                j+=1
        if s12_sorted[i][2] == 2:
            if s12_sorted[i][0]<c2[j][0]:
                res.append(s12_sorted[i][1])
                i+=1
            else:
                res.append(c2[j][1])
                j+=1
    if i == size_1:
        while j<size_2:
            res.append(c1[j][1])
            j+=1
    elif j == size_2:
        while i<size_1:
            res.append(s12_sorted[i][1])
            i+=1
    print(res)
    # res = res + s12_sorted[i:][1] + c1[j:][1]

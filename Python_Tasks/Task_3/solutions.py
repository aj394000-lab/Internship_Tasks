# Q1. Find the Frequency of Each Word in a Sentence.
def q1_word_frequency(sentence):
    a = sentence.split()
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    return b

# Q2. Find the Frequency of Each Character in a Word.
def q2_char_frequency(word):
    a = word
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    return b

# Q3. Find the First Non-Repeating Character in a Word.
def q3_first_non_repeating(word):
    a = word
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    d = 0
    for i in a:
        if b[i] == 1:
            d = i
            break
    return d

# Q4. Check Whether Two Strings Are Anagrams.
def q4_are_anagrams(s1, s2):
    d = None
    for i in s1:
        if i in s2:
            d = True
        else:
            d = False
    return d

# Q5. Find the First Repeating Character in a String.
def q5_first_repeating(word):
    a = word
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    d = 0
    for i in a:
        if b[i] > 1:
            d = i
            break
    return d

# Q6. Move All Zeros to the End of a List.
def q6_move_zeros(nums):
    a = nums
    d = []
    for i in a:
        if i > 0:
            d.append(i)
    for i in a:
        if i == 0:
            d.append(i)
    return d

# Q7. Find the Second Highest Distinct Number in a List.
def q7_second_highest(nums):
    a = nums
    d = sorted(list(set(a)), reverse=True)
    return d[1] if len(d) > 1 else None

# Q8. Remove Duplicates Without Changing the Original Order.
def q8_remove_duplicates(nums):
    a = nums
    seen = set()
    result = []
    for i in a:
        if i not in seen:
            seen.add(i)
            result.append(i)
    a = result
    return a

# Q9. Find the Missing Number from 1 to N.
def q9_find_missing(nums, N):
    a = N * (N + 1) // 2
    f = sum(nums)
    d = a - f
    return d

# Q10. Find Two Numbers Whose Sum Equals a Target.
def q10_two_sum(nums, target):
    result = None
    d = set()
    for i in nums:
        a = target - i
        if a in d:
            result = [a, i]
        d.add(i)
    return result

# Q11. Find the Number Closest to Zero.
def q11_closest_to_zero(nums):
    a = nums
    d = min(a, key=abs)
    return d

# Q12. Find Common Elements Between Two Lists.
def q12_common_elements(list1, list2):
    d = [i for i in list1 if i in list2]
    return d

# Q13. Rotate a List to the Right by K Positions.
def q13_rotate_list(nums, K):
    from collections import deque
    d = deque(nums)
    d.rotate(K)
    nums = list(d)
    return nums

# Q14. Find the Maximum Sum of Two Consecutive Elements.
def q14_max_consecutive_sum(nums):
    a = nums
    max_sum = a[0] + a[1]
    for i in range(len(a) - 1):
        current_sum = a[i] + a[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target.
def q15_all_pairs_sum(nums, target):
    result = [[nums[i], nums[j]] for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target]
    return result
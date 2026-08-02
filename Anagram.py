def check_anagram(str1, str2):
    # Step 1: Check length equality
    if len(str1) != len(str2):
        return False
    
    # Step 2: Initialize frequency tracking dictionaries
    count1 = {}
    count2 = {}
    
    # Step 3: Populate the first dictionary manually
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
            
    # Step 4: Populate the second dictionary manually
    for char in str2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
            
    # Step 5: Manually compare both dictionaries
    return count1 == count2

# --- Test the Program ---
word1 = "listen"
word2 = "silent"

# Call function and display results
if check_anagram(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are NOT anagrams.")
  

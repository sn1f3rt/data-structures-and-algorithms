## Intuition

Brute force solution would be to take each character in first string, and iterate over each character in second string. If a match is found, remove the character from the second string. Check the length of the second string at the end to get the result. TC: O(n^2), SC: O(1).

Optimal solution would be to use a fixed-size array. We know that for the validity of the anagram, both strings must be the same length, so we check that at beginning. Since we know english alphabet has 26 characters, we can create a fixed size array of 26 elements. We can run a common loop, for every character in the first string, we increment its position in the array by 1 and for every character in the second string we decrement its position by 1. In the end, we can check the array to see if all elements are 0. TC: O(n), SC: O(1) since array size is fixed.

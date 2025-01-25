## Intuition

Brute force approach would take each element, check against all other elements, then the next element against others, then next, and so on. TC: O(n)

Second-best approach will be to sort the array, and then check every element with the next element, if a match is found a duplicate exists. TC: O(log n) for sorting

Most optimal: keep track of all elements and access them quickly. Best DS for this - hash set - because it can access any element in O(1) time. TC: O(n) and SC:  O(n) for the new hash set

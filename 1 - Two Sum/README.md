## Intuition

Brute force approach would be to take each element and iterate over all other elements, add them and see if teh sum is equal to given target. TC: O(n^2), SC: O(1)

Another brute force approach is to take each element, subtract from target, and if the difference is more than 0 we perform a linear search on the array to see if the difference is present in the array or not. TC: O(n^2), SC: O(1)

If we sort the array, we can reduce the time complexity slightly as we can use binary search instead of linear search for the previous approach. TC: O(nlogn) for sorting, O(nlogn) for binary search, SC: O(1)

The optimal solution is to use a hashmap. For every element in the given array, we calculate its difference from the target and check if that value is present in the hashmap. If it is not present, we add the difference to the hashmap with its index as its value. If it is present, we return the index of the current element and the index of the element in the hashmap. TC: O(n), SC: O(n) for hashmap

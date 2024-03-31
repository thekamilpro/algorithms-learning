# Notes

Binary search lands in the middle of the array, and checkes whether the number is higher or lower than needed. If it's lower, it then goes in the middle of the lower part of the array util it finds the required number. If it's higher, it goes to higher part etc.
If value is not found it returns nothing.

Array for binary search must be in sorted from lowest to highest (e.g. names in address book) or from highest to lowest

Binary search is O(log n), as it cuts number of possible results by half with every step. It makes it much faster than simple search O(n) as it checks each element in array one by one.

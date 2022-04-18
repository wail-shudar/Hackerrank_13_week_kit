# Find the Median

The median of a list of numbers is essentially its middle element after sorting. The same number ofelements occur after it as before. Given a list of numbers with an odd number of elements, find the
median?

**Example**

*arr* = **[5, 3, 1, 2, 4]**

The sorted *arr'* = **[5, 3, 1, 2, 4]**. The middle element and the median is **3**

**Function Description**

Complete the *findMedian* function in the editor below.
*findMedian* has the following parameter(s):
* *int arr[n]:* an unsorted array of integers

**Returns**

* *int:* the median of the array

**Input Format**

The first line contains the integer *n*, the size of
*arr*.
The second line contains *n* space-separated integers *arr[i]*

**Constraints**

* 1 $\leq$ *n* $\leq$ 1000001
* *n* is odd
* -10000 $\leq$ *arr*[i] $\leq$ 10000

**Sample Input 0**

    7
    0 1 2 4 6 5 3

**Sample Output 0**

    3

**Explanation 0**

The sorted *arr* = **[5, 3, 1, 2, 4]**. It's middle element is at *arr*[**3**] = **3**
.
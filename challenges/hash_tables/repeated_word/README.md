# First repeated word

## Challenge
Function that can take in a lengthy piece of text and, using a hash table, return the first repeated word.

## Solution
![Solution](/assets/repeated_word.jpeg)

## Big-O
Time - Worst Case is when every word happens to have the same hash. In this case,we would need to loop through the subarray every time we set a new key. When doing this, the subarray is growing by 1 each time. So the number of operations in the set method would be 1 + 2 + 3 + ... + n. This is Gauss' formula to sum a series... $\dfrac{n(n+1)}{2}$. Since this method is called within a for loop, the worst case would be O($\dfrac{n^2(n+1)}{2}$). This is on the order of O(n<sup>3</sup>). More realistically, the hash function hashes keys more uniquely, in which case we would have O(n).

Space - O(n)

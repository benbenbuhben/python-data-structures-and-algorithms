# Find Edges

## Challenge
Given a business trip itinerary, and an Alaska Airlines route map, is the trip possible with direct flights? If so, how much will the total trip cost be?

## Solution
![Solution](/assets/get_edges.JPG)

## Big-O
Time: O(n<sup>2</sup>)
Space: O(1)

Note on Big-O: My Adjacency lists are stored as python lists. Therefore, I have a nested for loop. In the worst case where the itinerary includes every city the airline services, and each city's adjacency list contains every other city, then  Big-O of time would be O(n<sup>2</sup>). For any practical case, I would argue that the Big-O is O(n).

# Some Basic Questions and Their Answers
## 1. First: what is an algorithm?
Suppose you have:
[4, 7, 2, 9, 1]

and want to find 9.
One algorithm is:
Check 4
Check 7
Check 2
Check 9 → found

That's Linear Search.
The important question isn't only:
"Does it work?"

We also ask:
"How much work will it do as the input gets bigger?"


## 2. What is n?
n simply represents the size of the input.
Example:
arr = [10, 20, 30, 40, 50]


There are 5 elements.
So:
n = 5

For:
arr = [10, 20, 30, ... 1,000 elements]


then:
n = 1000

We care about what happens when n becomes large.

## 3. What does time complexity actually mean?
Forget the confusing phrase "time complexity" for a moment.
Think:
How does the amount of work grow when the input grows?

Consider:
print(arr[0])


Whether arr contains 10 elements or 10 million elements, we're accessing one location.
The work doesn't grow with n.
So:
O(1)
This means constant growth

Now:
for x in arr:    print(x)


For:
n = 5      → about 5 iterations
n = 100    → about 100 iterations
n = 1000   → about 1000 iterations

Work grows with n.
Therefore:
O(n)
That's exactly the kind of growth MIT and standard algorithm-analysis texts call linear. MIT OpenCourseWare
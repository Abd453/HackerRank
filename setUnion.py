# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input
num_english = int(input().strip())
english_subscribers = set(input().strip().split())
num_french = int(input().strip())
french_subscribers = set(input().strip().split())

# Convert roll numbers to integers for set operations
english_subscribers = set(map(int, english_subscribers))
french_subscribers = set(map(int, french_subscribers))

# Find students who are subscribed to at least one newspaper
all_subscribers = english_subscribers.union(french_subscribers)

# Output the total number of unique students with at least one subscription
print(len(all_subscribers))

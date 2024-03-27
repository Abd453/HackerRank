if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Convert map object to list and remove duplicates by converting to set
    arr = list(set(arr))
    
    # Sort the list in descending order
    arr.sort(reverse=True)
    
    # If there's only one element, the second maximum doesn't exist
    if len(arr) == 1:
        print("Second maximum doesn't exist")
    else:
        print(arr[1])  # Second maximum element


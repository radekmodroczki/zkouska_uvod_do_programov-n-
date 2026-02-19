import sys

def bubble_sort(arr):
    n = len(arr)
   
    # Sort the array using Bubble Sort algorithm
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr

def unique(arr):
    n = len(arr)
    ret = []

    # Filter out duplicate values from the sorted array
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            continue
        else:
            ret.append(arr[i])

    if n > 0:
        ret.append(arr[n - 1])

    return ret

def get_union(a, b):
    # Sort and remove duplicates from both input arrays
    a_sorted = bubble_sort(a)
    b_sorted = bubble_sort(b)

    a_unique = unique(a_sorted)
    b_unique = unique(b_sorted)

    m = len(a_unique)
    n = len(b_unique)

    i = 0
    j = 0
    new_val = 0
    last_val = None
    ret = []

    # Merge both sequences into one, keeping ascending order
    while(i < m and j < n):
        if a_unique[i] < b_unique[j]:
            new_val = a_unique[i]
            i = i + 1
        elif a_unique[i] > b_unique[j]:
            new_val = b_unique[j]
            j = j + 1
        else:
            new_val = a_unique[i]
            i = i + 1
            j = j + 1
        
        if new_val != last_val:
            ret.append(new_val)
            last_val = new_val

        # Add remaining elements from A or B if any are left
        while(i < m):
            if (a_unique[i] != last_val):
                ret.append(a_unique[i])
                last_val = a_unique[i]
            i = i + 1

        while(j < n):
            if (b_unique[j] != last_val):
                ret.append(b_unique[j])
                last_val = b_unique[j]
            j = j + 1
    
    return ret


if __name__ == "__main__":
    print("--- Union of Two Sequences ---")
    
    # Ask the user for the filename or use a default one
    filename = input("Enter the filename (e.g., data.txt): ").strip()
    if not filename:
        filename = "sequences.txt"
        print(f"No input provided. Trying default file: '{filename}'")

    try:
        # Open and read lines from the file
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        if len(lines) < 2:
            print("Error: The file must contain at least two lines of numbers.")
            sys.exit(1)

        # Parse the strings into integer lists
        list_a = [int(x) for x in lines[0].split()]
        list_b = [int(x) for x in lines[1].split()]

        print(f"Loaded {len(list_a)} numbers from Sequence A, {len(list_b)} numbers from Sequence B.")

        # Calculate and print the final union
        result = get_union(list_a, list_b)
        
        print("-" * 30)
        print("Resulting Union:")
        
        print(", ".join(map(str, result)))
        
        print(f"Number of unique elements: {len(result)}")
        print("-" * 30)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please make sure it's in the same folder as this script.")
    except ValueError:
        print("Error: The file contains invalid characters. Make sure it only contains numbers separated by spaces.")
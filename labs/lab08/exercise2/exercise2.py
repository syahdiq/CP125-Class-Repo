def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """

    # Step 1: Read both files
    f1 = open(file1, "r")
    list1 = f1.readlines()
    f1.close()

    f2 = open(file2, "r")
    list2 = f2.readlines()
    f2.close()

    # Step 2: Process (remove duplicates using a set)
    names = set()

    for name in list1 + list2:
        names.add(name.strip())  # remove newline characters

    # Step 3: Sort alphabetically
    sorted_names = sorted(names)

    # Step 4: Write to output file
    f = open(output_file, "w")
    for name in sorted_names:
        f.write(name + "\n")
    f.close()

    return len(sorted_names)


# Test your code here
result = merge_lists(
    "labs/lab08/exercise2/data/list1.txt",
    "labs/lab08/exercise2/data/list2.txt",
    "labs/lab08/exercise2/data/merged.txt"
)
print(f"Unique names: {result}")
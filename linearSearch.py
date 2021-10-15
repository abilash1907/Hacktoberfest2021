def linearSearch(arr1, value):
    for i in range(len(arr1)):
        if arr1[i] == value:
            return i
    return -1


input_str1 = input("Enter elements of the first array separated by space: ")
print("\n")
arr = input_str1.split()  # to convert the input string to list
print("array: ", arr)

for i in range(len(arr)):  # to convert each element to integer type
    arr[i] = int(arr[i])
num = input("enter the number to search:")

a = linearSearch(arr, int(num))
if a == -1:
    print("Element not present")
else:
    print("Element present at position", a + 1)

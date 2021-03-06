# Python 3 program for recursive
# Modifications needed for the older Python 2 are found in comments.
# Returns index of x in arr if present, else -1
def main(arr, low, high, x):
	# Check base case
	if high >= low:
		mid = (high + low) // 2
		# If element is present at the middle itself
		if arr[mid] == x:
			return mid
		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return main(arr, low, mid - 1, x)
		# Else the element can only be present in right subarray
		else:
			return main(arr, mid + 1, high, x)
	else:
		# Element is not present in the array
		return -1


# Jupyter Notebook: NumPy Basics - Detailed Explanations with Line-by-Line Comments

# ------------------------
# 1. Importing NumPy
# ------------------------
import numpy as np  # Import NumPy library as 'np' for convenience

# ------------------------
# 2. Creating Arrays
# ------------------------

# 1D array from a Python list
arr1 = np.array([1, 2, 3, 4, 5])  # Create 1D array
print("1D array:", arr1)  # Print the array
print("Shape:", arr1.shape)  # Shape of array (number of elements in each dimension)
print("Data type:", arr1.dtype)  # Data type of array elements

# 2D array (matrix) from a list of lists
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # Create 2x3 array
print("\n2D array:")
print(arr2)
print("Shape:", arr2.shape)  # 2 rows, 3 columns

# Array with zeros
zeros = np.zeros((3, 4))  # 3x4 array filled with zeros
print("\nZeros array:")
print(zeros)

# Array with ones
ones = np.ones((2, 3))  # 2x3 array filled with ones
print("\nOnes array:")
print(ones)

# Array with a specific value
full_array = np.full((2, 2), 7)  # 2x2 array filled with 7
print("\nFull array with 7s:")
print(full_array)

# Array with range of numbers
arr_range = np.arange(0, 10, 2)  # Start=0, Stop=10, Step=2
print("\nArray with range 0 to 10 step 2:")
print(arr_range)

# Linearly spaced array
arr_linspace = np.linspace(0, 1, 5)  # 5 numbers evenly spaced between 0 and 1
print("\nLinearly spaced array:")
print(arr_linspace)

# ------------------------
# 3. Array Properties
# ------------------------

arr = np.array([[1, 2, 3], [4, 5, 6]])  # Create 2x3 array
print("\nArray:")
print(arr)

print("Number of dimensions (ndim):", arr.ndim)  # Number of dimensions
print("Shape of array:", arr.shape)  # Shape of array
print("Total elements (size):", arr.size)  # Total number of elements
print("Data type (dtype):", arr.dtype)  # Type of elements

# ------------------------
# 4. Indexing and Slicing
# ------------------------

# 1D array indexing
arr1 = np.array([10, 20, 30, 40, 50])  # 1D array
print("\nOriginal 1D array:", arr1)
print("First element:", arr1[0])  # Index 0
print("Last element:", arr1[-1])  # Last element using negative index

# 1D array slicing
print("Elements from index 1 to 3:", arr1[1:4])  # Slice from index 1 to 3 (4 not included)
print("Every second element:", arr1[::2])  # Step of 2

# 2D array indexing
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 3x3 array
print("\nOriginal 2D array:")
print(arr2)
print("Element at row 1, column 2:", arr2[1, 2])  # Access element at 2nd row, 3rd column

# 2D slicing
print("First two rows, all columns:")
print(arr2[:2, :])  # Rows 0-1, all columns
print("All rows, columns 1 to 2:")
print(arr2[:, 1:3])  # All rows, columns 1-2

# ------------------------
# 5. Array Operations
# ------------------------

arr1 = np.array([1, 2, 3, 4])  # First array
arr2 = np.array([5, 6, 7, 8])  # Second array

# Element-wise addition, subtraction, multiplication, division
print("\nElement-wise addition:", arr1 + arr2)  # Add corresponding elements
print("Element-wise subtraction:", arr1 - arr2)  # Subtract corresponding elements
print("Element-wise multiplication:", arr1 * arr2)  # Multiply corresponding elements
print("Element-wise division:", arr2 / arr1)  # Divide corresponding elements

# Universal functions (ufuncs)
print("\nSquare root:", np.sqrt(arr1))  # Square root of each element
print("Exponential:", np.exp(arr1))  # e^x for each element
print("Sine:", np.sin(arr1))  # Sine of each element (in radians)

# Aggregation functions
print("\nSum of arr1:", np.sum(arr1))  # Sum of all elements
print("Minimum:", np.min(arr1))  # Minimum element
print("Maximum:", np.max(arr1))  # Maximum element
print("Mean:", np.mean(arr1))  # Average
print("Standard deviation:", np.std(arr1))  # Standard deviation

# ------------------------
# 6. Reshaping and Flattening
# ------------------------

arr = np.arange(12)  # Array from 0 to 11
print("\nOriginal array:", arr)

# Reshape to 3x4
arr_reshaped = arr.reshape(3, 4)  # Reshape into 3 rows, 4 columns
print("Reshaped array (3x4):")
print(arr_reshaped)

# Flatten back to 1D
arr_flat = arr_reshaped.flatten()  # Convert 2D array back to 1D
print("Flattened array:", arr_flat)

# Transpose
print("\nTranspose of reshaped array:")
print(arr_reshaped.T)  # Swap rows and columns

# ------------------------
# 7. Boolean Indexing and Conditions
# ------------------------

arr = np.array([10, 15, 20, 25, 30])  # 1D array
print("\nOriginal array:", arr)

# Condition: elements greater than 20
cond = arr > 20  # Boolean array where condition is True or False
print("Condition array (arr > 20):", cond)
print("Filtered elements:", arr[cond])  # Apply condition to filter array

# Combine condition with logical operators
print("Elements between 15 and 30:", arr[(arr > 15) & (arr < 30)])  # Logical AND

# ------------------------
# 8. Stacking and Splitting Arrays
# ------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical stack
v_stack = np.vstack((a, b))  # Stack arrays vertically (rows)
print("\nVertical stack:")
print(v_stack)

# Horizontal stack
h_stack = np.hstack((a, b))  # Stack arrays horizontally (columns)
print("Horizontal stack:")
print(h_stack)

# Splitting arrays
arr = np.arange(10)  # 0 to 9
split_arr = np.array_split(arr, 3)  # Split array into 3 parts
print("\nSplit array:")
for part in split_arr:
    print(part)

# ------------------------
# 9. Random Numbers
# ------------------------

# Random integers
rand_int = np.random.randint(0, 10, size=(2, 3))  # 2x3 array with integers 0-9
print("\nRandom integers:")
print(rand_int)

# Random floats between 0 and 1
rand_float = np.random.rand(2, 3)  # 2x3 array of floats 0-1
print("\nRandom floats:")
print(rand_float)

# Random normal distribution
rand_normal = np.random.randn(2, 3)  # 2x3 array, mean=0, std=1
print("\nRandom normal distribution:")
print(rand_normal)
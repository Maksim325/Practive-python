from array import array

def test_arrays():
    arr = array("i", [1, 2, 3, 4, 5, 6, 7])

    print(arr) #array("i", [1, 2, 3, 4,])
    #index
    print(f"Index of 0 element: {arr[0]}") #1
    print(arr[-1]) #7

    #slice
    print(f"Slised array: {arr[0:4]}") #array('i', [1, 2, 3, 4])
    print(f"Slised array:{arr[3:]}") #array('i', [4, 5, 6, 7])

    #Find out the data type of the array
    print(arr.typecode) #i

    #combining arrays
    arr2 = array("i", [8, 9, 10])
    print(arr + arr2) #array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    arr.append(10) #array('i', [1, 2, 3, 4, 5, 6, 7, 10])
    print(arr)
    print(arr.count(2)) # 1

    #search by index
    print(arr.index(3)) # 2

    #delete by index
    print(arr.pop()) #10
    print(arr)

    # remove the first occurence of item with given value
    arr.remove(3)
    print(arr) #array('i', [1, 2, 4, 5, 6, 7])
    
def main():
    test_arrays()

if __name__ == '__main__':
    main()



def checkPairSumExists(rows, cols, arr, sum):

    seen = set()
    for i in range(len(rows)):
        for j in range(len(cols)):
            if seen.contains(sum-arr[i][j]):
                return True
            seen.add(arr[i][j])

    return False



if __name__ == "__main__":

    print("hello world")

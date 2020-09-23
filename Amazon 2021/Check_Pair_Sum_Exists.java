import java.util.*;
class Main {

  static Boolean checkPairSumExists(int rows, int cols, int[][] arr, int sum) {

    Set<Integer> seen = new HashSet<Integer>();

    for(int i = 0; i < rows; i++) {
      for(int j = 0; j < cols; j++) {
        if (seen.contains(sum-arr[i][j])) {
          return true;
        } else {
          seen.add(arr[i][j]);
        }
      }
    }
    return false;
  }

  public static void main(String[] args) {
    int[][] arr = {{1,1,1,1}, {1,1,1,1}};

    System.out.println(checkPairSumExists(2, 4, arr, 3));
  }
}

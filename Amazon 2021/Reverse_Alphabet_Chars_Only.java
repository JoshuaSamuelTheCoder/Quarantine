class Main {


  static String reverseAlphabetCharsOnly(String inputString) {

    char[] inputChar = inputString.toCharArray();
    int right = inputString.length() - 1;
    int left = 0;
    while(left < right && left >=0) {
      if(!Character.isAlphabetic(inputChar[left])) {
        left++;
      } else if(!Character.isAlphabetic(inputChar[right])) {
        right--;
      } else {
        char temp = inputChar[left];
        inputChar[left] = inputChar[right];
        inputChar[right] = temp;
        left++;
        right--;
      }
    }
    return new String(inputChar);

  }

  public static void main(String[] args) {
    System.out.println(reverseAlphabetCharsOnly("55555gf56789"));
  }
}

class Main {

  static int calculateSumOfNumbersInString(String inputString) {
     String temp = "";
     int sum = 0;

     for(int i = 0; i < inputString.length(); i++) {

       char ch = inputString.charAt(i);
       if(Character.isDigit(ch)) {
         temp += ch;
       } else {
         sum += Integer.parseInt(temp);
         temp = "0";
       }

     }
     return sum + Integer.parseInt(temp);
   }

   public static void main(String[] args) {
     System.out.println(calculateSumOfNumbersInString("100a10a"));
   }

}

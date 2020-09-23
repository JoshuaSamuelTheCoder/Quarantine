import java.io.*;
import java.util.*;
import java.lang.*;

class Main {

    static boolean is_vowel(char ch) {
      return (ch == 'a') || (ch == 'e') || (ch == 'i') || (ch == 'o') || (ch == 'u');
    }

    static String removeConsecutiveVowels(String str) {

      String st = "" + str.charAt(0);

      for(int i = 1; i < str.length(); i++) {
        if (is_vowel(str.charAt(i-1)) && is_vowel(str.charAt(i))) {
          continue;
        } else {
          st = st + str.charAt(i);
        }
      }

      return st;

    }

  public static void main(String[] args) {
    System.out.println(removeConsecutiveVowels("aeeeeeefff"));
  }
}

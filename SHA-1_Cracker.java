//crack SHA-1 160 bit hash from wordlist

import java.io.*;
import java.util.*;
import java.security.*;

public class SHA-1_Cracker {
    public static void main(String[] args) throws Exception {
        // read in the hash
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the SHA-1 hash: ");
        String hash = sc.nextLine();
        // read in the wordlist
        System.out.print("Enter the wordlist file name: ");
        String filename = sc.nextLine();
        File file = new File(filename);
        Scanner fileScanner = new Scanner(file);
        // loop through the wordlist
        while (fileScanner.hasNextLine()) {
            String word = fileScanner.nextLine();
            // hash the word
            MessageDigest md = MessageDigest.getInstance("SHA-1");
            md.update(word.getBytes());
            byte[] digest = md.digest();
            // convert the hash to hex
            String hex = "";
            for (byte b : digest) {
                hex += String.format("%02x", b);
            }
            // compare the hashes
            if (hex.equals(hash)) {
                System.out.println("The password is: " + word);
                break;
            }
        }
    }
}

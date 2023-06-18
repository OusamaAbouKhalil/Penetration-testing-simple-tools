//crack SHA-256 hash from wordlist

import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class SHA_256_Cracker {

    public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the hash to be cracked");
        String hash = sc.nextLine();
        System.out.println("Enter the wordlist file path");
        String wordlist = sc.nextLine();
        BufferedReader br = new BufferedReader(new FileReader(wordlist));
        String line;
        while ((line = br.readLine()) != null) {
            if (hash.equals(sha256(line))) {
                System.out.println("The password is " + line);
                break;
            }
        }
    }

    public static String sha256(String input) throws NoSuchAlgorithmException {
        MessageDigest mDigest = MessageDigest.getInstance("SHA-256");
        byte[] result = mDigest.digest(input.getBytes());
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < result.length; i++) {
            sb.append(Integer.toString((result[i] & 0xff) + 0x100, 16).substring(1));
        }
        return sb.toString();

    }
}

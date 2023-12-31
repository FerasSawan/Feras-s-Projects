/**
 *Prompts the user for 2 fractions and displays the two fractions, multipided, added, subracted, and divided. The fractions are also simplified.
 * Feras Sawan
 * 1/09/2022
 */


import java.util.Scanner;
import java.lang.Math;

public class fractions {
    public static void main(String[] args) {
        int numerator1 = 0;
        int denominator1 = 0;
        int numerator2 = 0;
        int denominator2 = 0;

        Scanner input = new Scanner(System.in);

        boolean checker1 = true;
        while (checker1) {
            try {
                System.out.print("Enter the numerator for the first fraction: ");
                String numberStr = input.nextLine();
                numerator1 = Integer.parseInt(numberStr);
                checker1 = false;
            } catch (Exception e) {
                System.out.println("Please input a valid number!!!");
            }
        }

        boolean checker2 = true;
        while (checker2) {
            try {
                System.out.print("Enter the denominator for the first fraction: ");
                String numberStr = input.nextLine();
                denominator1 = Integer.parseInt(numberStr);
                if (denominator1 == 0) {
                    System.out.println("Please input a non-zero number!!!");
                    continue;
                }
                checker2 = false;
            } catch (Exception e) {
                System.out.println("Please input a valid number!!!");
            }
        }

        boolean checker3 = true;
        while (checker3) {
            try {
                System.out.print("Enter the numerator for the second fraction: ");
                String numberStr = input.nextLine();
                numerator2 = Integer.parseInt(numberStr);
                checker3 = false;
            } catch (Exception e) {
                System.out.println("Please input a valid number!!!");
            }
        }

        boolean checker4 = true;
        while (checker4) {
            try {
                System.out.print("Enter the denominator for the second fraction: ");
                String numberStr = input.nextLine();
                denominator2 = Integer.parseInt(numberStr);
                if (denominator2 == 0) {
                    System.out.println("Please input a non-zero number!!!");
                    continue;
                }
                checker4 = false;
            } catch (Exception e) {
                System.out.println("Please input a valid number!!!");
            }
        }

        input.close();

        System.out.println();

        add(numerator1, denominator1, numerator2, denominator2);
        System.out.println();
        subtract(numerator1, denominator1, numerator2, denominator2);
        System.out.println();
        multiply(numerator1, denominator1, numerator2, denominator2);
        System.out.println();
        divide(numerator1, denominator1, numerator2, denominator2);
        System.out.println();
    }

    public static void add(int numerator1, int denominator1, int numerator2, int denominator2) {
        int numerator3 = numerator1 * denominator2 + numerator2 * denominator1;
        int denominator3 = denominator1 * denominator2;

        simplify(numerator1, denominator1);
        System.out.print(" + ");
        simplify(numerator2, denominator2);
        System.out.print(" = ");
        simplify(numerator3, denominator3);
    }

    public static void subtract(int numerator1, int denominator1, int numerator2, int denominator2) {
        int numerator3 = numerator1 * denominator2 - numerator2 * denominator1;
        int denominator3 = denominator1 * denominator2;

        simplify(numerator1, denominator1);
        System.out.print(" - ");
        simplify(numerator2, denominator2);
        System.out.print(" = ");
        simplify(numerator3, denominator3);
    }

    public static void multiply(int numerator1, int denominator1, int numerator2, int denominator2) {
        int numerator3 = numerator1 * numerator2;
        int denominator3 = denominator1 * denominator2;

        simplify(numerator1, denominator1);
        System.out.print(" * ");
        simplify(numerator2, denominator2);
        System.out.print(" = ");
        simplify(numerator3, denominator3);
    }

    public static void divide(int numerator1, int denominator1, int numerator2, int denominator2) {
        int numerator3 = numerator1 * denominator2;
        int denominator3 = denominator1 * numerator2;

        simplify(numerator1, denominator1);
        System.out.print(" / ");
        simplify(numerator2, denominator2);
        System.out.print(" = ");
        simplify(numerator3, denominator3);
    }

    public static void simplify(int numerator, int denominator) {
        int gcd = 1;
        for (int i = 1; i <= Math.abs(numerator) && i <= Math.abs(denominator); i++) {
            if (numerator % i == 0 && denominator % i == 0) {
                gcd = i;
            }
        }

        int numeratorSimplified = numerator / gcd;
        int denominatorSimplified = denominator / gcd;

        if (numeratorSimplified < 0 && denominatorSimplified < 0) {
            numeratorSimplified = Math.abs(numeratorSimplified);
            denominatorSimplified = Math.abs(denominatorSimplified);
        }

        if (numeratorSimplified == 0) {
            System.out.print(0);
        } else if (denominatorSimplified == 1) {
            System.out.print(numeratorSimplified);
        } else if (numeratorSimplified == denominatorSimplified) {
            System.out.print(1);
        } else {
            System.out.print(numeratorSimplified + "/" + denominatorSimplified);
        }
    }
}
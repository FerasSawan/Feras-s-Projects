/*
Author - Feras Sawan
Date - 3/19/2023
Purpose - Displays seats in a theater and has user choose to select a seat or price from the movie theater until the user stops
*/

import java.util.Arrays;
import java.util.Scanner;
public class Main1 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String[][] seats = {
                {"10", "10", "10", "10", "10", "10", "10", "10", "10", "10"},
                {"10", "10", "10", "10", "10", "10", "10", "10", "10", "10"},
                {"10", "10", "10", "10", "10", "10", "10", "10", "10", "10"},
                {"10", "10", "20", "20", "20", "20", "20", "20", "10", "10"},
                {"10", "10", "20", "20", "20", "20", "20", "20", "10", "10"},
                {"10", "10", "20", "20", "20", "20", "20", "20", "10", "10"},
                {"20", "20", "30", "30", "40", "40", "30", "30", "20", "20"},
                {"20", "30", "30", "40", "50", "50", "40", "30", "30", "20"},
                {"30", "40", "50", "50", "50", "50", "50", "50", "40", "30"},
        };
        printSeating(seats);
        System.out.println("Please pick a seat, price or quit the program. To pick a seat, enter 'seat'. To pick price, enter 'price'. To quit, enter 'quit'");
        String a = s.nextLine();
        do {
            if (a.equals("quit")) {
                break;
            }
            if (a.equals("seat")) {
                int r, c;
                while (true) {
                    while (true) {
                        try {
                            System.out.println("Please enter the row of the seat you want (1-9)");
                            r=Integer.parseInt(s.nextLine());
                            if ( r > 9 || r < 1) {
                                System.out.println("Please enter the collum of the seat you want  (1-10)");
                            } else {
                                break;
                            }
                        } catch (Exception e) {
                            System.out.println("Please enter a valid number. ");
                        }
                    }
                    while (true) {
                        try {
                            System.out.println("Please enter the seat number (1-9)");
                            c=Integer.parseInt(s.nextLine());
                            if (c > 0 && c < 10) {
                                break;
                            } else {
                                System.out.println("Please enter a number between 1 and 9.");
                            }
                        } catch (Exception e) {
                            System.out.println("Please enter a valid number. ");
                        }
                    }
                    if (!seats[r-1][c-1].equals("00")) {
                        System.out.println("You have chosen seat " + c + " in row " + r + ". This seat costs $" + seats[r-1][c-1]);
                        break;
                    }else{
                    System.out.println("This seat was taken already. Please choose another seat. ");
                    }
                }
                seats[r-1][c-1]="00";
            } else if (a.equals("price")) {
                while (true) {
                    int[] c;
                    int p = 0;
                    while (true) {
                        try {
                            System.out.println("Please enter the price of the seat that you want. Valid prices are 10, 20, 30, 40 and 50");
                            p = Integer.parseInt(s.nextLine());
                            if (p != 10 && p != 20 && p != 30 && p != 40 && p != 50) {
                                System.out.println("Please enter 10, 20, 30, 40 or 50");
                            } else {
                                break;
                            }
                        } catch (Exception e) {
                            System.out.println("Please enter a valid number");
                        }
                    }
                    c=indexOfPrice(seats, String.valueOf(p));
                    if (c[0] == -1) {
                        System.out.println("There are no seats with this price. Please pick another. ");
                    } else {
                        seats[c[0]][c[1]] = "00";
                        System.out.println("You chose seat " + (c[1]+1) + " in row " + (c[0]+1));
                        break;
                    }
                }
            } else {
                System.out.println("Please enter a valid input.\nPlease pick a seat, price or quit the program. To pick a seat, enter 'seat'. To pick price, enter 'price'. To quit, enter 'quit'");
                a=s.nextLine();
                continue;
            }
            printSeating(seats);
            System.out.println("Please pick a seat, price or quit the program. To pick a seat, enter 'seat'. To pick price, enter 'price'. To quit, enter 'quit'");
            a = s.nextLine();
        } while (!a.equals("quit"));

        System.out.println("The program is terminating. ");
    }
    public static void printSeating(String[][] seats) {
        System.out.println("The seats and prices for the theater.");
        System.out.print("Seat number:\n       ");
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + "   ");
        }
        System.out.println();
        for (int i = 0; i < seats.length; i++) {
            System.out.println("Row " + (i+1)  + " " + Arrays.toString(seats[i]));
        }
    }

    public static int[] indexOfPrice(String[][] seats, String target) {
        for (int i = 0; i < seats.length; i++) {
            for (int j = 0; j < seats[i].length; j++) {
                if (seats[i][j].equals(target)) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[] {-1,-1};
    }
}
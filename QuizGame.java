import java.util.Scanner;

public class QuizGame {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int score = 0;

        System.out.println("======================================");
        System.out.println("          WELCOME TO QUIZ GAME        ");
        System.out.println("======================================");
        System.out.println("Answer the following questions.");
        System.out.println("Enter the option number (1-4).");
        System.out.println("--------------------------------------");

        // Question 1
        System.out.println("\nQuestion 1:");
        System.out.println("What is the capital of India?");
        System.out.println("1. Mumbai");
        System.out.println("2. New Delhi");
        System.out.println("3. Chennai");
        System.out.println("4. Kolkata");

        System.out.print("Enter your answer: ");
        int answer1 = scanner.nextInt();

        if (answer1 == 2) {
            System.out.println("Correct! 🎉");
            score++;
        } else {
            System.out.println("Wrong answer!");
            System.out.println("Correct answer: New Delhi");
        }

        // Question 2
        System.out.println("\nQuestion 2:");
        System.out.println("Which planet is known as the Red Planet?");
        System.out.println("1. Earth");
        System.out.println("2. Jupiter");
        System.out.println("3. Mars");
        System.out.println("4. Venus");

        System.out.print("Enter your answer: ");
        int answer2 = scanner.nextInt();

        if (answer2 == 3) {
            System.out.println("Correct! 🎉");
            score++;
        } else {
            System.out.println("Wrong answer!");
            System.out.println("Correct answer: Mars");
        }

        // Question 3
        System.out.println("\nQuestion 3:");
        System.out.println("Which language is primarily used for Android development?");
        System.out.println("1. Kotlin");
        System.out.println("2. HTML");
        System.out.println("3. SQL");
        System.out.println("4. CSS");

        System.out.print("Enter your answer: ");
        int answer3 = scanner.nextInt();

        if (answer3 == 1) {
            System.out.println("Correct! 🎉");
            score++;
        } else {
            System.out.println("Wrong answer!");
            System.out.println("Correct answer: Kotlin");
        }

        // Question 4
        System.out.println("\nQuestion 4:");
        System.out.println("What does CPU stand for?");
        System.out.println("1. Central Processing Unit");
        System.out.println("2. Computer Personal Unit");
        System.out.println("3. Central Program Utility");
        System.out.println("4. Control Processing User");

        System.out.print("Enter your answer: ");
        int answer4 = scanner.nextInt();

        if (answer4 == 1) {
            System.out.println("Correct! 🎉");
            score++;
        } else {
            System.out.println("Wrong answer!");
            System.out.println("Correct answer: Central Processing Unit");
        }

        // Question 5
        System.out.println("\nQuestion 5:");
        System.out.println("Which data type is used to store whole numbers in Java?");
        System.out.println("1. String");
        System.out.println("2. int");
        System.out.println("3. boolean");
        System.out.println("4. double");

        System.out.print("Enter your answer: ");
        int answer5 = scanner.nextInt();

        if (answer5 == 2) {
            System.out.println("Correct! 🎉");
            score++;
        } else {
            System.out.println("Wrong answer!");
            System.out.println("Correct answer: int");
        }

        // Final Result
        System.out.println("\n======================================");
        System.out.println("             QUIZ COMPLETED           ");
        System.out.println("======================================");

        System.out.println("Your score: " + score + "/5");

        if (score == 5) {
            System.out.println("Excellent! Perfect score! 🏆");
        } else if (score >= 3) {
            System.out.println("Good job! Keep learning! 👏");
        } else {
            System.out.println("Keep practicing! You can do better! 💪");
        }

        System.out.println("======================================");

        scanner.close();
    }
}
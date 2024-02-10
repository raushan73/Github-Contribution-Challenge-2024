// This program plays a Rock-Paper-Scissors game against the user.

public class RockPaperScissorsGame {

    public static void main(String[] args) {
        String[] options = {"Rock", "Paper", "Scissors"};
        Random random = new Random();

        // Bug: Missing import statement for Random class
        String computerChoice = options[random.nextInt(options.length)];

        String userChoice = JOptionPane.showInputDialog("Choose: Rock, Paper, or Scissors");

        // Bug: Incomplete logic for game rules (missing ties)
        if (userChoice.equals(computerChoice)) {```

package HarryPotterScoreboard;
// 20240810 SMW
// Show the scores of the 4 HP houses. Each score can be modified with buttons.
// The winner can be declared with a button.

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class HarryPotterScoreboard {
    // declare variables
    private JFrame frame;
    private JLabel gryffindorLabel, hufflepuffLabel, ravenclawLabel, slytherinLabel;
    private JButton upGryffindor, downGryffindor, upHufflepuff, downHufflepuff;
    private JButton upRavenclaw, downRavenclaw, upSlytherin, downSlytherin;
    private int gryffindorScore=170, hufflepuffScore=250, ravenclawScore=130, slytherinScore=140;

    private JLabel dummyLabel; // used to shift declareWinnerButton to the center
    private JButton declareWinnerButton;
    private JLabel dummyLabel2; // used to shift declareWinnerButton to the center

    public HarryPotterScoreboard(){
        // create GUI components here
        {
            frame = new JFrame("Harry Potter Scoreboard");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLayout(new GridLayout(5,4));
            frame.setSize(600, 400);
            frame.setLocationRelativeTo(null); // Center on screen
        }

        // create labels
        {
            gryffindorLabel = new JLabel("Gryffindor: " + gryffindorScore, SwingConstants.CENTER);
            hufflepuffLabel = new JLabel("Hufflepuff: " + hufflepuffScore, SwingConstants.CENTER);
            ravenclawLabel = new JLabel("Ravenclaw: " + ravenclawScore, SwingConstants.CENTER);
            slytherinLabel = new JLabel("Slytherin: " + slytherinScore, SwingConstants.CENTER);
            dummyLabel = new JLabel("");
            dummyLabel2 = new JLabel("");
        }

        // create buttons
        {
            upGryffindor = new JButton("+10");
            downGryffindor = new JButton("-10");
            upHufflepuff = new JButton("+10");
            downHufflepuff = new JButton("-10");
            upRavenclaw = new JButton("+10");
            downRavenclaw = new JButton("-10");
            upSlytherin = new JButton("+10");
            downSlytherin = new JButton("-10");
            declareWinnerButton = new JButton("Declare Winner");
        }

        // add components to the frame
        {
            frame.add(gryffindorLabel);
            frame.add(upGryffindor);
            frame.add(downGryffindor);

            frame.add(hufflepuffLabel);
            frame.add(upHufflepuff);
            frame.add(downHufflepuff);

            frame.add(ravenclawLabel);
            frame.add(upRavenclaw);
            frame.add(downRavenclaw);

            frame.add(slytherinLabel);
            frame.add(upSlytherin);
            frame.add(downSlytherin);

            frame.add(dummyLabel);
            frame.add(declareWinnerButton);
            frame.add(dummyLabel2);
        }

        // implement button actions
        {
            upGryffindor.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    gryffindorScore+=10;
                    gryffindorLabel.setText("Gryffindor: " + gryffindorScore);
                }
            });
            downGryffindor.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    gryffindorScore-=10;
                    gryffindorLabel.setText("Gryffindor: " + gryffindorScore);
                }
            });
            upHufflepuff.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    hufflepuffScore+=10;
                    hufflepuffLabel.setText("Hufflepuff: " + hufflepuffScore);
                }
            });
            downHufflepuff.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    hufflepuffScore-=10;
                    hufflepuffLabel.setText("Hufflepuff: " + hufflepuffScore);
                }
            });
            upRavenclaw.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    ravenclawScore+=10;
                    ravenclawLabel.setText("Ravenclaw: " + ravenclawScore);
                }
            });
            downRavenclaw.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    ravenclawScore-=10;
                    ravenclawLabel.setText("Ravenclaw: " + ravenclawScore);
                }
            });
            upSlytherin.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    slytherinScore+=10;
                    slytherinLabel.setText("Slytherin: " + slytherinScore);
                }
            });
            downSlytherin.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    slytherinScore-=10;
                    slytherinLabel.setText("Slytherin: " + slytherinScore);
                }
            });
            declareWinnerButton.addActionListener(new ActionListener(){
                @Override
                public void actionPerformed(ActionEvent e) {
                    declareWinner();
                }
            });
        }
    }

    private void declareWinner(){
        int maxScore = Math.max(gryffindorScore, Math.max(hufflepuffScore, Math.max(ravenclawScore, slytherinScore)));
        String winner = "";
        if (gryffindorScore == maxScore){ winner = "Gryffindor";}
        else if (hufflepuffScore == maxScore){ winner = "Hufflepuff";}
        else if (ravenclawScore == maxScore){ winner = "Ravenclaw";}
        else if (slytherinScore == maxScore){ winner = "Slytherin";}
        JOptionPane.showMessageDialog(frame, winner + " wins!");
    }
    
    // main
    public static void main(String args[]){
        HarryPotterScoreboard scoreboard = new HarryPotterScoreboard();
        scoreboard.frame.setVisible(true);
    }
}
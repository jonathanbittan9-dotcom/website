import java.util.Scanner;

import javax.sound.midi.SysexMessage;

import java.lang.Math;
public class physics {
    public static void main(String[] args) {    
        while (true){   
        Scanner scanner = new Scanner(System.in);
        System.out.println("this is a physics program");
        System.out.println("Do you want to calculate equations for a black hole? yes or no");
        String answer=scanner.next();
        if (answer.equals("yes")){
        System.out.println("Enter a mass of a black hole:");
        System.out.println("Data accepted: mass: we will calculate the Schwarzschild radius and then move on");
        Double massblackhole=scanner.nextDouble();
        Double G2 =  (6.67430e-11)*2;
        Double c = 300000.0 * 300000.0;
        Double radiusSchwarzschild = (massblackhole*G2) /c;
        System.out.println("The Schwarzschild radius is: " + radiusSchwarzschild + " kilometers"); 
        System.out.println("now: lets calculate the escape velocity of the black hole");
        Double escapevelocity= Math.sqrt((G2*massblackhole)/radiusSchwarzschild);
        System.out.println("The escape velocity is: " + escapevelocity + " kilometers per second");
        Double h = 6.62607015e-34;
        Double k = 1.380649e-23;
        Double pi = 3.14159;
        Double G = 6.67430e-11;
        Double c2 = Math.pow(c , 3);
        Double tempatureofblackhole = (h*c2)/ (8*pi*G*massblackhole*k);
        System.out.println("The tempature of the black hole is: " + tempatureofblackhole + " kelvins");
        continue;
    }
        else if(answer.equals("no")){
            System.out.println("the program support also calculations of newton rules and explanations");
            System.out.println("Do you want the explanations? of newton rules? yes or no");
            String answer2=scanner.next();
            if (answer2.equals("yes")){
                System.out.println("The first law is that object will move at the same speed unless a force acts upon it, and one straight line.");
                System.out.println("The second law is that force equals mass times acceleration, or F=ma.");
                System.out.println("The third law is that for every action there is an equal and opposite reaction.");
                System.out.println("Do you want to calculate newton equations? yes or no");
                System.out.println("now, do you want to calculate newton equations? yes or no");
                String answer3=scanner.next();
                if (answer3.equals("yes")){
                    System.out.println("what do you want to calculate? the first law, second law, or third law?");
                    
                    if (answer3.equals("first law")){
                        System.out.println("Enter a balanced power:");
                        Double balancedpower=scanner.nextDouble();
                        if(balancedpower == 0){
                            System.out.println("V=const");
                            System.out.println("it means that the object will move at a constant speed in a straight line");
                        }
                        else{
                            System.out.println("the object will not move in a straight line or at a constant speed");
                        }

                            
                        }
                        else if (answer3.equals("second law")){
                            System.out.println("Enter a mass, average speed and a time:");
                            Double mass=scanner.nextDouble();
                            Double averageacceleration=scanner.nextDouble();
                            Double time=scanner.nextDouble();
                            Double force = (time/averageacceleration)*mass;
                            System.out.println("The force is: " + force + " newtons");
                


                        }
                        else if (answer3.equals("third law")){
                            System.out.println("Enter an action force:");
                            Double actionforce=scanner.nextDouble();
                            System.out.println("The reaction force is: " + actionforce + " newtons");
                        }
                        else{
                            System.out.println("unknown response, restarting program");
                            
                        }
                    }
                    else if (answer3.equals("no")){
                        System.out.println("you can use the calculator if you want");
                        System.out.println("choose how many numbers you want to calculate:");
                        int n=scanner.nextInt();
                        for (int x=0; x==n+1; x++){
                            System.out.println("enter number " + (x+1) + ":");
                            float number=scanner.nextFloat();
                            float sum=0;
                            sum=sum+number;
                            System.out.println("the sum is: " + sum);

                        }

                        
                    }
                    else{
                        System.out.println("unknown response, restarting program");
                        
                    }
        }
        else{
            System.out.println("unknown response, reastarting program");
            
            
        }





    }
    }
}
}

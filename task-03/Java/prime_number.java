import java.util.Scanner;
public class main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: \n");
        int n = sc.nextInt();
                System.out.println("The prime numbers are:");
        
        for(int i = 2; i <= n; i++){
            int count = 0;
            for(int j = 2; j*j <= i; j++){
                if(i % j == 0){
                    count = 1;
                    break;
                }
            }
            if(count == 0){
            System.out.print(i + " ");
                
            }
        }
    }
}


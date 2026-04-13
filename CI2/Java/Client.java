import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class Client {
   public Client() {
   }

   public static void main(String[] var0) {
      try {
         Scanner var1 = new Scanner(System.in);
         System.out.print("Enter String 1: ");
         String var2 = var1.nextLine();
         System.out.print("Enter String 2: ");
         String var3 = var1.nextLine();
         Registry var4 = LocateRegistry.getRegistry("localhost", 5000);
         StringRemote var5 = (StringRemote)var4.lookup("StringService");
         String var6 = var5.concatenate(var2, var3);
         System.out.println("Concatenated Result: " + var6);
         var1.close();
      } catch (Exception var7) {
         System.out.println("Client Error: " + var7.getMessage());
      }

   }
}


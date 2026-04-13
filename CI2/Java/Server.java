import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
   public Server() {
   }

   public static void main(String[] var0) {
      try {
         StringRemoteImpl var1 = new StringRemoteImpl();
         Registry var2 = LocateRegistry.createRegistry(5000);
         var2.rebind("StringService", var1);
         System.out.println("Server is running and ready...");
      } catch (Exception var3) {
         System.out.println("Server Error: " + var3.getMessage());
      }

   }
}


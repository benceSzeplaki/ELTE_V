import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;

public class Bank {
    public static void main(String[] args) {
        int[] bigg = new int[]{Integer.MAX_VALUE};
        ExecutorService exec = Executors.newFixedThreadPool(10);
        for(int i = 0; i < 1_000_000_000; i++){
            exec.submit(() -> {
               bigg[0] -= ThreadLocalRandom.current().nextInt(10);
            });
        }
        exec.shutdown();
        try{
            exec.awaitTermination(10000, TimeUnit.MILLISECONDS);
        } catch (InterruptedException e){
            throw new RuntimeException(e);
        }
    }
}

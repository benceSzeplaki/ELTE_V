import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        /*Thread hello = new HelloThread();
        Thread world = new WorldThread();
        //hello.start();
        //world.start();

        Runnable helloImpl = new HelloThreadImplRunnable();
        Runnable worldImpl = new HelloThreadImplRunnable();
        Thread helloImplThread = new Thread(helloImpl);
        Thread worldImplThread = new Thread(worldImpl);
        //elloImplThread.start();
        //worldImplThread.start();


        Thread inLineWorldThread = new Thread(){
            @Override
            public void run() {
                System.out.println(" world!");
            }
        };
        //inLineWorldThread.start();

        Thread inLineHelloThread = new Thread(() -> System.out.println("LOL"));
        //inLineHelloThread.start();

        Thread inLineRunnableHelloThread = new Thread(new Runnable() {
            public void run(){
                System.out.println("Hello");
            }
        });
        //inLineRunnableHelloThread.start();

        Thread inLineRunnableWorldThread = new Thread(() -> System.out.println(" world!"));
        //inLineRunnableWorldThread.start();*/

        List<Double> list = new ArrayList<Double>();
        Thread firstThread = new Thread(() -> {
            for(int i = 0; i < 500000; i++) {
                synchronized(list){
                    list.add((double) Math.round(Math.random() * 100));
                }
            }
        });
        Thread secondThread = new Thread(() -> {
            for(int i = 0; i < 500000; i++) {
                synchronized(list){
                    list.add((double) Math.round(Math.random() * 100));
                }
            }
        });
        firstThread.start();
        secondThread.start();
        try {
            //Thread.sleep(100);
            firstThread.join();
            secondThread.join();
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }
        System.out.println(list.size());
        for(Double d : list){
            System.out.println(d);
        }
    }
}

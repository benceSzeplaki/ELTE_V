public class Main {
    public static void main(String[] args) {
        ThreadSafeMutableInteger i = new ThreadSafeMutableInteger(1);
        Thread threads[] = new Thread[10];
        final int[] counter = new int[10];
        for(int j = 0; j < 10; j++){
            final int jj = j;
            Thread t = new Thread(() -> {
                System.out.println(jj);
                counter[0]++;
                i.getAndAdd(jj);
            });
            t.start();
            threads[j] = t;
        }
    }
}

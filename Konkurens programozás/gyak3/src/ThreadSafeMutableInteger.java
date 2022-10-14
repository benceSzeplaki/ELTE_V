public class ThreadSafeMutableInteger {
    private int value;

    public ThreadSafeMutableInteger(int initValue){
        value = initValue;
    }
    public ThreadSafeMutableInteger(){
        value = 0;
    }
    public final synchronized int get(){
        return value;
    }
    public final synchronized void set(int newValue){
        value = newValue;
    }
    public final synchronized int getAndIncrement(){
        return value++;
    }
    public final synchronized int getAndDecrement(){
        return value--;
    }
    public final synchronized int getAndAdd(int v){
        int get = value;
        value += v;
        return get;
    }
    public final synchronized int incrementAndGet(){
        return ++value;
    }
    public final synchronized int decrementAndGet(){
        return ++value;
    }
    public final synchronized int addAndGet(int v){
        return value + v;
    }
}

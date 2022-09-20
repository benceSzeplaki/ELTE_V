import utils.Employee;
import utils.Manager;
import utils.SalariedEntity;
import utils.Subordinate;

import java.util.ArrayList;
import java.util.List;

public class Company {

    private String name;
    private final List<SalariedEntity> workers = new ArrayList<>();

    public Company(String name) {
        this.name = name;
    }

    public void addWorker(SalariedEntity worker){
        this.workers.add(worker);
    }

    public void removeWorker(SalariedEntity worker){
        int removeAtIndex = 0;
        for(int i = 0; i < workers.size(); i++) {
            if (worker.equals(workers.get(i))) {
                removeAtIndex = i;
            }
        }
        if(workers.get(removeAtIndex) instanceof Subordinate subordinate){
            for (SalariedEntity salariedEntity : workers) {
                if (salariedEntity instanceof Manager manager) {
                    salariedEntity.deleteEmployee(workers.get(removeAtIndex));
                }
            }
        }
        workers.remove(removeAtIndex);
    }

    public void giveRaiseToEmployees(Double percentage){
        for (SalariedEntity worker : workers) {
            if (worker instanceof Employee employee) {
                ((Employee) worker).setSalary(worker.getSalary() * (1 + percentage / 100));
            }
        }
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void workerList(){
        for (SalariedEntity worker : workers) {
           System.out.println(worker);
           System.out.println("-----------------------------------------------");
        }
    }
}

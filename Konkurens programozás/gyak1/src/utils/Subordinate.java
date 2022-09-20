package utils;

public class Subordinate extends Employee {

    public Subordinate(String name, Double salary) {
        super(name, salary);
    }

    @Override
    public Double getSalary() {
        return this.salary;
    }

    @Override
    public void deleteEmployee(SalariedEntity salariedEntity) {}
}

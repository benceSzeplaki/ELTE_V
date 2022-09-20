package utils;

import java.util.HashSet;

public class Manager extends Employee{

    private final HashSet<Employee> employees = new HashSet<>();

    public Manager(String name, Double salary) {
        super(name, salary);
    }

    @Override
    public Double getSalary() {
        Double employeeBonus = 0.0;
        for(Employee e : employees){
            employeeBonus += e.getSalary() * 0.05;
        }
        return this.salary + employeeBonus;
    }

    @Override
    public void deleteEmployee(SalariedEntity salariedEntity) {
        this.employees.remove(salariedEntity);
    }

    public void addEmployee(Employee employee){
        this.employees.add(employee);
    }

    public void deleteEmployee(Employee employee){
        this.employees.remove(employee);
    }

    @Override
    public String toString() {
        return "{" + System.lineSeparator() +
                "   \"name\": \"" + this.getName() + '\"' + ", " + System.lineSeparator() +
                "   \"salary\": " + this.getSalary() + ", " + System.lineSeparator() +
                "   \"employees\": [" + System.lineSeparator() + this.toStringEmployees() +
                "   ]" + System.lineSeparator() +
                '}';
    }

    private String toStringEmployees() {
        StringBuilder stringBuilder = new StringBuilder();
        for (Employee e : employees) {
            if(e.equals(this.getLastEmployee())) {
                stringBuilder.append(e.toStringForManager()).append(System.lineSeparator());
            } else {
                stringBuilder.append(e.toStringForManager()).append(',').append(System.lineSeparator());
            }
        }
        return stringBuilder.toString();
    }

    private Employee getLastEmployee() {
        Employee lastEmployee = new Subordinate("null",0.0);
        for (Employee x : this.employees){
            lastEmployee = x;
        }
        return lastEmployee;
    }
}

package utils;

public abstract class Employee implements SalariedEntity {
    protected String name;
    protected Double salary;

    protected Employee(String name, Double salary) {
        this.name = name;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public void giveRaise(Double percentage){
        this.salary = this.salary * (1 + percentage / 100);
    }

    @Override
    public String toString() {
        return "{" + System.lineSeparator() +
                "\"name\": \"" + name + '\"' + "," + System.lineSeparator() +
                "\"salary\": "+ salary + System.lineSeparator() +
                "}";
    }

    public String toStringForManager() {
        return "       { " + System.lineSeparator() +
                "           \"name\": \"" + name + '\"' + "," + System.lineSeparator() +
                "           \"salary\": "+ salary + System.lineSeparator() +
                "       }";
    }
}

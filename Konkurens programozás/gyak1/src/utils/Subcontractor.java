package utils;

public class Subcontractor implements SalariedEntity{

    private String name;
    private Long taxNumber;
    private Double salary;

    public Subcontractor(String name, long taxNumber, Double salary) {
        this.name = name;
        this.taxNumber = taxNumber;
        this.salary = salary;
    }

    @Override
    public Double getSalary() {
        return this.salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Long getTaxNumber() {
        return taxNumber;
    }

    public void setTaxNumber(Long taxNumber) {
        this.taxNumber = taxNumber;
    }

    @Override
    public void deleteEmployee(SalariedEntity salariedEntity) {

    }

    @Override
    public String toString() {
         return "{ " + System.lineSeparator() +
                "\"name\": \"" + name + '\"' + "," + System.lineSeparator() +
                "\"taxNumber:\": " + taxNumber + "," + System.lineSeparator() +
                "\"salary\": "+ salary + System.lineSeparator() +
                "}";
    }
}

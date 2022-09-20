import utils.Manager;
import utils.Subcontractor;
import utils.Subordinate;

public class Main {
    public static void main(String[] args) {
        String separationLine = "-----------------------------------------------";
        System.out.println(separationLine);
        System.out.println("Establishing company...");
        Company myFutureBigCompany = new Company("The Best Company Ever Ltd.");
        Manager boss = new Manager("Me", 3000.0);
        Subordinate subordinateOne = new Subordinate("John",1700.0);
        Subordinate subordinateTwo = new Subordinate("Bobby",1500.0);
        Subcontractor subcontractor = new Subcontractor("Mike", 8485481230L, 2000.0);
        boss.addEmployee(subordinateOne);
        boss.addEmployee(subordinateTwo);
        System.out.println(separationLine);

        System.out.println("Hiring workers...");
        myFutureBigCompany.addWorker(boss);
        myFutureBigCompany.addWorker(subordinateOne);
        myFutureBigCompany.addWorker(subordinateTwo);
        myFutureBigCompany.addWorker(subcontractor);

        System.out.println("Successfully hired:");
        myFutureBigCompany.workerList();

        System.out.println("The company is busy...");
        System.out.println("We did well this year! :)");
        System.out.println("Giving a raise to everyone...");
        myFutureBigCompany.giveRaiseToEmployees(20.0);
        myFutureBigCompany.workerList();

        System.out.println("The company is busy...");
        System.out.println("We didn't do well this year! :(");
        System.out.println("Firing employee for cutting down the budget...");
        myFutureBigCompany.removeWorker(subordinateTwo);
        myFutureBigCompany.workerList();
        System.out.println("Good bye, Bobby! :'( ");
        System.out.println("To be continued...");
    }
}

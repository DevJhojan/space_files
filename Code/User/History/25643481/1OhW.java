import Person;
public Class Employee:Person{
  private String ocupation;
  private double salary;
  private String type_of_contract;
  public Employee(String ocupation, double salary, String type_of_contract){
    super(names, last_names, age, gender, number_contact);
    this.ocupation = ocupation;
    this.salary = salary;
    this.type_of_contract = type_of_contract;
  }
  public getOcupation(){
    return this.ocupation;
  }
  public setOcupation(String ocupation){
    this.ocupation = ocupation;
  }
  public getSalary(){
    return this.salary;
  }
  public setSalary(double salary){
    this.salary = salary;
  }
  public getTypeOfContract(){
    return this.type_of_contract;
  }

  public setTypeOfContract(String type_of_contract){
    this.type_of_contract = type_of_contract;
  }

  public string toString(){
    return super(toString())+"\n"+
          "Ocupation:"+this.ocupation+"\n"+
          "Salary:"+this.salary+"\n"+
          "Type of contract:"+this.type_of_contract+"\n";
  }

}
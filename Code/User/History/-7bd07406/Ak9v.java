public Class Person{
  private String names;
  private String last_names;
  private int age;
  private char gender;
  private int number_contact;
  public Person(names, last_names, age, gender, number_contact){
    this.names = names;
    this.last_names = last_names;
    this.age = age;
    this.gender = gender;
    this.number_contact = number_contact;
  }

  public getNames(){
    return this.names;
  }
  public setNames(String names){
    this.names = names;
  }
  public getLastNames(){
    return this.last_names;
  }
  public setLastNames(String last_names){
    this.last_names = last_names;
  }
  public getAge(){
    return  this.age;
  }
  public setAge(int age){
    this.age =age;
  }
  public getGender(){
    return this.gender;
  }
  public setGender(char gender){
    this.gender = gender;
  }

  public getNumberContact(){
    return this.number_contact;
  }
  public setNumberContact(int number_contact){
    this.number_contact = number_contact;
  }
  public String toString(){
    return "Names:"+this.names+"\n"+
          "Last Names:"+this.last_names+"\n"+
          "Age:" +this.Age+"\n"+
          "Gender:"+this.gender+"\n"+
          "Number Contact:"+this.number_contact+"\n";
  }
}
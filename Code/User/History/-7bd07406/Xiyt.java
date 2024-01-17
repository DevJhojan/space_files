public Class Person{
  private String names;
  private String lastnames;
  private int age;
  private char gender;
  private int numbercontact;
  public Person(names, lastnames, age, gender, numbercontact){
    this.names = names;
    this.lastnames = lastnames;
    this.age = age;
    this.gender = gender;
    this.numbercontact = numbercontact;
  }

  public getNames(){
    return this.names;
  }
  public setNames(String names){
    this.names = names;
  }
  public getLastNames(){
    return this.lastnames;
  }
  public setLastNames(String lastnames){
    this.lastnames = lastnames;
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
    return this.numbercontact;
  }

  public setNumberContact(int numbercontact){
    this.numbercontact = numbercontact;
  }
  public String toString(){
    return "Names:"+this.names+"\n"+
          "Last Names:"+this.lastnames+"\n"+
          "Age:" +this.age+"\n"+
          "Gender:"+this.gender+"\n"+
          "Number Contact:"+this.numbercontact+"\n";
  }
}
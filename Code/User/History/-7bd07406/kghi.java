public Class Person{
  private String _names;
  private String _last_names;
  private int _age;
  private char _gender;
  private int number_contact;
  public Person(names, last_names, age, gender, number_contact){
    this._names = names;
    this._last_names = last_names;
    this.age = age;
    this._gender = gender;
    this.number_contact = number_contact;
  }

  public getNames(){
    return this._names;
  }
  public setNames(String names){
    this._names = names;
  }
  public getLastNames(){
    return this._last_names;
  }
  public setLastNames(String last_names){
    this._last_names = last_names;
  }
  public getAge(){
    return  this._age;
  }
  public setAge(int age){
    this._age =age;
  }
  public getGender(){
    return this._gender;
  }
  public setGender(char gender){
    this._gender = gender;
  }

  public getNumberContact(){
    return this.number_contact;
  }

  public setNumberContact(int number_contact){
    this.number_contact = number_contact;
  }
  public String toString(){
    return "Names:"+this._names+"\n"+
          "Last Names:"+this._last_names+"\n"+
          "Age:" +this._age+"\n"+
          "Gender:"+this._gender+"\n"+
          "Number Contact:"+this.number_contact+"\n";
  }
}
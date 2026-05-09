- Encapsulation is the bundling of data (variables) and methods (functions) that operate on the data into a single unit or class. 

- Abstraction involves hiding the complex implementation details and showing only the essential features of the object.

Ex. 

const myCar = new Car('Toyota', 'Camry');
console.log(myCar.startEngine()); // Toyota Camry engine started.
console.log(myCar.drive()); // Toyota Camry is driving.

- Polymorphism allows objects of different classes to be treated as objects of a common super class. 
It is often achieved through method overriding,
where a subclass provides a specific implementation of a method that is already defined in its superclass.

```
class Animal {
  speak() {
    console.log('Animal makes a sound');
  }
}

class Dog extends Animal {
  speak() {
    console.log('Dog barks');
  }
}

class Cat extends Animal {
  speak() {
    console.log('Cat meows');
  }
}

const animals = [new Animal(), new Dog(), new Cat()];
animals.forEach(animal => animal.speak());
// Output:
// Animal makes a sound
// Dog barks
// Cat meows
```

- Inheritance allows a class (child class) to inherit properties and methods from
another class (parent class). This promotes code reusability.

```
class Vehicle {
  constructor(brand) {
    this.brand = brand;
  }

  start() {
    return `${this.brand} vehicle started.`;
  }
}

class Car extends Vehicle {
  constructor(brand, model) {
    super(brand);
    this.model = model;
  }

  start() {
    return `${this.brand} ${this.model} car started.`;
  }
}

const myCar = new Car('Toyota', 'Camry');
console.log(myCar.start()); // Toyota Camry car started.
```
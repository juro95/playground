// example of nominal typing

class Animal {
  constructor(public name: string) {}
}

class Cat extends Animal {
  meow() {
    console.log("meow");
  }
}

class Dog extends Animal {
  bark() {
    console.log("bark");
  }
}

function makeAnimalSound(animal: Animal) {
  if (animal instanceof Cat) {
    animal.meow();
  } else if (animal instanceof Dog) {
    animal.bark();
  }
}

const cat = new Cat("Fluffy");
const dog = new Dog("Fido");

makeAnimalSound(cat);
makeAnimalSound(dog);

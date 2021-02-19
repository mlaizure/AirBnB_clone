# AirBnB clone - The Console
- Creating command interpreter to manage objects for the AirBnB clone
- Has a parent class (`BaseModel`) for initialization and json serialization and deserialization of class instances
- Stores and reloads json string representation from file using abstracted storage engine `FileStorage`
- Creates all classes for future AirBnB projects (all inherit from `BaseModel`)
  - `User`
  - `State`
  - `City`
  - `Amenity`
  - `Place`
  - `Review`
- Unittests to validate all classes including storage engine

## Command interpreter
- How to start:
  - clone repository
  - run ./console.py from the repo's base directory
- How to use:
  - quit or Ctrl + D to exit console
  - help: see valid commands and documentation
  - create: creates a new instance of a class (`$ create BaseModel`)
  - show: prints stringified instance of a class (`$ show BaseModel 123`)
  - destroy: deletes an instance (`$ destroy BaseModel 123`)
  - all: prints strings of all instances (or all instances of a certain class) in JSON file (`$ all` or `$ all BaseModel`)
  - update: updates an instance attribute (`$ update BaseModel 123 attribute "value"`)
- Examples:
```
$ ./console.py
(hbnb) create User
f7479d71-40a2-4ba0-97c1-cc9dc2ea8a35
(hbnb) show User f7479d71-40a2-4ba0-97c1-cc9dc2ea8a35
[User] (f7479d71-40a2-4ba0-97c1-cc9dc2ea8a35) {'updated_at': datetime.datetime(2021, 2, 16, 21, 37, 23, 544315), 'created_at': datetime.datetime(2021, 2, 16, 21, 37, 23, 544257), 'id': 'f7479d71-40a2-4ba0-97c1-cc9dc2ea8a35'}
(hbnb) update User f7479d71-40a2-4ba0-97c1-cc9dc2ea8a35 first_name "Betty"
(hbnb) all
["[User] (f7479d71-40a2-4ba0-97c1-cc9dc2ea8a35) {'first_name': 'Betty', 'updated_at': datetime.datetime(2021, 2, 16, 21, 39, 54, 28478), 'created_at': datetime.datetime(2021, 2, 16, 21, 37, 23, 544257), 'id': 'f7479d71-40a2-4ba0-97c1-cc9dc2ea8a35'}"]
(hbnb) destroy User f7479d71-40a2-4ba0-97c1-cc9dc2ea8a35
(hbnb) all
[]
(hbnb) quit
$
```

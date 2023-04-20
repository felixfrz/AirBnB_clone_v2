<center> <h1>AirBnB - The Console V2</h1> </center>

<center> <h3>This repo was forked from https://github.com/justinmajetich/AirBnB_clone and modified to include MySQL</h3> </center>

This repository contains the initial stage of the project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization and MySQL database, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks                                | Files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                           |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| 0. Fork me if you can!               | [AUTHORS](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/AUTHORS)                                                                                                                                                                                                                                                                                                                                                                                                                                   | Fork repo and edit code                                               |
| 1. Bug free!                         | [/tests](https://github.com/felixfrz/AirBnB_clone_v2/tree/master/tests)                                                                                                                                                                                                                                                                                                                                                                                                                                      | Uses Unittests to test for bugs in all files                          |
| 2. Console improvements              | [console.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/console.py)                                                                                                                                                                                                                                                                                                                                                                                                                             | Upgrades functions in the Console                                     |
| 3. MySQL setup development           | [setup_mysql_dev.sql](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql)                                                                                                                                                                                                                                                                                                                                                                                                           | Prepares a MySQL database for project                                 |
| 4. MySQL setup test                  | [setup_mysql_test.sql](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/setup_mysql_test.sql)                                                                                                                                                                                                                                                                                                                                                                                                         | Tests MySQL database                                                  |
| 5. Delete object                     | [/models/engine/file_storage.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/engine/file_storage.py)                                                                                                                                                                                                                                                                                                                                                                                      | Updates File Storage and creates new instance method                  |
| 6. DBStorage - States and Cities     | [models/base_model.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/base_model.py) [models/city.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/city.py) [models/state.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/state.py) [models/engine/db_storage.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/engine/db_storage.py) [models/**init**.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/__init__.py) | Modify models to make them inherit from BaseModel and access database |
| 7. DBStorage - User                  | [models/user.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/user.py)                                                                                                                                                                                                                                                                                                                                                                                                                     | Update the User model to inherit from BaseModel                       |
| 8. DBStorage - Place                 | [models/place.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/place.py) [models/user.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/user.py) [models/city.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/city.py)                                                                                                                                                                                                                                 | Update Place to inherit from BaseModel and backref other models       |
| 9. DBStorage - Review                | [models/review.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/review.py) [/models/user.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/user.py) [/models/place.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/place.py)                                                                                                                                                                                                                           | Update Review to inherit from BaseModel and backref other models      |
| 10. DBStorage - Amenity... and BOOM! | [models/amenity.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/amenity.py) [/models/place.py](https://github.com/felixfrz/AirBnB_clone_v2/blob/master/models/place.py)                                                                                                                                                                                                                                                                                                                   | Update model Amenities (many to many relationship)                    |

<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

2. Once the repository is cloned locate the "console.py" file and run it as follows:

```
/AirBnB_clone_v2$ ./console.py
```

4. When this command is run the following prompt should appear:

```
(hbnb)
```

5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands

    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

##### Alternative Syntax

Users are able to issue a number of console command using an alternative syntax:

    Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])

Advanced syntax is implemented for the following commands:

    * all - Shows all objects the program has access to, or all objects of a given class

    * count - Return number of object instances by class

    * show - Shows an object based on class and UUID

    * destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object

Usage: create <class_name>

```
(hbnb) create BaseModel
```

```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)
```

###### Example 1: Show an object

Usage: show <class_name> <\_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959),
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)
```

###### Example 2: Destroy an object

Usage: destroy <class_name> <\_id>

```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)
```

###### Example 3: Update an object

Usage: update <class_name> <\_id>

```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889),
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```

<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects

Usage: <class_name>.all()

```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User

Usage: <class_name>.destroy(<\_id>)

```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 2: Update User (by attribute)

Usage: <class_name>.update(<\_id>, <attribute_name>, <attribute_value>)

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 3: Update User (by dictionary)

Usage: <class_name>.update(<\_id>, <dictionary>)

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

<br>

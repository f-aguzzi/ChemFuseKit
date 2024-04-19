#UML

A **use case diagram** is a graphical depiction of a user's possible interactions with a system. 

A use case diagram shows various use cases and different types of users the system has and will often be accompanied by other types of diagrams as well. The use cases are represented by ellipses. The actors are shown as stick figures.

```plantuml
:All Users:      as allUsers
:Main Admin:     as Admin

Admin   -up-|>    allUsers: manages

rectangle System {
	(Manage Users) -up-|> (Management)
	(Management) ..> (Manage users): <<include>>
	Admin -right-|> (Manage Users)
	allUsers --> (Use system)
}
```

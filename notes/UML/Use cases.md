Probably incomplete and maybe wrong.

```plantuml
rectangle "Graphical Application" {
	(Learn chemiometry)
	(Classify crime scene data)
	(Perform data fusion)
	(Import and export data)
	(Make graphs)
}

rectangle "Python Library" {
	(Use library from Colab)
}

(Add new functionality)

"Student" --> (Learn chemiometry)
"Forensic Analyst" --> (Classify crime scene data)
"Anyone" --> (Perform data fusion)
"Anyone" --> (Import and export data)
"Anyone" --> (Make graphs)
"Google Colab User" --> (Use library from Colab)
"System manager" -up-> (Add new functionality)

"Graphical Application" ..|> "Python Library" : <<uses>>

(Use library from Colab) --> (Use Python library)
(Add new functionality) -up-|> "Graphical Application"
(Add new functionality) -up-|> "Python Library"
```


 ```plantuml

!define UML_LOOK "TB"

actor User
participant WebApp
participant WebServer
participant ChemiometryLibrary

User -> WebApp : Upload training tables
User -> WebApp : Set parameters
User -> WebApp : (optional) Upload model


WebApp -> WebServer : Pass training tables and/or model
WebApp -> WebServer : Load configuration

WebServer -> ChemiometryLibrary  : Pass preprocessed tables
ChemiometryLibrary --> WebApp : Fused tables


WebApp -> WebServer : Run training
WebServer -> ChemiometryLibrary : Execute training
ChemiometryLibrary --> WebServer : Training finished


User -> WebApp : Upload data to classify
WebApp -> WebServer : Pass data to classify
WebServer -> ChemiometryLibrary: Run classification
ChemiometryLibrary --> WebApp : Fused tables, classification results, graphs

WebApp --> User : Download processed data
```

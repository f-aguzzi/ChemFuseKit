

```plantuml


node Client {
	portin ReceiveArtifacts

	[Web App] -( RestAPI

	portout SendCommandsData

	RestAPI - SendCommandsData
}

"User\nInput" -- [Web App]

node Server {
	portin ReceiveCommandsData

	() "RestAPI" as RA
	
	ReceiveCommandsData -( RA

	RA - [Django Server]

	[Django Server] -( CommonAPI
	CommonAPI - [Chemiometry Library]

	portout SendArtifacts
}

SendCommandsData --> ReceiveCommandsData

SendArtifacts --> ReceiveArtifacts
```



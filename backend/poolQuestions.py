# Final Project: Quiz Application with Microservices
# Date: 28-Nov-2022
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
#          A01751587 Paulo Ogando Gulias
#          A01745865 José Ángel García Gómez
#          A01745419 José Luis Madrigal Sánchez

items = [
    {
        "id": {"N": "0"},
        "Sentence": {"S": "What design pattern lets you fit more objects into the available amount of RAM"},
        "CorrectAnswer": {"S": "Flyweight"},
        "Choices": {"L": [{"S": "Observer"}, {"S": "Flyweight"}, {"S": "Decortaro"}, {"S": "Builder"}]},
        "Image": {"S": "0.jpg"},
    },
    {
        "id": {"N": "1"},
        "Sentence": {"S": "A thick client..."},
        "CorrectAnswer": {"S": "holds business logic"},
        "Choices": {"L": [{"S": "holds the user interface of the application"}, {"S": "can grow horizontally"}, {"S": "can grow vertically"}, {"S": "holds business logic"}]},
        "Image": {"S": "1.jpg"},
    },
    {
        "id": {"N": "2"},
        "Sentence": {"S": "Clients shouldn’t be forced to depend on methods they do not use."},
        "CorrectAnswer": {"S": "Interface Segregation Principle"},
        "Choices": {"L": [{"S": "Interface Segregation Principle"}, {"S": "Dependency Inversion Principle"}, {"S": "Open/Closed Principle"}, {"S": "Single Responsibility Principle"}]},
        "Image": {"S": "2.jpg"},
    },
    {
        "id": {"N": "3"},
        "Sentence": {"S": "Which of the following is NOT a load balancing approach"},
        "CorrectAnswer": {"S": "Application load balancing"},
        "Choices": {"L": [{"S": "DNS load balancing"}, {"S": "Hardware load balancing"}, {"S": "Application load balancing"}, {"S": "Software load balancing"}]},
        "Image": {"S": "3.jpg"},
    },
    {
        "id": {"N": "4"},
        "Sentence": {"S": "Distribute heavy traffic load across the servers running in the cluster"},
        "CorrectAnswer": {"S": "Load Balancers"},
        "Choices": {"L": [{"S": "NAT Gateway"}, {"S": "Load Balancers"}, {"S": "On the cloud cluster manager"}, {"S": "Sharding"}]},
        "Image": {"S": "4.jpg"},
    },
    {
        "id": {"N": "5"},
        "Sentence": {"S": "What do you do to increasing reliability of a particular system?"},
        "CorrectAnswer": {"S": "Duplication of critical components or functions of a system"},
        "Choices": {"L": [{"S": "Establish SLA (Service Level Agreements"}, {"S": "Distribute workloads across Regions"}, {"S": "Use a CDN to deploy servers across the globe"}, {"S": "Duplication of critical components or functions of a system"}]},
        "Image": {"S": "5.jpg"},
    },
    {
        "id": {"N": "6"},
        "Sentence": {"S": "It refers to the number of data packets being successfully sent per second"},
        "CorrectAnswer": {"S": "Throughput"},
        "Choices": {"L": [{"S": "Throughput "}, {"S": "Bandwidth"}, {"S": "Redis"}, {"S": "Latency"}]},
        "Image": {"S": "6.jpg"},
    },
    {
        "id": {"N": "7"},
        "Sentence": {"S": "Type of diagram that show the objects in the modeled system"},
        "CorrectAnswer": {"S": "Structural diagram"},
        "Choices": {"L": [{"S": "Behavioral diagram"}, {"S": "Conceptual diagram"}, {"S": "Structural diagram"}, {"S": "Synoptic diagram"}]},
        "Image": {"S": "7.jpg"}
    },
    {
        "id": {"N": "8"},
        "Sentence": {"S": "It briefly describes both the problem and the solution of a pattern"},
        "CorrectAnswer": {"S": "Intent"},
        "Choices": {"L": [{"S": "Motivation"}, {"S": "Intent"}, {"S": "Structure"}, {"S": "Code example"}]},
        "Image": {"S": "8.jpg"}
    },
    {
        "id": {"N": "9"},
        "Sentence": {"S": "Type of patterns that provide object creation mechanisms that increase flexibility and reuse of existing code"},
        "CorrectAnswer": {"S": "Creational patterns"},
        "Choices": {"L": [{"S": "Creational patterns"}, {"S": "Behavorial patterns"}, {"S": "Structural patterns"}, {"S": "Code patterns"}]},
        "Image": {"S": "9.jpg"}
    },
    {
        "id": {"N": "10"},
        "Sentence": {"S": "It is the design pattern that is also known as Wrapper"},
        "CorrectAnswer": {"S": "Adapter"},
        "Choices": {"L": [{"S": "Builder"}, {"S": "Decorator"}, {"S": "Adapter"}, {"S": "Singleton"}]},
        "Image": {"S": "10.jpg"}
    },
    {
        "id": {"N": "11"},
        "Sentence": {"S": "It is the design pattern that lets you construct complex objects step by step"},
        "CorrectAnswer": {"S": "Builder"},
        "Choices": {"L": [{"S": "Builder"}, {"S": "Flyweight"}, {"S": "Monolith"}, {"S": "Singleton"}]},
        "Image": {"S": "11.jpg"}
    },
    {
        "id": {"N": "12"},
        "Sentence": {"S": "It refers to the application's ability to handle and withstand increased workload, so it can be maintaining performance"},
        "CorrectAnswer": {"S": "Scalability"},
        "Choices": {"L": [{"S": "Bandwidth"}, {"S": "Scalability"}, {"S": "Network capacity"}, {"S": "Adaptability"}]},
        "Image": {"S": "12.jpg"}
    },
    {
        "id": {"N": "13"},
        "Sentence": {"S": "It is a network of interconnected servers that speeds up webpage loading for data-heavy applications"},
        "CorrectAnswer": {"S": "Content Distribution Network"},
        "Choices": {"L": [{"S": "Organized Network"}, {"S": "Content Distribution Network"}, {"S": "Data Optimized Network"}, {"S": "Scalable Network"}]},
        "Image": {"S": "13.jpg"}
    },
    {
        "id": {"N": "14"},
        "Sentence": {"S": "Which type of scaling means adding more power to our server?"},
        "CorrectAnswer": {"S": "Vertical Scaling"},
        "Choices": {"L": [{"S": "Vertical Scaling"}, {"S": "Horizontal Scaling"}, {"S": "Synchronized Scaling"}, {"S": "Diagonal Scaling"}]},
        "Image": {"S": "14.jpg"}
    },
    {
        "id": {"N": "15"},
        "Sentence": {"S": "This is not a type of testing"},
        "CorrectAnswer": {"S": "Post Commit Hooks"},
        "Choices": {"L": [{"S": "Chaos Engineering"}, {"S": "A/B"}, {"S": "Post Commit Hooks"}, {"S": "Pre Commit Hooks"}]},
        "Image": {"S": "15.jpg"}
    },
    {
        "id": {"N": "16"},
        "Sentence": {"S": "¿When does a model is considered smart?"},
        "CorrectAnswer": {"S": "All of them"},
        "Choices": {"L": [{"S": "Contains all the data validation/business rules/logic"}, {"S": "All of them"}, {"S": "Handles the state of the application"}, {"S": "Does not depend on the UI"}]},
        "Image": {"S": "16.jpg"}
    },
    {
        "id": {"N": "17"},
        "Sentence": {"S": "¿When does a model is considered thin?"},
        "CorrectAnswer": {"S": "Updates the view when the model changes"},
        "Choices": {"L": [{"S": "When it wheights less than 10MB"}, {"S": "When it is hosted on a separated instance from the view"}, {"S": "When it updates the view when the model changes"}, {"S": "When you can reuse it for different views"}]},
        "Image": {"S": "17.jpg"}
    },
    {
        "id": {"N": "18"},
        "Sentence": {"S": "¿When does a view is considered dumb?"},
        "CorrectAnswer": {"S": "All of them"},
        "Choices": {"L": [{"S": "Does only minimal processing, usually provided by a template language"}, {"S": "Does not store any data"}, {"S": "Does not access the application data directly"}, {"S": "All of them"}]},
        "Image": {"S": "18.jpg"}
    },
    {
        "id": {"N": "19"},
        "Sentence": {"S": "An Application is Serverless when..."},
        "CorrectAnswer": {"S": "You write functions instead of deployments"},
        "Choices": {"L": [{"S": "You make constant deployments"}, {"S": "The application is running on several instances"}, {"S": "You write functions instead of deployments"}, {"S": "All of them"}]},
        "Image": {"S": "19.jpg"}
    },
    {
        "id": {"N": "20"},
        "Sentence": {"S": "This is a con of making serverless application"},
        "CorrectAnswer": {"S": "Gain flexibility and ease of use at the expense of control"},
        "Choices": {"L": [{"S": "No servers to manage"}, {"S": "Pay per invocation"}, {"S": "Service integrations"}, {"S": "Gain flexibility and ease of use at the expense of control"}]},
        "Image": {"S": "20.jpg"}
    },
    {
        "id": {"N": "21"},
        "Sentence": {"S": "What is the purpose of the Singleton pattern?"},
        "CorrectAnswer": {"S": "To ensure that a class has only one instance and provides a global point of access to it"},
        "Choices": {"L": [{"S": "To provide a way to create objects without specifying their exact class"}, {"S": "To decouple an abstraction from its implementation"}, {"S": "To ensure that a class has only one instance and provides a global point of access to it"}, {"S": "To provide a way to encapsulate a group of individual factories that have a common theme"}]},
        "Image": {"S": "21.jpg"}
    },
    {
        "id": {"N": "22"},
        "Sentence": {"S": "What is the purpose of the Observer pattern?"},
        "CorrectAnswer": {"S": "To decouple an object from its dependent objects so that changes to one object do not require changes to other dependent objects"},
        "Choices": {"L": [{"S": "To provide a way to encapsulate a group of individual factories that have a common theme"}, {"S": "To provide a way to create objects without specifying their exact class"}, {"S": "To decouple an object from its dependent objects so that changes to one object do not require changes to other dependent objects"}, {"S": "To provide a way to ensure that a class has only one instance and provides a global point of access to it"}]},
        "Image": {"S": "22.jpg"}
    },
    {
        "id": {"N": "23"},
        "Sentence": {"S": "What is the purpose of the Builder pattern?"},
        "CorrectAnswer": {"S": "To provide a way to separate the construction of a complex object from its representation"},
        "Choices": {"L": [{"S": "To provide a way to create objects without specifying their exact class"}, {"S": "To provide a way to encapsulate a group of individual factories that have a common theme"}, {"S": "To provide a way to decouple an abstraction from its implementation"}, {"S": "To provide a way to separate the construction of a complex object from its representation"}]},
        "Image": {"S": "23.jpg"}
    },
    {
        "id": {"N": "24"},
        "Sentence": {"S": "What is a federated architecture?"},
        "CorrectAnswer": {"S": "An architecture where multiple independent components or systems are integrated to form a larger system"},
        "Choices": {"L": [{"S": "An architecture where all components are centrally managed and controlled"}, {"S": "An architecture where multiple independent components or systems are integrated to form a larger system"}, {"S": "An architecture where all components are designed to work independently and do not communicate with each other"}, {"S": "An architecture where all components are designed to share a common database schema"}]},
        "Image": {"S": "24.jpg"}
    },
    {
        "id": {"N": "25"},
        "Sentence": {"S": "What are some benefits of using a federated architecture?"},
        "CorrectAnswer": {"S": "It allows for easier maintenance and scalability of the system"},
        "Choices": {"L": [{"S": "It allows for easier maintenance and scalability of the system"}, {"S": "It ensures that all components are tightly coupled and communicate with each other"}, {"S": "It reduces the need for data replication and synchronization"}, {"S": "It increases the overall complexity of the system and makes it harder to manage and maintain"}]},
        "Image": {"S": "25.jpg"},
    },
    {
        "id": {"N": "26"},
        "Sentence": {"S": "What is the purpose of a load balancer in a client-server web architecture?"},
        "CorrectAnswer": {"S": "It distributes incoming traffic across multiple servers to improve performance and reliability"},
        "Choices": {"L": [{"S": "It distributes incoming traffic across multiple servers to improve performance and reliability"}, {"S": "It stores and manages data for the server, reducing the load on server-side resources"}, {"S": "It provides a way for clients to authenticate themselves to the server and access protected resources"}, {"S": "It enables servers to communicate with each other and coordinate their processing."}]},
        "Image": {"S": "26.jpg"},
    },
    {
        "id": {"N": "27"},
        "Sentence": {"S": "What is the purpose of the MVC (Model-View-Controller) pattern?"},
        "CorrectAnswer": {"S": "To separate the application logic into three main components to facilitate development and maintainability"},
        "Choices": {"L": [{"S": "To create an attractive and user-friendly interface"}, {"S": "To enable communication between different systems in a distributed architecture"}, {"S": "To organize data in a relational database"}, {"S": "To separate the application logic into three main components to facilitate development and maintainability"}]},
        "Image": {"S": "27.jpg"}
    },
    {
        "id": {"N": "28"},
        "Sentence": {"S": "What is horizontal scalability in the context of server infrastructure?"},
        "CorrectAnswer": {"S": "Adding more servers to the system to handle a larger volume of traffic or workload"},
        "Choices": {"L": [{"S": "Increasing the processing capacity of an existing server"}, {"S": "Adding more servers to the system to handle a larger volume of traffic or workload"}, {"S": "Optimizing the performance of a server using specific technologies"}, {"S": "Redesigning the system architecture to improve efficiency"}]},
        "Image": {"S": "28.jpg"}
    }, 
    {
        "id": {"N": "29"},
        "Sentence": {"S": "What is the difference between a RESTful web service and a SOAP web service?"},
        "CorrectAnswer": {"S": "RESTful uses HTTP protocols and is lighter and more flexible, while SOAP uses XML and is more rigid and complex"},
        "Choices": {"L": [{"S": "RESTful uses HTTP protocols and is lighter and more flexible, while SOAP uses XML and is more rigid and complex"}, {"S": "RESTful is more suitable for mobile applications, while SOAP is more suitable for desktop applications"}, {"S": "RESTful only supports GET and POST operations, while SOAP supports more complex operations"}, {"S": "RESTful is an older standard than SOAP"}]},
        "Image": {"S": "29.jpg"}
    },
    {
        "id": {"N": "30"},
        "Sentence": {"S": "What is the purpose of the serverless architecture?"},
        "CorrectAnswer": {"S": "To write functions instead of server implementations to facilitate development and scalability"},
        "Choices": {"L": [{"S": "To eliminate the need for servers and rely solely on client-side processing"}, {"S": "To centralize all components and resources in a single server"}, {"S": "To provide a flexible and scalable environment for deploying microservices"}, {"S": "To write functions instead of server implementations to facilitate development and scalability"}]},
        "Image": {"S": "30.jpg"}
    }
]

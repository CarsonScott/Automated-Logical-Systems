# Automated Logical Systems

The following is a description of a multi-agent system for distributed constraint satisfaction. Agents send and receive messages between one another, executing them recursively in order to change and update their knowledge of the environment. Agents collectively act as a distributed knowledge system, developing and progressing by way of delegating tasks through messages. 

## 1. Objects and Storage

A data store has a capacity which limits the amount of information that it can hold. When the capacity of a store is met, the contents are mapped by a function M(S) to another structure called an object. The store is then free to hold new new information as the previous content has been moved to the object. Objects can take on various roles depending on the type of information dealt to them, for instance they can be used to represent a pattern, where the map function removes all but a certain set of features from the content of a store.

Objects can add connections between elements to represent their relationships, such as sequential order or cause-and-effect. The main idea is that objects take some fuzzy or ill-defined aspect and explicitly state it as either true or false in the form of a proposition. This gives rise to a logical representation that relies on rules, making it effective for high-level reasoning with heuristics due to the fact that it reconstructs incomplete information as a collection of well-defined truths. Unobserved aspects can then be assumed from observed information, based on rules learned over time from previous experiences with similar observations.

## 2. Logic and Rules

Objects can contain other objects, and be linked together in vast networks. Logic is built up by chains of objects, each with propositional definitions regarding rules and facts about certain bits of information. For instance, a correlation between one event can be used to predict another, even if their relationship is not causal. It doesn’t matter whether one event directly induces another as long as the occurrence of the first tends to be followed by the occurrence of the second. If the assumption that “A causes B” allows for correct predictions to be made regarding B most of the time, then as a rule it is effective and should be assumed in the future.

Rules about rules can be used to define exceptions, or instances where a given rule should not be taken as true. Too many exceptions can cause a rule to dissolve, meaning the object that defines the rule is broken down and recycled. This is effective in minimizing the errors brought about from bad assumptions, but it is also an efficient mechanism of data handling. Harmful and Irrelevant data is replaced by potentially useful information, yielding a system of applicable knowledge over time.

## 3. Creation and Purpose

A function is selected from a list of maps and used to transform a given bit of information into a new object, which is pulled from a collection of empty objects called a warehouse and initialized by the selected map. When objects are dissolved, the content and structure are removed and the empty object is placed back into the warehouse for future use. Objects remain active for as long as necessary and dissolve when their intended use is fulfilled, or until they’re deemed no longer useful or relevant.

Certain objects define rules for creating new objects or dissolving old ones, including the selection of map functions and the intended purpose of a created object. A system of objects begins with a single store called the input store and a single rule for creating new objects. A set of base functions map the inputs to new objects, which build up the first-order level of the system.

## 4. Networks and Statements

Rules defining the creation of objects can be chained together, effectively remapping a given object sequentially to form a more complex object. The chain of rules defining such a process is considered a map in and of itself. An equivalent concept in mathematics is function composition, where multiple functions are included in a larger, more complex function. When new objects are formed, they are compiled into a store. This leads to recursive creation of objects from lower-level stores, forming a hierarchical object Network. Objects are linked through special objects called connectives. Connectives are units of logic which form the base elements of a propositional statement.

## 5. Truth and Conditions

Objects can take a bit of information and pass it along connectives that holds true, providing another object with the same information who can then send it further into the network. Data propagates through the medium of true propositions, where a certain connective will allow the transference of information if and only if it satisfies some proposition. Therefore a given bit of data will only travel through a network if it meets the logical requirements of said network, providing an essential structure for testing information against a set of propositional statements to determine whether certain conditions hold true.

## 6. Agents and Knowledge

An agent is an object that interprets a set of statements. Agents act like computer programs, with a scope equal to the elements stored within the agent called its knowledge. Agents can contain other agents and execute recursively, calling each individual sequentially who in turn either executes another set of agents or, in the case of base agents (lowest agents in a hierarchy), a set of statements.

## 7. Society and Communication

Agents are connected in two ways, either hierarchically as described above or in a network where no individual is explicitly dominant to any other. Networks allow agents to send and receive information, forming a system of distributed knowledge. Each individual can make requests and provide information to its neighbors, or a subset of agents to which one is connected via communication lines, which act as vehicles for messages between agents.

## 8. Beliefs and Messages

Messages are statements that are sent by an agent and received by its neighbors, who have the ability to either accept or deny the message which determines whether the statement is executed. By accepting a given message, the receiver allows the sender to manipulate some aspect of their memory, whether it be a request for some specific knowledge or a command that causes change to that which is known by the receiver. Together a system collectively constructs knowledge that is known by its members. Information that is perceived as true is established through interactions between agents who then conform to a stable set of concepts.

## 9. Culture and Conformity

Messages that do not reflect or even violate the ideals of a system are more likely to be rejected, as receiving agents do not belief what is said to be true. The beliefs of a system are therefore resistant to change, slowing the development of knowledge that is not pre-established as the system moves forward in time. However, subtle difference between members in what is accepted cause the development of knowledge over time, albeit gradually. This leads to cultural trends that spread and dissipate across the network, causing shifts in attitude regarding what rules should be followed in terms of sending and receiving messages.

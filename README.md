22 October 2018

Mark and Maven is a hiring platform that uses Dossier instead of Resumes. Dossiers' are made of dynamic, contextual, verifiable personal data instead of user-inputted text, and can help to more accurately price human talent, helping with issues of diversity, gender imbalance, and talent underavailability. The platform consists of a graph of nodes, and each node is categorised as a bot, job, company, or humans. Nodes have an operating system and a profile. Their Operating Systems' purpose is to build up the nodes' profile, and profiles are made up of attribute key:value pairs. The types of attributes that a node can have include their characteristics/traits (as-yet undefined), experiences (as-yet undefined), and relationships to other nodes (as-yet undefined). 

This programme, mavenOS, is the operating system for a bot in the network called Maven.

0.9 Release Notes
*Trumpets sound* Exciting week! Mark and Maven, for the very first time have taken .json data extracted from a HAT and parsed it to put verifiable information into a node regarding the source's location. Mark and Maven can run the analyst.locationsBasic() function which returns locationsBigly (most common address in the sample), locationsBigNight (most common between 9pm-5am), and locationsBigWork (most common between 9am-5pm). It's a baby step, but a fun one, as we have successfully setup MavenOS to parse an external API for the v first time - the geopy library, which is v awesome.

0.9 Features list
- DONE mavenOS.admin.nodeCreate() connects all nodes to Maven Prime
- DONE all nodes to date are connected to Maven Prime
- DONE new f(x) mavenOS.importCall() searches the imports folder for a ID.txt file to import into the node
- DONE debug mavenOS.analyst.locationsBasic() 
- DONE create new nodes up to 19/10/2018
- DONE mavenOS.sourceJobs() exports all node data (not just ID)

ROADMAP 

1.0 Planned Features
- mavenOS.sourceNetwork() exports node type as well as ID
-- requires new f(x) mavenOS.sourceAttribute(ID, attribute key (opt)) which finds attributes of key or simply returns all attributes of given node
- New f(x) admin.update can recognize when an attribute already exists in-node and will avoid adding duplicate data
- A candidate can click a link that takes them to a page at markandmaven.com that walks them through how to create a Dossier
- A candidate can click a link that takes them to a page at markandmaven.com that talks about what Dossiers are and why they're valuable 
- www.markandmaven.com v2 scoped and shipped
- new function mavenOS.schema() can export the types of Characteristics/Traits, Experiences, and Relationships possessible of a node
- mavenOS can run when offline, deferring pending imports to the next time it IS online

Icebox:
- analyst no longer uses standard addresses and relies on the what3words API instead
- "analyst" and "admin" are global modules (and thus don't need to be locally stored)
- An admin can create (make), destroy (kill), amend (fix), and append (update) a node

Resources / links:
- [GetaDossier](https://github.com/MarkandMaven/mavenOS/blob/master/GetaDossier.txt)
- [mavenMilestones](https://github.com/MarkandMaven/mavenOS/wiki)
- [mavenHistory](https://github.com/MarkandMaven/mavenOS/commits/master/README.md)

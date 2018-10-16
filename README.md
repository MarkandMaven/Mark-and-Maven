16 October 2018

Mark and Maven is a hiring platform that uses Dossier instead of Resumes. Dossiers' are made of dynamic, contextual, verifiable personal data instead of user-inputted text, and can help to more accurately price human talent, helping with issues of diversity, gender imbalance, and talent underavailability. The platform consists of a graph of nodes, and each node is categorised as a bot, job, company, or humans. Nodes have an operating system and a profile. Their Operating Systems' purpose is to build up the nodes' profile, and profiles are made up of attribute key:value pairs. The types of attributes that a node can have include their characteristics/traits (as-yet undefined), experiences (as-yet undefined), and relationships to other nodes (as-yet undefined). 

This programme, mavenOS, is the operating system for a bot in the network called Maven.

0.8 Release Notes
We moved the structure of the network around a bit (easy when you don't have any nodes...) and now every node's OS lives in a single root folder. There are also two support modules "analyst" and "admin" and each Maven-classified node has a second programme for creating nodes in their network that come pre-connected. Some debugging was performed, but OSv08 still can't run the analyst module successfully.

0.8 Features list
- DONE Create Mark and Maven Source Folder, put all Mavens inside
- DONE Create Maven Prime (standard mavenOS)
- DONE debug mavenOS_v08
- DONE mavenOS_v08 no longer misses attribute exports from the anchorRoot node
- DONE Maven Mim, Shelley, Harrera all have nodes
- DONE Mim, Shelley, and Harerra have an OS 
- DONE Mim, Shelley, and Harerra have a CreateNode

ROADMAP 

0.9 Planned Features
- mavenOS sourceNodes(ID, 'job') works for Maven Prime (do we need to be able to see all jobs in the network at once? probs. Should Prime be able to run all of its functions over its networks' networks? (currently it's just searching its network, which only has Maven Nodes))
- debug mavenOS.analyst.locationsBasic() 

Icebox:
- "analyst" and "admin" are global modules (and thus don't need to be locally stored)
- A candidate can create a dossier from a (Databuyer-hosted) URL (ie "click here and follow the instructions"
- mavenOS has defined the Characteristics/Traits of a node
- mavenOS has defined the Experiences of a node
- mavenOS has defined the Relationships of a node
- An admin can create (make), destroy (kill), amend (fix), and append (update) a node
- Candidates are stored in a cloud-based systems with backup and automated comms? Like Mailchimp? Maybe?
- mavenOS can communicate with email addresses in the outside world

Resources / links:
[GetaDossier](https://github.com/MarkandMaven/mavenOS/blob/master/GetaDossier.txt)
[mavenMilestones](https://github.com/MarkandMaven/mavenOS/wiki)
[mavenHistory](https://github.com/MarkandMaven/mavenOS/commits/master/README.md)

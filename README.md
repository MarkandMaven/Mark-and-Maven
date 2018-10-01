# mavenOS
Operating system for Maven

1 October 2018

Mark and Maven is a hiring platform that uses a dynamic, contextual, verifiable profile data resource called a Dossier instead of a Resume. Dossiers' can more accurately price human talent, helping with issues of diversity, gender imbalance, and talent underavailability. The platform operates as a graph, including bots, jobs, companies, and humans as nodes. Each node has an operating system and a profiles. Profiles are made up of attributes. Attributes are characteristics/traits (as-yet undefined), experiences (as-yet undefined), and relationships to other nodes (as-yet undefined). 

This programme, mavenOS, is the operating system for a bot in the network called Maven.

0.6 Release Notes
mavenOS v0.6 has a new module, 'analyst', and a new feature. Maven can now read a Hub of All Things GPS locations data file and use it to return three new characteristics to a node: the most common GPS coordinates in that file, and the most common GPS coordinates in that file filtered for only workday timestamps, and only nighttime timestamps. 

0.6 Features list
- Add a new module "analyst" for processing raw data and turning it into characteristics
- Maven can import raw data for adding to nodes as characteristics, from the folder "Imports"
- Maven can add the following characteristics to a node (given GPS intake data from Hub of All Things DataBuyer in the imports folder): locationBigly (most common location in record), locationBigNight (same, overnight timestamps only), and locationBigWork (same, 9-5 only)

ROADMAP 

0.7 Planned Features
- mavenOS can determine from a raw data file which countries a candidate has been to and add as such to their Dossier

Icebox:
- A candidate can create a dossier from a (Databuyer-hosted) URL (ie "click here and follow the instructions"
- mavenOS has defined the Characteristics/Traits of a node
- mavenOS has defined the Experiences of a node
- mavenOS has defined the Relationships of a node
- An admin can create (make), destroy (kill), amend (fix), and append (update) a node
- Candidates are stored in a cloud-based systems with backup and automated comms? Like Mailchimp? Maybe?
- mavenOS can communicate with email addresses in the outside world

Resources / links:
GetaDossier = https://github.com/MarkandMaven/mavenOS/blob/master/GetaDossier.txt
mavenMilestones = https://github.com/MarkandMaven/mavenOS/wiki
mavenHistory = https://github.com/MarkandMaven/mavenOS/commits/master/README.md

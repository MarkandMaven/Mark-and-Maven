# mavenOS
Operating system for Maven Prime

10 September 2018

Mark and Maven is a hiring platform that's attempting to improve on the resume with a profile that's dynamic, verifiable, and contextual, better-representing and valuing the job candidate. These profiles will help to solve the pervasive issues in diversity, gender imbalance, and talent underavailability by improving the accuracy at which all candidates are priced, especially under-valued ones.

0.3 Release Notes
If last week was the birth of the "MaM profile creator", this week turned that into a v1 product in the form of the first iteration of mavenOS. mavenOS is a wrapper for all the product features we create in the form of a single program that an admin can run to get isht done. It kept all the outputs of locationsPrep, namely exports of interesting gps locations, and it still requires a bunch of manual steps by the admin user, but it's the foundation around which we'll built future Mark and Maven products. 

0.3 Features list
- An admin can run a single program, mavenOS, that navigates the process by which an applicant can create a Mark and Maven profile
- An admin can create a user profile for a MaM applicant, stored in csv to a local folder
- mavenOS can save an archive of user profiles in a local folder as a backup
- mavenOS can create an export of interesting locations from the users' dataset stored in csv to a local folder
- An admin can append a new profile to include a single verified location that they have gleaned from that users' dataset
- An admin can access a locally-stored copy of a users' profile
- mavenOS can append a copy of a locally-stored "feed" to document a new profile addition

ROADMAP 

0.4 Planned Features
- An admin can add as many verified locations to a users' MaM profile as they wish when creating their profile
- MaM has a better (branded) word for "Mark and Maven profile" that can be used as an alternative to resume
- MaM has a GitHub repo
- MaM applicant process is documented/signposted
- MaM has an online repository for 1) weekly updates and 2) product release notes (readmes)

Icebox:
- Candidates are stored in a cloud-based systems with backup and automated comms? Like Mailchimp? Maybe?
- mavenOS can communicate with email addresses in the outside world

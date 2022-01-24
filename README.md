# lookupservice
A web service that responds to GET requests where the caller passes in a URL and the service responds with some information about that URL.


We have an HTTP proxy that is scanning traffic looking for malware URLs. Before allowing HTTP connections to be
made, this proxy asks a service that maintains several databases of malware URLs if the resource being requested is
known to contain malware.
Write a small web service, in the language/framework your choice, that responds to GET requests where the caller
passes in a URL and the service responds with some information about that URL. The GET requests look like this:

GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}

The caller wants to know if it is safe to access that URL or not. As the implementer, you get to choose the response
format and structure. These lookups are blocking users from accessing the URL until the caller receives a response
from your service.

# Setup
Database: sqllite
Web service framework: Flask


1. git clone this repo
2. pyvenv opendns-exercise
3. cd opendns-exercise
4. source bin/activate
5. pip install requirements.txt
6. Setup the database (in venv dir)
7. sqlite3 malware.db
8. .mode csv malware
9. .import malware.csv malware
10. Run main.py
11. Connect to localhost:5000 via browser
12. /urlinfo/1 will return full list of urls in database
13. /urlinfo/1/{host:port}/{uri} will return reputation of host:port/uri
14. output should be json


● The size of the URL list could grow infinitely, how might you scale this beyond the memory capacity of this VM?
● The number of requests may exceed the capacity of this VM, how might you solve that? Bonus if you implement this.
● What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand URLs a day with updates arriving every 10 minutes.

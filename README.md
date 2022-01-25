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

# Test

1. Run test_lookupservice.py


# Enhancement Ideas
- **The size of the URL list could grow infinitely, how might you scale this beyond the memory capacity of this VM?**
    -- We could move to a self scalable database such as DynamoDB provided by Amazon Web Services

- **The number of requests may exceed the capacity of this VM, how might you solve that?**
    -- Increasing number of requests may increase the number of operations on the database. We could use a caching storage such as Elasticache provided by Amazon Web Services to temporarily store the results for frequently accessed websites.

- **What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand URLs a day with updates arriving every 10 minutes.**
    -- Multiple read-only servers: The system works by having a single leader who accepts data manipulation requests (INSERT/UPDATE) and numerous instances which read activity log to replicate what the leader is doing.
    -- Sharding database: Data sharding is splitting the dataset between different servers based on the hash key
    
- **Containerize the application and orchestrate**
    -- We can containerize the application along with its dependencies using platform as a service such as Docker. This helps to horizontally scale the application as demand grows. 

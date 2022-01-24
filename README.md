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

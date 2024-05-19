# A dockerized application with 2 Containers

## crawler-1
This goes through all the files in the designated link
once it crawls into a link that follows its rules
the data is scraped and each individual items is then pipelined into the **postgres container**. note that, the container will only function if the Postgres container runs before the crawer.<br>
<br>
Each data item is configured to pull exactly the required items from the designated class with variant requirments i.e, <br>
it manipulates the response through the use of (but not limitted to) ; mapping,filter,split,RegEx opperatios.
once all the possible files have been scraped, the function exits

## Postgres
It creates a table (if it already doesnt exists) to the allocated port number on the dockercomposite file, <br>
Then it is ready to insert/pipeline the data values that were scrapped and recieved from the crawler contgresainer
note that, no check were done if the value is repeated for each time the crawler is run for the following reason; <br>
<br>
The data inside the Postgres DB is non-persistant i,e once the container exits. the data saved becomes null. <br>
With that in mind this implementation assumes that there is no need to save the context of the DB for each run


I'll be the first to admit, that I've never really done Web Development, so I spent a little time exploring REST APIs and how to implement them in Python.

However, reading doesn't make up for actual experience with something, so I definitely have questions about how something like this would actually interface with a website.

For now, I've made my API a class with three functions to handle the required capabilities. The class also contains a Pandas DataFrame to act as the internal storage for the Database. I chose Pandas because it makes syntax for dealing with large data simple, it can easily convert to and from JSON (and get a csv/JSON from a URL), and it has NUMPY backend which is highly optimized Python (vectorized C backend) designed for fast manipulation of matrices/tables.

I made a Truck class to avoid repetition in code for when I want to add, update, or retrieve a Truck from the DF. Additionally, the class would make the code more readable instead of filling in every field into the JSON REST POST request each time I want to do a POST (imagining the posibility of an update function in the future). I avoided creating getters and setters for the variables to conserve time and also, I would want more information before creating functions that allow access to the variables (as in is there some function in the program that requires this access?). 

Additionally, I currently hardcoded the URL to create the dataframe, but that could easily be replaced with accessing the csv file or retrieving the URL from a configuration file. I also only added the bare minimum for creating a truck since, this would probably not be hardcoded in the real application anyway (I'm imagining a web form interface with drop down menus or an XML/CSV file read depending on the Use Case/User Story for this).

Also, normally, I would put the classes in their own separate files.

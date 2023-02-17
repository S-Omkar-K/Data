This project is a Python program that scrapes a webpage about the MPP program at the Harris School of Public Policy at the University of Chicago, and extracts information about the core courses required for the program. The program uses the requests and BeautifulSoup libraries to parse the HTML of the webpage and extract the relevant data.

The website being scraped is https://harris.uchicago.edu/academics/programs-degrees/degrees/master-public-policy-mpp, which is the webpage for the Master of Public Policy (MPP) program at the Harris School of Public Policy at the University of Chicago.

The information being parsed is related to the core courses required for the MPP program. Specifically, the code is searching for information about the courses that fulfill the MPP program's "6 core courses" requirement, which is a set of required courses that all MPP students must complete.

The code searches the HTML of the webpage for lists of courses and extracts the course names and descriptions, storing the information in a Python dictionary called my_dict. The code uses two different methods to retrieve the information: Method 1 uses the 'lxml' parser and Method 2 uses the 'html.parser' parser. Both methods find the same information, but they use slightly different approaches to navigate the HTML and extract the relevant data.

Once the data is stored in the my_dict dictionary, the code cleans up the dictionary by removing any keys with empty values. The cleaned-up dictionary is then printed to the console.

Finally, the code accesses specific values in the dictionary by their keys to print out the course names of two specific core courses: "Analytical Politics I" and "Microeconomics Sequence I".

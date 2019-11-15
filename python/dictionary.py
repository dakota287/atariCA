#storing info in key value pairs
# the word is the key; 
# the value is the definition;
# ie: a word and a definition in an actual dictionary 

monthConversions = {
"Jan": "January",
"Feb": "February",
"Mar": "March",
"Apr": "April",
"May": "May",
"Jun": "June",
"Jul": "July", 
"Aug": "August",
"Sep": "September",
"Oct": "October",
"Nov": "November",
"Dec": "December"
}

print(monthConversions.get("luv", "that is not a valid key!!"))
####The .get method will give you a default of "none" for the return value or if you enter a comma followed by a value then it will give you a tuple defaulet. 




from pyscript import document,display



def process(e):
    document.getElementById("output1").innerHTML = ""
    x = ['Noelle Holiday','Oliver Pungenca','Elise Ifthen','Abigail Orchard','Emil Sinclair'] #accepted names for the input's value

    a = (document.getElementById('1stput').value) #gets firstname input
    b = (document.getElementById('2ndput').value) #gets surname input
    result = a + " " + b #combines both inputs to create the result

    r = [f"Sorry {result}, your name is not on the list.", f"Congratulations! {result}!You are now part of the ICT club."]

    
    checker = result in x #checks if the value is apart of the set

    f = r[checker]
    display(f, target="output1")

# Elements
# Dictionary with information about Non-metals
# Element Symbol: Element Name, Atomic Number, Atomic Mass
nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Se": ("Selenium", 34, 78.97),
    "F": ("Fluorine", 9, 18.998),
    "Cl": ("Chlorine", 17, 35.45),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.90),
    "At": ("Astatine", 85, 210),
    "Te": ("Tennessine", 117, 294),
    "He": ("Helium", 2, 4.003),
    "Ne": ("Neon", 10, 20.180),
    "Ar": ("Argon", 18, 39.948),
    "Kr": ("Krypton", 36, 83.798),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222),
    "Og": ("Oganesson", 118, 294)}
#          Key      :  Value

# Create a function to search a nonmetal
def search_element(e):
    # Get input from HTML
    Element1 = document.getElementById("element1").value
    # Retrieve information from the dictionary
    result = nonmetals.get(Element1, ("Element not found!", "N/A", "N/A"))
    # Display of result
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]


def submit(e):
    document.getElementById("output").innerHTML = "" #clears the previous output when a new one is inputted

    Grade_7 = {'Adrian Christian Hernandez', 'Daniel Harwell', 'Robert Rodriguez', 'Claudine Amington', 'John Doe'}
    Grade_8 = {'Carlos Borromeo', 'Joaquin Castor', 'Philip Ponce', 'Gerthy Bausa', 'Danielle Sandoval'}
    Grade_9 = {'Princess Schwab', 'Nathan Ladion', 'Jericho Magsalin', 'Eran Diaz', 'Jacob Sherburn'}
    Grade_10 = {'Therese Reyes', 'Cheree Mendoza', 'Zoey Ledres', 'Samantha Lacuesta', 'Francis Fernandez'} #sets including the students in their respective grade level

    fname = (document.getElementById('firstname').value) #grabs the firstname textbox's input
    sname = (document.getElementById('surname').value) #grabs the surname textbotx's input
    result = fname + " " + sname #combines both value above and adds a space between to create the full name

    master_set = Grade_7 | Grade_8 | Grade_9 | Grade_10 #unionizes each set to become the master_set's value
    master_set.add(result) #adds inputted results into the master_set's values
    master_set = ", ".join(sorted(master_set)) #sorts the master_set's values in alaphabetical order

    full_list = master_set.split(",")

    display(f"Student list: {master_set} | " f"Total number of students:{len(full_list)}", target="output") #displays the text "student list:" and follows up with master set values, then displays the total number of values in the variable
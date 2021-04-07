# Homework 3: Python
# Python Challenge #3: PyBoss
#
# I created a Python script to modify employee information and records, 
# due to a new HR program being implemented in a company, which requires
# certain format. 
# Make sure to run the script from the right directory for the relative path to work.

# Import modules
import os
import csv
import datetime

# Create path for csv and output
employees_csv = os.path.join("Resources","employee_data.csv")
output_path = os.path.join("Analysis","newemployee_data.csv")

# Define initial arrays
ids = []
names = []
lastnames = []
newdates = []
censorssn = []
states = []

# Define censor function
def censor(text, word):
    return text.replace(word, "*" * len(word))

# Define states dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open file and calculate values, skip header
with open(employees_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:
        empid = str(row[0])
        compname = str(row[1])
        date = str(row[2])
        ssn = str(row[3])
        state = str(row[4])

        # Get names and last names, save into new arrays
        splittedname = compname.split()
        names.append(splittedname[0])
        lastnames.append(splittedname[1])

        # Change date format, save into new array
        indate = datetime.datetime.strptime(date,'%Y-%m-%d')
        newdate = indate.strftime('%m/%d/%Y')
        newdates.append(newdate)
        
        # Censor first digits of SSN, save into new array
        splitssn = ssn.split("-")
        part1 = censor(ssn,splitssn[0])
        part2 = censor(part1,splitssn[1])
        censorssn.append(part2)
        
        # Change state names to abbreviations
        abbreviate = (f'{us_state_abbrev[state]}')
        states.append(abbreviate)

        # Get employee id data
        ids.append(empid)

    # Export new format of employee data
    with open(output_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the headers
        csvwriter.writerow(['Emp ID','First Name', 'Last Name', 'DOB', 'SSN', 'State'])

        # Write each row with the new data
        for i in range(len(ids)):
            csvwriter.writerow([ids[i],names[i],lastnames[i],newdates[i],censorssn[i],states[i]])
        





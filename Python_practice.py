#counties = ["Arapahoe","Denver", "Jefferson"]
#print(counties)

#if "Arapahoe" in counties and "El Paso" in counties:
    #print("Arapahoe and El Paso are in the list of counties.")
#else:

    #print("Arapahoe or El Paso is not in the list of counties.")

#print(counties[0])
#print(counties[1])  
#print(counties[2])
#print(counties[-2])
#print(counties[-1])

#print(len(counties))

#print(counties[0:2])

#counties.append("El Paso")
#counties.insert(2, "El Paso")
#counties.remove("El Paso")
#counties.pop(3)
#counties[2] = "El Paso"
#print(counties)

#counties_tuple = ("Arapahoe","Denver", "Jefferson")
#print(len(counties_tuple))
counties = ["Arapahoe","Denver", "Jefferson"]
#print(counties)

counties_dict = dict({"Arapahoe": 422829, "Denver": 463353, "Jefferson" : 432438})

#print(counties_dict)
#print(len(counties_dict))
#print(counties_dict.items())
#print(counties_dict.keys())
#print(counties_dict.values())
#print(counties_dict.get("Denver"))
#print(counties_dict["Arapahoe"])
for i in range(len(counties)):
    print(counties[i])
print("1")
for voters in counties_dict.values():
    print(voters)
print("2")
for county in counties_dict:
    print(counties_dict.get(county))
print("3")
for county, voters in counties_dict.items():
    print(county, voters)


for county, voters in counties_dict.items():
    #Using standard for concatenation
    #print(county + " county has " + str(voters) + " registered voters.")
    # Using f-strings for concatenation
    print(f"{county} county has {voters} registered voters.")


# List of dictionaries for voting date, appending and removing
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data.append({"county": "El Paso", "registered_voters": 487524})
voting_data.append({"county": "Queens", "registered_voters": 497524})

voting_data.remove({"county": "Queens", "registered_voters": 497524})
voting_data.remove({"county": "El Paso", "registered_voters": 487524})


#for county_dict in voting_data:
    #print(county_dict['county'])

#print(voting_data)
#print(len(voting_data))

# Method 1 using input
    # How many votes did you get?
    # my_votes = int(input("How many votes did you get in the election? "))
    #  Total votes in the election
    # total_votes = int(input("What is the total votes in the election? "))
    # Calculate the percentage of votes you received.
    # ercentage_votes = (my_votes / total_votes) * 100
    # print("I received " + str(percentage_votes)+ " % of the total votes.")

# Method 2 using f-strings with input
    #my_votes = int(input("How many votes did you get in the election? "))
    #total_votes = int(input("What is the total votes in the election? "))
    #print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
    #print("Turn on the AC.")
#else:
    #print("Open the windows.")

#What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
    # print('Your grade is an A.')
# else:
    # if score >= 80:
        # print('Your grade is a B.')
    # else:
        # if score >= 70:
            # print('Your grade is a C.')
        # else:
            # if score >= 60:
                # print('Your grade is a D.')
            # else:
                # print('Your grade is an F.')
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)




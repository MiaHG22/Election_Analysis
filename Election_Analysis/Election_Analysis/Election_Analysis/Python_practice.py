print("Hello World")
type(3)
ballots=1,341
print(ballots)
print(type(ballots))
print(type(73.81))
print(type("hello world"))
print(type(True)) 
print(5+2*3)
counties=["Arapahoe", "Denver", "Jefferson"]
print(counties)
print(counties[0])
print(counties[1])
print(counties[-1])
print(len(counties))
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties[2]="El Paso"
print(counties)
counties_tuple=("Arapahoe", "Denver", "Jefferson")
print(len(counties_tuple))
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
print(voting_data)
print(len(voting_data))
voting_data.append({"county":"El Paso", "registered_voters":461149})
print(voting_data)
voting_data.pop(3)
print(voting_data)
# How many votes did you get?
my_votes=int(input("How many votes did you get in the election?"))
# Total votes in the election
total_votes=int(input("What's the total votes in the election?"))
# Calculate the percentage of votes you received
percentage_votes=(my_votes/total_votes)*100
print("I received"+ str(percentage_votes)+"% of the total votes,")
counties=["Arapahoe", "Denver", "Jefferson"]
if counties[1]=="Denver":
    print(counties[1])
print(len(counties_dict))
score=int(input("What's your test score?"))
if score>=90:
    print("Your grade is an A")
elif score>=80:
    print("Your grade is a B")
elif score>=70:
    print("Your grade is a C")
elif score>=60:
    print("Your grade is a D")
else:
    print("Your grade is a F")
counties=["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

x=0
while x<=5:
    print(x)
    x=x+1

for county in counties:
    print(county)
counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])  
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, voters)
voting_dta=[{"county":"Arapahoe", "registered voters": 422829},
             {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
    print(counties_dict)
for counties_dict in voting_data:
    for value in counties_dict:
        print(value)
counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county, voters in counties_dict.items():
    print(county + " county has "+str(voters)+" registered voters.")
counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county, voters in counties_dict.items():
    print(f'{county} has {voters} registered voters.')

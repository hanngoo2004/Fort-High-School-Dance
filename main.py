# set ticket price to 0

ticket_price = 0
# set pupil_name as a list
pupil_name = []

# Ask for group name
group_name = input ("Please enter the name of your group ")

# Ask for number in the group
group_no = int(input("How many pupils are in your group? "))

# Validate the no. of pupils in the group
while group_no <3 and group_no > 10 :

# If wrong ask to re enter no. in group
  group_no = int(input("ERROR. Please enter a valid number of pupils"))

# loop for number of pupils in group
  for x in range(group_no):
    # Ask for individual names of pupils
    pupil_name.append == input("Please enter each individual pupils name ")
  # Ask if that pupil wants a photo or not
  photo = input ("Do you want a photo? ")

# If the pupil wants a photo their ticket is 4.99
  if photo == "yes":
      ticket_price = 4.99
      # Otherwise their ticket is 3.00
  else:
      ticket_price = 3.00
# Then display everything 

print(group_name)
print(group_no)
print(pupil_name) 
print(ticket_price)
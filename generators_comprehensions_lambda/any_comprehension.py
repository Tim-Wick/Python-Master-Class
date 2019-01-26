from named_tuples import people, basic_plants_list, plants_list

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit list of recipients")

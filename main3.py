from pyscript import display, document 

def show_club_info(e):
    club_selected= int(document.getElementById("clubselect").value)
    
    club_description={"Dance Club" : "A club for people with dance hobbies and school preformances." , 
                   "Glee Club" : "A club for people with singing hobbies and school preformances." , 
                   "Science Club" : "A club for people who love science." , 
                   "Communication Arts Club" : "A club for people with writing hobbies." , 
                   "Basketball Varsity" : "A club for people who love basketball." , 
                   "Volleyball Varsity" : "A club for people who love volleyball."}
    
    club_meet_time={"Dance Club" : "Tuesday 03:00 - 05:00 PM" , 
                   "Glee Club" : "Monday 03:00- 05:00 PM" , 
                   "Science Club" : "Tuesday  03:00 - 04:00 PM" , 
                   "Communication Arts Club" : "Wednesday 03:00 - 04:00 PM, Friday 03:00 - 04:00 PM" , 
                   "Basketball Varsity" : "Monday 03:00 - 04:00 PM" , 
                   "Volleyball Varsity" : "Wednesday 03:00 - 04:00 PM"}
    
    club_location={"Dance Club" : "Teatro Preciosa" , 
                   "Glee Club" : "High School Music Room" , 
                   "Science Club" : "Room 404" , 
                   "Communication Arts Club" : "Room 406" , 
                   "Basketball Varsity" : "Quadrangle" , 
                   "Volleyball Varsity" : "Quadrangle"}
    
    club_advisors={"Dance Club" : "Mr. Alfred Cases" , 
                   "Glee Club" : "Mr. Denver Martin" , 
                   "Science Club" : "Ms. Jameelyn Maramag" , 
                   "Communication Arts Club" : "Ms. Yannis Fernandez" , 
                   "Basketball Varsity" : "Mr. Adrian Ruiz" , 
                   "Volleyball Varsity" : "Mr. Adrian Ruiz"}
    
    club_num_of_members={"Dance Club" : "30" , 
                   "Glee Club" : "25" , 
                   "Science Club" : "20" , 
                   "Communication Arts Club" : "20" , 
                   "Basketball Varsity" : "24" , 
                   "Volleyball Varsity" : "24"}
    
    club_category={"Dance Club" : "Non-Academic" , 
                   "Glee Club" : "Non-Academic" , 
                   "Science Club" : "Academic" , 
                   "Communication Arts Club" : "Academic" , 
                   "Basketball Varsity" : "Non-Academic" , 
                   "Volleyball Varsity" : "Non-Academic"}
    
    if club_selected == 1:
        display(f"""Dance Club\n
                Description: {club_description["Dance Club"]}\n
                Advisor: {club_advisors["Dance Club"]}\n
                Locaton: {club_location["Dance Club"]}\n
                Meeting Time: {club_meet_time["Dance Club"]}\n
                No. of Members: {club_num_of_members["Dance Club"]}\n
                Category: {club_category["Dance Club"]}""" , target="info_output", append=False)
    
    elif club_selected == 2:
        display(f"""Glee Club\n
                Description: {club_description["Glee Club"]}\n
                Advisor: {club_advisors["Glee Club"]}\n
                Locaton: {club_location["Glee Club"]}\n
                Meeting Time: {club_meet_time["Glee Club"]}\n
                No. of Members: {club_num_of_members["Glee Club"]}\n
                Category: {club_category["Glee Club"]}""" , target="info_output", append=False)
    

    elif club_selected == 3:
        display(f"""Science Club\n
                Description: {club_description["Science Club"]}\n
                Advisor: {club_advisors["Science Club"]}\n
                Locaton: {club_location["Science Club"]}\n
                Meeting Time: {club_meet_time["Science Club"]}\n
                No. of Members: {club_num_of_members["Science Club"]}\n
                Category: {club_category["Science Club"]}""" , target="info_output", append=False)
    
    elif club_selected == 4:
        display(f"""Communication Arts Club\n
                Description: {club_description["Communication Arts Club"]}\n
                Advisor: {club_advisors["Communication Arts Club"]}\n
                Locaton: {club_location["Communication Arts Club"]}\n
                Meeting Time: {club_meet_time["Communication Arts Club"]}\n
                No. of Members: {club_num_of_members["Communication Arts Club"]}\n
                Category: {club_category["Communication Arts Club"]}""" , target="info_output", append=False)
    
    elif club_selected == 5:
        display(f"""Basketball Varsity\n
                Description: {club_description["Basketball Varsity"]}\n
                Advisor: {club_advisors["Basketball Varsity"]}\n
                Locaton: {club_location["Basketball Varsity"]}\n
                Meeting Time: {club_meet_time["Basketball Varsity"]}\n
                No. of Members: {club_num_of_members["Basketball Varsity"]}\n
                Category: {club_category["Basketball Varsity"]}""" , target="info_output", append=False)
    
    elif club_selected == 6:
        display(f"""Volleyball Varsity\n
                Description: {club_description["Volleyball Varsity"]}\n
                Advisor: {club_advisors["Volleyball Varsity"]}\n
                Locaton: {club_location["Volleyball Varsity"]}\n
                Meeting Time: {club_meet_time["Volleyball Varsity"]}\n
                No. of Members: {club_num_of_members["Volleyball Varsity"]}\n
                Category: {club_category["Volleyball Varsity"]}""" , target="info_output", append=False)

    elif club_selected == 0:
        display(f"""Please Choose A Club :).""" , target="info_output", append=False)
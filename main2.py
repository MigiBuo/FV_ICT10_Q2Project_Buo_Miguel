from pyscript import display, document # type: ignore

def general_weighted_average (e):
    FirstName = document.getElementById('1stName').value
    LastName = document.getElementById('LstName').value
    Science = float(document.getElementById('Sci').value)
    Math = float(document.getElementById('Mat').value)
    English = float(document.getElementById('Eng').value)
    SocSci = float(document.getElementById('Soc_Sci').value)
    Filipino = float(document.getElementById('Fil').value)
    InCoTe = float(document.getElementById('In_Co_Te').value)
    subjects = ['Science', 'Math', 'English', 'SS', 'Filipino', 'ICT']

    weighted_sum = (Science*5 + Math*5 + English*5 + SocSci*4 + Filipino*3 + InCoTe*2)
    total_units = (5 * 3) + 4 + 3 + 2
    gwa = weighted_sum / total_units

    summary = f"""{subjects[0]}: {Science:.0f}
    {subjects[1]}: {Math:.0f}
    {subjects[2]}: {English:.0f}
    {subjects[3]}: {SocSci:.0f}
    {subjects[4]}: {Filipino:.0f}
    {subjects[5]}: {InCoTe:.0f}
        """
    
    display(f'Name: {FirstName} {LastName}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
from pyscript import document

#clubs is a dictionary that is like a variable that holds my keys and values for my button/generation. 
clubs = {
    "Dance Club": {
        "D1": "<br> Aims to enhance your skills in dancing and sharpen your movements through professional and proper training.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br> Tuesday ~ 3:00 p.m. to 5:00 p.m.", #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br> Teatro Preciosa", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br> Mr. Alfred Cases", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 27", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br> Performance Arts" #C1 is a key I assigned for category that will be utilized in my button. 
    },

    "Math Club": {
        "D1": "<br> This club ensures to sharpen and polish your numerical skills by introducing to you speed, methods, and competitions all year round.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br> Monday ~ 2:30 p.m. to 3:30 p.m.", #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br> 404", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br> Mr. Nicole Gabuya", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 16", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br> Academic" #C1 is a key I assigned for category that will be utilized in my button. 
    },
    "Science Club": {
        "D1": "<br> Explores the natural essence of the world through precision and accuracy.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br> Tuesday ~ 3:00 p.m. - 4:00 p.m. <br> Friday ~ 2:00 p.m. - 3:00 p.m.",  #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br> Room 404", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br> Ms. Jameelyn Maramag", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 18", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br> Academic" #C1 is a key I assigned for category that will be utilized in my button. 
    },
    "Communications Club": {
        "D1": "<br> This aims to enhance your public speaking and literature skills.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br> Wednesday ~ 3:00 p.m. - 4:00 p.m. <br> Friday ~ 3:00 p.m. - 4:00 p.m.",  #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br> Room no. 406", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br> Ms. Yannis Fernandez", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 23", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br> Academic" #C1 is a key I assigned for category that will be utilized in my button. 
    },
    "Volleyball Varsity": {
        "D1": "<br>Aims to develope and enhance skills of talented students who desire to take on the sport to the big stage.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br>Wednesday ~ 3:00 p.m. - 5:00 p.m.",  #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br> Quadrangle", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br> Mr. Adrian Ruiz", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 24", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br>Sports" #C1 is a key I assigned for category that will be utilized in my button. 
    },
    "Basketball Varsity": {
        "D1": "<br> This nurtures future skillful and talented athletes for the big arena!", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br>Monday ~ 3:00 p.m. – 5:00 p.m.",  #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br>Quadrangle", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br>Mr. Adrian Ruiz", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 16", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br>Sports" #C1 is a key I assigned for category that will be utilized in my button. 
    },
    "COCC Club": {
        "D1": "<br> Instills discipline and leadership skills within determined students.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br>Wednesday ~ 2:30 p.m. - 4:30 p.m.",  #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br>Quadrangle/Theatro Preciosa", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br>SSgt Jemima David, PA (Res)", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 24", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br>Academic" #C1 is a key I assigned for category that will be utilized in my button. 
    }, 
     "Marching Band Club": {
        "D1": "<br>Practices the art of creativity and unity through music.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br> Monday ~ 3:00 p.m.- 4:30 p.m. <br> Tuesday ~ 3:00 p.m.- 4:30 p.m. <br> Wednesday ~ 3:00 p.m. - 4:30 p.m.",  #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br>Marching Band Room ", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br>Mr. Emilio Alumno", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 42", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br> Music" #C1 is a key I assigned for category that will be utilized in my button. 
    },  
     "Social Studies Club": {
        "D1": "<br>Aims to enhance debate skills and sharpen points during arguments.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br> Tuesday ~ 3:00 p.m. - 4:00 p.m. <br> Thursday ~ 3:00 p.m. - 4:00 p.m.",  #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br>Room 409", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br>Mr. Roberto Lim ", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 42", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br> Academic" #C1 is a key I assigned for category that will be utilized in my button. 
    },  
     "Glee Club": {
        "D1": "<br>This club combines different voices to create a masterpiece for our ears.", #D1 is a key I assigned for description that will be utilized in my button. 
        "MT": "<br> Monday ~ 3:00 p.m. - 4:30 p.m. <br> Friday ~ 3:00 p.m. - 4:30 p.m.",  #MT is a key I assigned for meeting time that will be utilized in my button. 
        "L1": "<br> High School Music Room", #L1 is a key I assigned for location that will be utilized in my button. 
        "A1": "<br>Mr. Denver Martin", #A1 is a key I assigned for club moderator that will be utilized in my button. 
        "M1": "<br> 28", #M1 is a key I assigned for number of members that will be utilized in my button. 
        "C1": "<br> Music" #C1 is a key I assigned for category that will be utilized in my button. 
    },
}

#This is the code for my button that is found in my index.html as when clicked, this code will be executed.
def club_info(e):
    dropdown = document.getElementById("type")
    selected = dropdown.value
#I used select and dropdown for my form in my index.html. Having these two codes in python makes sure that whatever the user clicks in the choices, that is the club info they will receive.
    output = document.getElementById("club-output")
#This displays the club info of their selected club direcntly of the main html through the div id in the index.html.
    if selected == "none":
        output.innerHTML = "<b><span style='color:#264085;'>Please select a club first.</span</b>"
        return
#This code will be executed in the html if the user failed to select any of the following clubs and will show up directly at the html file. 
    data = clubs.get(selected)
    html = f"""
        <h2 style='color:#264085; font-weight:bolder; font-size:70px;'>{selected}</h2>
        <p><b><span style="color:#264085">Description:</span></b> {data['D1']}</p>
        <p><b><span style="color:#264085">Meeting Time:</span></b> {data['MT']}</p>
        <p><b><span style="color:#264085">Location:</span></b> {data['L1']}</p>
        <p><b><span style="color:#264085">Club Moderator:</span></b> {data['A1']}</p>
        <p><b><span style="color:#264085">Number of Members:</span></b> {data['M1']}</p>
        <p><b><span style="color:#264085">Category:</span></b> {data['C1']}</p>
    """
    output.innerHTML = html
    #This code will be executed in the html if the user selects one of the choices and it will show up directly as the html file


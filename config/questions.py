'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html

GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.3.10.30
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "C:/Users/Pc/Desktop/buscar trabajo/Tomás Friz.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "1"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://tomasfriz.github.io/Tomas-Agustin-Friz/"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "www.linkedin.com/in/tomasagustinfriz"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = ""



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 6000000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 6000000            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 0                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Desarrollador Web Full Stack" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
★ PUEDO AYUDARTE\n
- Diseño, programación, mejoras y mantenimiento de páginas web.\n
- Solución de errores y fallas.\n
- Creación y migración de hosting.\n
- Carga de contenido, posicionamiento, optimización y SEO en WordPress.\n
\n
★ Tengo conocimientos en:\n
- Lenguajes: HTML5, CSS3, SASS, JavaScript, Python, Java, C, C#.\n
- Frameworks y Librerías: React.js, Angular, VUE.js, Laravel, Node.js, Spring Boot, Express, Tailwind.css, Bootstrap, Next.js, Vite.js.\n
- Bases de Datos: SQLServer, MySQL, MongoDB, OracleDB, Firebase, Firestore.\n
- Diseño y UX/UI: Figma, Photoshop, Illustrator, Canva.\n
- Herramientas: Git, GitHub, GitHub Pages, Trello, Jira, Slack, Aptugo, Visual Studio Code, IntelliJ.\n
- Otras Tecnologías: APIs, PWA, JSON, Linux, Hosting, Inteligencia Artificial (IA), Arduino.\n
\n
★ Puedes contactar conmigo de 2 formas:\n
- Cel: +54 9 1131574246\n
- Mail: tomas.agustin.friz@gmail.com\n
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Estimado/a:\n
\n
Me dirijo a usted para expresar mi interés en la vacante publicada. Soy Desarrollador Full Stack Junior y actualmente estoy cursando la carrera de Analista de Sistemas en la Escuela Da Vinci.\n
\n
Estoy entusiasmado por la posibilidad de formar parte de su equipo, donde pueda aplicar los conocimientos adquiridos, además de mis habilidades en diseño y desarrollo web, para contribuir al logro de los objetivos organizacionales.\n
\n
A lo largo de mi formación y experiencia, he desarrollado una gran capacidad de aprendizaje y adaptación, trabajando de manera eficiente en equipo con espíritu colaborativo. También destaco en la planificación del tiempo y el cumplimiento de tareas con responsabilidad y proactividad.\n
\n
Estoy seguro de que mi perfil técnico, junto con mis habilidades interpersonales, pueden aportar valor a su empresa, y estoy igualmente motivado por las oportunidades de aprendizaje y desarrollo que puedan surgir al trabajar con ustedes.\n
\n
Adjunto mi CV para que pueda conocer más sobre mi perfil profesional. Quedo a su disposición para una entrevista donde pueda ampliar esta información y conversar sobre cómo puedo contribuir a su equipo.\n
\n
Gracias por su tiempo y consideración.\n
Atentamente, Tomás Agustín Friz.\n
\n
Teléfono: +54 9 11 3157-4246\n
Mail: tomas.agustin.friz@gmail.com\n
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
'''

# Name of your most recent employer
recent_employer = "Not Applicable" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "1"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################
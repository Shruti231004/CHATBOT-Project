import json


# Load the existing JSON data
with open('intents.json', 'r') as file:
    data = json.load(file)


# JSON structure with URLs
chatbot_data_with_urls = {
    "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey", "Good day", "How are you?"],
      "responses": ["Hello!", "Good to see you!", "Hi there, how can I help?"]
    },
    {
      "tag": "farewell",
      "patterns": ["Goodbye", "Bye", "See you later", "Talk to you later"],
      "responses": ["Sad to see you go :(", "Goodbye!", "Come back soon!"]
    },
    {
      "tag": "hours",
      "patterns": ["What are the college timings?", "When is the college open?", "What are your hours of operation?"],
      "responses": ["The college is open from 8am to 5pm, Monday to Friday."]
    },
    {
      "tag": "contact",
      "patterns": ["How can I contact the college?", "What is the college telephone number?", "Can I get your contact number?"],
      "responses": ["You can contact the college at 0250-233 9486 or email us at info@vcet.edu.in."]
    },
    {
      "tag": "courses",
      "patterns": ["What courses are offered in the college?", "Can you tell me about the available courses?", "What are the branches in the college?"],
      "responses": ["The college offers courses in Information Technology, Computer Engineering, AI&DS ,Mechanical Engineering, VLSI & Designing Engineering, and Civil Engineering."]
    },
    {
      "tag": "fees",
      "patterns": ["How much is the college fee?", "Tell me about the fees", "What are the hostel fees?"],
      "responses": ["For detailed fee information, please follow the given link: https://vcet.edu.in/wp-content/uploads/2023/07/Approved-Fees-Structure-for-Academic-Year-2023-24.pdf"]
    },
    {
      "tag": "location",
      "patterns": ["Where is the college located?", "What is the college address?", "How can I reach the college?"],
      "responses": ["The college is located at K.T Marg, Shastri Nagar, Vishal Nagar, Vasai West, Vasai-Virar, Maharashtra 401202 . You can find the location on Google Maps."]
    },
    {
      "tag": "events",
      "patterns": ["What events are organized in the college?", "Are there any upcoming events?", "Tell me about the college events."],
      "responses": ["For information about the events, follow the given link: https://vcet.edu.in/ "]
    },
    {
      "tag": "admission",
      "patterns": ["What is the admission process?", "How can I take admission in the college?", "Tell me about the admission criteria."],
      "responses": ["For detailed admission information, follow the given link: https://forms.gle/tKSfZKHmxRey3U3P9"]
    },
    {
      "tag": "library",
      "patterns": ["Does the college have a library?", "What are the library timings?"],
      "responses": ["Yes, the college has a library.  The timings are from 9am to 5pm, Monday to Friday."]
    },
    {
      "tag": "facilities",
      "patterns": ["What facilities are available in the college?", "Tell me about the college facilities.", "Do you have a sports complex?"],
      "responses": ["The college provides various facilities including a sports complex, labs, canteen, and a library."]
    },
    {
      "tag": "placement",
      "patterns": ["How are the placements in the college?", "Tell me about the college placements.", "What is the placement record?"],
      "responses": ["The college has a good placement record. Many reputed companies visit our campus for recruitment."]
    },
    {
      "tag": "strengths",
      "patterns": ["What are your college's strengths?", "What makes your college stand out?"],
      "responses": ["Our college excels in providing quality education, fostering a supportive learning environment, and offering a wide range of extracurricular activities."]
    },
    {
      "tag": "academics_reputation",
      "patterns": ["What departments or programs have the best reputations?", "Which academic programs are well-regarded?", "Are there any standout departments in your college?"],
      "responses": ["Our college has well-regarded departments in Computer Science. These programs have a strong reputation for academic excellence."]
    },
    {
      "tag": "professors_teachers",
      "patterns": ["Are your professors good teachers?", "How is the quality of teaching at your college?", "Do you have experienced faculty?"],
      "responses": ["Our college prides itself on having experienced and dedicated faculty members who are committed to providing quality education."]
    },
    {
      "tag": "independent_study",
      "patterns": ["Does your major require an independent study or capstone project?", "Are there opportunities for independent research?", "Is there a culminating project for your major?"],
      "responses": ["Many majors at our college offer opportunities for independent study or capstone projects. These experiences allow students to delve deeper into their fields of interest and apply their knowledge."]
    },
    {
      "tag": "first_year_experience",
      "patterns": ["What's it like to be a first-year student here?", "Can you describe the first-year experience?", "What should I expect as a freshman?"],
      "responses": ["As a first-year student, you can expect a supportive and welcoming environment. Orientation programs, peer mentoring, and academic support services are available to help you transition smoothly into college life."]
    },
    {
      "tag": "typical_day",
      "patterns": ["What's a typical day like?", "Can you describe a day in the life of a student?", "What's the daily routine at your college?"],
      "responses": ["A typical day as a student involves attending classes, engaging in study sessions, participating in extracurricular activities, and utilizing campus resources. Each student's daily routine may vary based on their schedule and interests."]
    },
    {
      "tag": "weekend_activities",
      "patterns": ["What do you do on the weekends?", "Are there weekend activities or events?", "How do students spend their weekends?"],
      "responses": ["On weekends, students often take part in campus events, recreational activities, social gatherings, and may also use the time for relaxation and personal pursuits."],
      "context_set": ""
    },
    {
      "tag": "social_scene",
      "patterns": ["What is the social scene like?", "How would you describe the social life on campus?", "Are there opportunities to meet new people?"],
      "responses": ["The social scene on campus is vibrant and diverse. There are plenty of opportunities to meet new people, join committies and organizations, attend social events, and build lifelong friendships."]
    },
    {
      "tag": "food",
      "patterns": ["How's the food?", "What is the quality of the food on campus?", "Are there good dining options?","How is the canteen food?"],
      "responses": ["The college provides a variety of dining options on campus, including cafeterias, food courts, and specialty restaurants. The quality of food is generally satisfactory, with options to cater to different dietary preferences."]
    },
    {
      "tag": "favorite_place_on_campus",
      "patterns": ["What's your favorite place on campus?", "Which location do you enjoy the most?", "Where do students like to hang out?"],
      "responses": ["As an AI, I don't have personal preferences. However, many students enjoy spending time in common areas, libraries, student centers, outdoor spaces, and campus cafeterias."]
    },
    {
      "tag": "campus_facilities",
      "patterns": ["What are the facilities like (science labs, libraries, theaters, gyms, etc.)?", "Are the campus facilities well-maintained?", "Does the college have modern facilities?"],
      "responses": ["Our college prides itself on maintaining well-equipped facilities to support students' academic and extracurricular activities. This includes modern science labs, libraries with extensive resources, theaters, and well-equipped gyms."]
    },
    {
      "tag": "computer_labs",
      "patterns": ["Are there enough computer labs?", "How accessible are the computer labs?", "Is there a shortage of computer lab facilities?"],
      "responses": ["Our college provides an ample number of computer labs across campus. These labs are accessible to students and equipped with the necessary technology and software needed for academic work."]
    },
    {
      "tag": "campus_wifi",
      "patterns": ["How is the WiFi on campus?", "Is the campus WiFi reliable?", "Are there any connectivity issues with the WiFi?"],
      "responses": ["The campus WiFi network is designed to provide reliable internet connectivity to students, faculty, and staff. However, occasional connectivity issues may arise, which are usually promptly addressed by the IT department."]
    },
    {
      "tag": "sports_popularity",
      "patterns": ["Are sports popular?", "Do many students participate in sports?", "What's the athletic culture like at your college?"],
      "responses": ["Sports are popular at our college, and many students participate in various athletic activities. We have a range of sports teams, intramural sports, and fitness programs to cater to different interests and skill levels."],
      "context_set": ""
    },
    {
      "tag": "student_body_unique",
      "patterns": ["What makes the student body unique?", "Is there anything special about the student population?", "What sets the students apart at your college?"],
      "responses": ["The student body at our college is unique in its diversity of backgrounds, perspectives, talents, and passions. This diversity fosters a rich learning environment and encourages students to embrace different cultures and viewpoints."]
    },
    {
      "tag": "campus_diversity",
      "patterns": ["Is there diversity on campus?", "Are there students from different cultural backgrounds?", "Does the college promote diversity and inclusion?"],
      "responses": ["Yes, our college values diversity and strives to create an inclusive campus community. Students from different cultural backgrounds, ethnicities, and countries contribute to the diverse fabric of our college community."]
    },
    {
      "tag": "internship_opportunities",
      "patterns": ["Are internships available? How do you find them?", "What internship opportunities are there?", "How does the college support students in finding internships?"],
      "responses": ["Internship opportunities are available for students, and the college often provides resources and support to help students find and secure internships. The college's career services office and faculty advisors can offer guidance in exploring and applying for internships."]
    },
    {
      "tag": "career_services",
      "patterns": ["Is Career Services helpful?", "What services does the career center provide?", "How effective is the college's career guidance?"],
      "responses": ["Career Services at our college offers various resources and assistance to help students with career exploration, resume building, job search strategies, interview preparation, and more. Many students find the career guidance helpful in their professional development."]
    },
    {
      "tag": "mentorship_program",
      "patterns": ["Do you have a mentor?", "Is there a mentorship program?", "How can students connect with mentors?"],
      "responses": ["Our college may have a mentorship program or opportunities for students to connect with mentors. These programs facilitate valuable guidance and support from experienced individuals who can provide insights and advice on academic and career paths."]
    },
    {
      "tag": "summer_jobs",
      "patterns": ["How easy is it to find summer jobs and other kinds of work through your school?", "Are there resources for finding summer employment?", "Does the college assist with summer job opportunities?"],
      "responses": ["Our college may provide resources and support to help students find summer jobs and other types of employment. The career services office, online job boards, and networking events can be valuable in exploring and securing summer job opportunities."],
      "context_set": ""
    },
    {
      "tag": "notable_graduates",
      "patterns": ["Who are some of the notable graduates from your college?", "Can you mention any famous alumni?", "Which successful individuals attended your college?"],
      "responses": ["Our college has a distinguished list of notable graduates and successful alumni in various fields. Some may include renowned professionals, entrepreneurs, artists, scientists, and leaders who have made significant contributions to their respective fields."]
    },
    {
      "tag": "about_vcet",
      "patterns": ["About vcet", "General information"],
      "responses": ["Vidyavardhinis College of Engineering and Technology (VCET) in Vasai, Maharashtra, affiliated with the University of Mumbai, offers AICTE-approved B.E. programs in Computer, Electronics and Telecommunication, Information Technology, Mechanical, and Civil Engineering. The campus features modern labs, a library, sports facilities, and active placement services."]
    }
    ]
}



# Add the new entries to the existing data
data['intents'].extend(chatbot_data_with_urls)

# Save JSON to a file
with open('intents.json', 'w') as json_file:
    json.dump(chatbot_data_with_urls, json_file, indent=4)

#print("Chatbot data with URLs has been saved to chatbot_data_with_urls.json")


from django.shortcuts import render

def home(request):
    """View for the home page"""
    context = {
        'title': 'Asher Green - Software Developer',
        'name': 'Asher Green',
        'role': 'Full-Stack Development | Software Engineering | Web Development',
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """View for the about page"""
    context = {
        'title': 'About Me',
        'name': 'Asher Green',
        'location': 'Pickering, Ontario',
        'email': 'asher@ashergreen.ca',
        'phone': '+1 (416) 729-3001',
        'linkedin': 'https://www.linkedin.com/in/asher-green-6a96551/',
        'github': 'https://github.com/ashergreen82',
        'website': 'www.ashergreen.ca',
        'bio': 'Versatile Software Developer skilled in Python, JavaScript (React), and C#. Known for delivering reliable, high-quality solutions via APIs and RESTful services. Brings positivity, strong debugging skills (PyCharm, VS Code, Visual Studio), and deep Git/GitHub experience to collaborative teams. Lifelong learner and committed team members known for exceptional loyalty and punctuality.',
        'skills': [
            {'category': 'Languages / Frameworks', 'items': 'Python, JavaScript, HTML/CSS, Go, React, Bootstrap, Flask'},
            {'category': 'Technologies', 'items': 'Git, GitHub, Postman, PostgreSQL'},
        ],
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    """View for the projects page"""
    projects_list = [
        {
            'title': 'Community Sales Mapping App',
            'status': 'In Development',
            'description': 'Maps garage sales during a community sales event on Google Maps.',
            'details': [
                'Developed a responsive React.js front-end for a community garage sales mapping application, collaborating with a back-end developer in a cross-functional team environment.',
                'Implemented an interactive map interface using Google Maps that displays and filters community garage sales by location and category.',
                'Gained valuable experience in collaborative development, Git workflow, and full-stack application architecture.',
            ],
            'link': 'https://community-map-207215937730.us-central1.run.app',
            'image': 'Screenshot 2025-05-12 105204 main screen.png',
        },
        {
            'title': 'Super Simple Chat App',
            'description': 'A simple group chat which allows you to send messages to everyone in a group.',
            'details': [
                'Written in HTML, CSS, JavaScript, ReactJS, Bootstrap, Python, Flask and PostgreSQL.',
                'Utilizes web sockets to display real-time messages to users.',
                'Implements a PostgreSQL database. Implements JSON Web Tokens for user authentication.',
            ],
            'link': 'https://chatapp-fdyf.onrender.com',
            'image': 'login_screenshot.png',
        },
        {
            'title': 'Star Wars App',
            'description': 'Accesses the Star Wars API (https://swapi.dev) to get information on the characters in the Star Wars franchise of the characters found in the movies.',
            'details': [
                'Written in HTML, CSS, Javascript, ReactJs and Bootstrap',
                'Utilizes the swap.dev RESTful API to retrieve character data displayed in application',
                'Deployed on Netlify',
            ],
            'link': 'https://silly-brigadeiros-d326dd.netlify.app',
            'image': 'background.jpg',
        },
    ]
    context = {
        'title': 'Projects',
        'projects': projects_list,
    }
    return render(request, 'portfolio/projects.html', context)

def resume(request):
    """View for the resume page"""
    education = [
        {
            'institution': 'ALGOEXPERT/PROGRAMMINGEXPERT',
            'details': [
                'Data Structures, Big O Notation, Logarithms, Arrays etc.',
                'Go, Software Design, Object Oriented Programming as well as other advanced programming.',
            ],
        },
        {
            'institution': 'BOOTCAMP FROM ZERO TO HERO IN PYTHON',
            'date': 'May 2022',
            'details': [
                'Developed skills in Python while learning core programming concepts.',
            ],
        },
    ]
    
    experience = [
        {
            'position': 'Software Development Mastermind (Mentorship Program)',
            'date': 'October 2022 – February 2024',
            'details': [
                'Strengthened programming skills across multiple languages and technologies, becoming a more versatile and well-rounded developer.',
                'Received invaluable feedback and coaching resulting in enhanced development skills in a professional environment.',
            ],
        },
    ]
    
    context = {
        'title': 'Resume',
        'name': 'Asher Green',
        'role': 'Full-Stack Development | Software Engineering | Web Development',
        'location': 'Pickering, Ontario',
        'email': 'asher@ashergreen.ca',
        'phone': '+1 (416) 729-3001',
        'linkedin': 'https://www.linkedin.com/in/asher-green-6a96551/',
        'github': 'https://github.com/ashergreen82',
        'website': 'www.ashergreen.ca',
        'education': education,
        'experience': experience,
        'skills': [
            {'category': 'Languages / Frameworks', 'items': 'Python, JavaScript, HTML/CSS, Go, React, Bootstrap, Flask'},
            {'category': 'Technologies', 'items': 'Git, GitHub, Postman, PostgreSQL'},
        ],
    }
    return render(request, 'portfolio/resume.html', context)

def contact(request):
    """View for the contact page"""
    context = {
        'title': 'Contact Me',
        'name': 'Asher Green',
        'email': 'asher@ashergreen.ca',
        'phone': '+1 (416) 729-3001',
        'linkedin': 'https://www.linkedin.com/in/asher-green-6a96551/',
        'github': 'https://github.com/ashergreen82',
    }
    return render(request, 'portfolio/contact.html', context)

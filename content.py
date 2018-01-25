# -*- coding: utf-8 -*-

from datetime import datetime

content = {
    'title': {
        'name': 'Michal',
        'family': 'Wachowski',
        'job': 'programmer &amp; software engineer',
        'location': 'Berlin'
    },
    'contact': {
        'url': [
            'http://mwachowski.pl',
            'https://github.com/Potfur/'
        ],
        'mail': [
            'wachowski.michal@gmail.com'
        ],
        'tel': [
            '+491724795137',
            '+48502251933'
        ],
    },
    'keywords': ['michal wachowski', 'programmer', 'engineer', 'developer', 'architect', 'resume', 'cv'],
    'description': 'Michal Wachowski resume',
    'authorship': '105788185695209510820',
    'analytics': 'UA-3665481-3',
    'lastmod': datetime.now().isoformat(),
    'skills': {
        'lang': {
            'title': 'Languages, DBMS & Tools',
            'nodes': [
                ['PHP', 'Python', 'JavaScript', 'Java'],
                ['MySQL', 'PostgreSQL', 'SQLite', 'MongoDB'],
                ['Git', 'Jenkins', 'Docker']
            ]
        },
        'methods': {
            'title': 'Methodologies, standards, good practices',
            'nodes': [
                [('OOP', 'Object Oriented Programming'), ('OOD', 'Object Oriented Design'),
                 ('DDD', 'Domain-driven Design'), ('TDD', 'Test-driven Design'),
                 ('BDD', 'Behavior-driven development')],
                ['clean code', 'design patterns', 'profiling', 'optimization', 'continuous integration',
                 'continuous deployment']
            ]
        }
    },
    'employment': [
        {
            'firm': 'Vimcar',
            'job': 'Senior software engineer',
            'time': [
                ['2015-10']
            ],
            'desc': [
                'Building distributed system that can process extensive streams of data for constantly growing number of users.',
                'Event based communication, event store and integration with different systems (IoT).'
            ]
        },
        {
            'firm': 'Rocket Internet',
            'job': 'Senior software engineer',
            'time': [
                ['2014-06', '2015-10']
            ],
            'desc': [
                'Took part in building flexible and mantainable platforms used by several Rocket\'s ventures.'
            ]
        },
        {
            'firm': 'TNN Finance',
            'job': 'Senior programmer',
            'time': [
                ['2012-07', '2014-05']
            ],
            'desc': [
                'Banking related domain allowed to build system based around concept of event store.',
                'Application had to process exchange rates coming from different sources in real time for calculating customer fees and real time reporting.'
            ]
        },
        {
            'firm': 'Caritas Polska',
            'job': 'Programmer',
            'time': [
                ['2007-01', '2013-12'],
                ['2011-12', '2012-02']
            ],
            'desc': [
                'Built several applications supporting resource planning for nationwide charity actions and data analysis.',
                'Low-traffic applications with large amounts of data and plenty of customizable reporting.'
            ]
        },
        {
            'firm': 'BEST IT Solutions INC.',
            'job': 'Programmer',
            'time': [
                ['2010-10', '2012-11']
            ],
            'desc': [
                'Started as bringing legacy code up to date and simple maintenance.',
                'Quickly evolved into managing traffic peaks, writing spam protection and a image filters.'
            ]
        },
        {
            'firm': 'Malachowski',
            'job': 'Senior programmer &amp; team leader',
            'time': [
                ['2009-04', '2010-01']
            ],
            'desc': [
                'Created application that allowed tracking and managing tailoring production processes.',
                'Integration with additional services / software like: accounting, multiple warehouse management tools, sewing and cutting machines etc.'
            ]
        },
        {
            'firm': 'Telekam',
            'job': 'Programmer',

            'time': [
                ['2006-01', '2007-12']
            ],
            'desc': [
                'Developed system that managed ISP connections according to accounting information - also part of developed system.'
            ]
        },
        {
            'firm': 'TEB',
            'job': 'Lecturer',

            'time': [
                ['2000-09', '2001-02']
            ],
            'desc': [
                'Lead a series of lectures on computer technologies, components and basic knowledge of computer science.'
            ]
        }
    ],
    'education': [
        {
            'degree': 'Engineer\'s degree',
            'polish': (
                'Inzynier',
                'Inzynier translates into Master of Engineering (M. Eng.), from what I was able to google out.'
            ),
            'school': 'Wyzsza Informatyczna Szkola Zawodowa (WISZ)',
            'desc': [
                'Type of studies: full time, engineering, majoring in system administration.',
                '<small>WISZ doesn\'t exist anymore, it merged with PWSZ under its name (another university in Gorzow Wlkp.).</small>'
            ]
        },
        {
            'degree': 'Technician\'s degree',
            'polish': 'Technik',
            'school': 'Zespol Szkol Technicznych i Ogolnoksztalcacych (ZSTiO)',
            'desc': [
                'Received technician\'s degree, specialization in electrotechnics, automatics and industrial robotics.'
            ]
        }
    ]
}

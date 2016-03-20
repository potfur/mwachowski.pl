# -*- coding: utf-8 -*-

from datetime import datetime

content = {
    'title': {
        'name': u'Michal',
        'family': u'Wachowski',
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
            '+4915154087506',
            '+48502251933'
        ]
    },
    'keywords': ['michal wachowski', 'programmer', 'software engineer', 'software architect', 'application architect',
                 'resume'],
    'description': 'Michal Wachowski resume',
    'authorship': '105788185695209510820',
    'analytics': 'UA-3665481-3',
    'lastmod': datetime.now().isoformat(),
    'skills': {
        'lang': {
            'title': 'Languages, DBMS & frameworks',
            'nodes': [
                ['PHP', 'JavaScript', 'Python', 'Node.js'],
                ['MySQL', 'PostgreSQL', 'SQLite', 'MongoDB'],
                ['Git', 'SVN']
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
                'Developing high traffic applications working on large data sets.',
                'Profiling &amp; improving efficiency'
            ]
        },
        {
            'firm': 'Rocket Internet',
            'job': 'Senior software engineer',
            'time': [
                ['2014-06', '2015-10']
            ],
            'desc': [
                'Responsible for designing and building flexible and maintainable platforms, tools and libraries for Rocket\'s ventures.'
            ]
        },
        {
            'firm': 'TNN Finance',
            'job': 'Senior programmer',
            'time': [
                ['2012-07', '2014-05']
            ],
            'desc': [
                'Hired to introduce new methodologies and good practices to existing development process. After that, I was responsible for redesigning old architectures to meet today\'s standards.',
                'Also for refactoring / profiling legacy code and database optimisation.'
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
                'Responsible (2007-2008) for creating two web applications that support resource planning for nationwide charity actions and later data analysis.',
                'Both use unique framework based on functional programming (that was before first Zend Framework release).',
                'In 2012 newer version of one of mentioned applications was made, with many improvements and new functionalities.'
            ]
        },
        {
            'firm': 'BEST IT Solutions INC.',
            'job': 'Programmer',
            'time': [
                ['2010-10', '2012-11']
            ],
            'desc': [
                'Mainly debugging, code analysis, safety improvements.',
                'Optimisation and profiling in response to traffic increase.'
            ]
        },
        {
            'firm': 'Malachowski',
            'job': 'Senior programmer &amp; team leader',
            'time': [
                ['2009-04', '2010-01']
            ],
            'desc': [
                'During that time I was responsible for creating an application supporting production processes using Gantt diagrams.'
                'Application was integrated with additional services / software like: accounting, warehouse management etc.'
            ]
        },
        {
            'firm': 'Telekam',
            'job': 'Programmer',

            'time': [
                ['2006-01', '2007-12']
            ],
            'desc': [
                'Development and integration of web applications managing wireless networks, and CRM applications.'
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

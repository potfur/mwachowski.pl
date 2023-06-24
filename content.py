# -*- coding: utf-8 -*-

from datetime import datetime

content = {
    'title': {
        'name': 'Michal',
        'family': 'Wachowski',
        'job': 'software engineer',
        'location': 'Berlin'
    },
    'contact': {
        'url': [
            'http://mwachowski.pl',
            'https://github.com/potfur/'
        ],
        'mail': [
            'wachowski.michal@gmail.com'
        ],
        'tel': [
            '+491724795137'
        ],
    },
    'keywords': [
        'michal wachowski',
        'software',
        'programmer',
        'engineer',
        'developer',
        'architect',
        'resume',
        'cv'
    ],
    'description': 'Michal Wachowski resume',
    'authorship': '105788185695209510820',
    'analytics': 'UA-3665481-3',
    'lastmod': datetime.now().isoformat(),
    'skills': {
        'lang': {
            'title': 'Languages, DBMS & Tools',
            'nodes': [
                ['Kotlin', 'Python', 'PHP', ('JavaScript', ['also with TypeScript']), 'Java'],
                [
                    ('SQL', ['PostgreSQL', 'MySQL', 'SQLite']),
                    ('NoSQL', ['MongoDB', 'DynamoDB', 'Redis']),
                    ('Messaging &amp; queues', ['SNS/SQS', 'RabbitMQ', 'Kafka'])
                ],
                [
                    'Git',
                    ('CI/CD', ['GitLab', 'GitHub', 'Jenkins']),
                    ('Container', ['Docker', 'JIB'])
                ]
            ]
        },
        'methods': {
            'title': 'Methodologies, ways of working',
            'nodes': [
                [
                    (
                        'System design',
                        ['Domain models', 'Boundaries', 'Contracts', 'Communication', 'Performance', 'Product alignment']
                    ),
                    (
                        'Architecture',
                        ['Microservice', 'Monolith', 'Distributed', 'Event-Based', 'Event-Sourcing',
                         'Command Query Responsibility Segregation', 'Ports and Adapters', 'Entity-Boundary-Interactor']
                    ),
                    ('Code organisation', ['Monorepo', 'Multirepo']),
                    ('Contribution strategies', ['Team programming', 'Branch-pull'])
                ],
                [
                    ('OOP', 'Object Oriented Programming'),
                    ('OOD', 'Object Oriented Design'),
                    ('DDD', 'Domain-Driven Design'),
                    ('TDD', 'Test-Driven Design'),
                    ('BDD', 'Behavior-Driven Development'),
                    ('CI/CD', 'Continuous Integration / Continuous Deployment')
                ]
            ]
        }
    },
    'employment': [
        {
            'firm': 'OLX',
            'job': 'Acting staff engineer',
            'time': [
                ['2018-03']
            ],
            'desc': [
                'Driving and guiding multiple initiatives, keeping alignment and long-term architecture vision in sync. Keeping close collaboration and shared understanding between product and engineering on short and long term projects. Promoting good practices and mentoring engineers into new positions.',
                'Member of "Architecture Committee" and "Unification Team", tech lead of multiple initiatives.'
            ]
        },
        {
            'firm': 'Vimcar',
            'job': 'Senior software engineer',
            'time': [
                ['2015-10', '2018-01']
            ],
            'desc': [
                'Built a distributed system that can process extensive streams of data for a constantly growing number of users.',
                'Event-based communication, event store and integration with different systems (IoT).'
            ]
        },
        {
            'firm': 'Rocket Internet - Core',
            'job': 'Senior software engineer',
            'time': [
                ['2014-06', '2015-10']
            ],
            'desc': [
                'Built several systems for global startups.',
                'Developed extendable base platform, multiple additional packages for future ventures.'
            ]
        },
        {
            'firm': 'TNN Finance',
            'job': 'Senior software engineer',
            'time': [
                ['2012-07', '2014-05']
            ],
            'desc': [
                'Mentoring and introducing good practices into developement team of on-line exchange platform. Introducing Event-Sourcing concepts into accounting system.',
                'The application had to process exchange rates coming from different sources in close to real time for calculating customer fees and reporting.'
            ]
        },
        {
            'firm': 'Caritas Polska',
            'job': 'Senior software engineer',
            'time': [
                ['2007-01', '2013-12'],
                ['2011-12', '2012-02']
            ],
            'desc': [
                'Built several applications supporting resource planning for nationwide charity actions and data analysis.',
                'Low-traffic applications with large amounts of analytical data, customizable reporting for specific target-user group.'
            ]
        },
        {
            'firm': 'BEST IT Solutions INC.',
            'job': 'Software engineer',
            'time': [
                ['2010-10', '2012-11']
            ],
            'desc': [
                'Started as effort to bring inherited codebase up to date - refactoring &amp; introducing multiple layers of tests.',
                'With growing popularity, shifted into scaling system to match new levels of traffic.'
            ]
        },
        {
            'firm': 'Malachowski',
            'job': 'Senior software engineer &amp; team leader',
            'time': [
                ['2009-04', '2010-01']
            ],
            'desc': [
                'Designed and built system for tracking and managing tailoring production processes.',
                'Integration with additional services &amp; software like: accounting, multi-warehouse management tools, sewing and cutting machines. on-line shops etc.'
            ]
        },
        {
            'firm': 'Telekam',
            'job': 'Software engineer',
            'time': [
                ['2006-01', '2007-12']
            ],
            'desc': [
                'Developed two connected systems: accounting and access control for local ISP - where accounting system regulated access to broadband connection of ISP customers.'
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
            'polish': (
                'Technik',
                'Nothing special, but I like the sound of it.'
            ),
            'school': 'Zespol Szkol Technicznych i Ogolnoksztalcacych (ZSTiO)',
            'desc': [
                'Received technician\'s degree, specialization in electrotechnics, automatics and industrial robotics.'
            ]
        }
    ]
}


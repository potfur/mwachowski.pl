# -*- coding: utf-8 -*-

from datetime import datetime

content = {
    'title': {
        'name': 'Michal',
        'family': 'Wachowski',
        'job': 'software engineer & architect',
        'location': None
    },
    'contact': {
        'personal': 'https://mwachowski.pl',
        'linkedin': 'https://www.linkedin.com/in/michal-wachowski/',
        'github': 'https://github.com/potfur/',
        'mail': 'wachowski.michal@gmail.com',
        'tel': '+491724795137',
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
                    ('Containerisation', ['Docker', 'OCI', 'Terraform', 'K8S'])
                ]
            ]
        },
        'methods': {
            'title': 'Methodologies, ways of working',
            'nodes': [
                [
                    (
                        'System design',
                        ['Domain models', 'Bounded Contexts', 'Contracts', 'Communication', 'Performance', 'Product alignment', 'Security']
                    ),
                    (
                        'Architecture',
                        ['Microservices', 'Monoliths', 'Archipelago', 'Distributed', 'Event-Driven', 'Event-Sourcing',
                         'CQRS', 'Hexagonal', 'Layered', 'IoT']
                    ),
                    (
                        'Workflows',
                        ['Monorepo', 'Multirepo', 'Ensemble Programming', 'Branching', 'Trunk-Based']
                    ),
                    (
                        'Mentoring',
                        ['1-on-1', 'Workshops', 'Pair Programming']
                    )
                ],
                [
                    ('OOP', 'Object Oriented Programming'),
                    ('OOD', 'Object Oriented Design'),
                    ('DDD', 'Domain-Driven Design'),
                    ('TDD', 'Test-Driven Design'),
                    ('BDD', 'Behavior-Driven Development'),
                ]
            ]
        }
    },
    'employment': [
        {
            'firm': 'Cardino',
            'job': 'Software engineer',
            'time': [
                ['2024-12']
            ],
            'desc': [
                'Foster a rapid and adaptive engineering culture focused on testability and fast delivery.',
                'Implement Domain-Driven Design (DDD) practices to formalize business processes and transform into no-code, low-code, or full-code solutions.',
                'Enable and educate engineers to enhance their skills and productivity.',
                'Provide hands-on support and guidance in daily engineering tasks.'
            ]
        },
        {
            'firm': 'OLX Group',
            'job': 'Acting staff engineer',
            'time': [
                ['2018-03', '2024-09']
            ],
            'desc': [
                'Co-drove transactional expansion across multiple markets, contributing to system design and domain models.',
                'Lead role in cross-team initiatives to consolidate products and ecosystems over major markets.',
                'Influenced engineering culture by promoting good practices and mentoring engineers.',
                'Improved stability and performance with 2.2 million checkouts across multiple markets, P95 of ~200ms.',
                'Increased delivery speed - highest DORA classification (High Performers - 2024), with 10+ deployments per day, change failure below 4% and lead time to change under 3 hours.',
                'Simplified codebase, monitoring, and alerting with shared infrastructure components and tooling, promoting best practices for testing, observability, and security.',
                'Shaped company-wide engineering and product decision-making processes.',
                'Supported multiple teams in tackling challenges through enabling and hands-on participation.',
                'Acted as a trusted partner for stakeholders outside of engineering, such as legal, product, and design.',
                'Member of Architectural Committee, defining large scale, long term architectural evolution of OLX ecosystem.'
            ]
        },
        {
            'firm': 'Vimcar',
            'job': 'Senior software engineer',
            'time': [
                ['2015-10', '2018-01']
            ],
            'desc': [
                'Co-designed distributed system for processing large event streams (IoT).',
                'Key role in introducing domain modeling practices and leading shaping domain models.',
                'Introduced code-derived living documentation.'
            ]
        },
        {
            'firm': 'Rocket Internet - Core',
            'job': 'Senior software engineer',
            'time': [
                ['2014-06', '2015-10']
            ],
            'desc': [
                'Significant role in defining the architecture of modular platform for rapid venture development.',
                'Influenced and improved team practices in delivering fully tested and robust solutions.',
                'Lead role in developing multiple key modules intended for ease of localization and ease of development.',
            ]
        },
        {
            'firm': 'TNN Finance',
            'job': 'Senior software engineer',
            'time': [
                ['2012-07', '2014-05']
            ],
            'desc': [
                'Improved engineering culture by introducing pair programming, promoting good practices, and mentorship.',
                'Led introduction and development of event-sourcing concepts in transactional systems.',
                'Had a key role in designing and later developing of close-to-realtime calculations engine.',
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
                'Drove design of a country-wide systems for managing charity actions and warehousing.',
                'Influenced shaping of analytical systems, and customization of reporting for decision-making processes.',
                'Defined long-term vision for built systems and their evolution.',
            ]
        },
        {
            'firm': 'BEST IT Solutions INC.',
            'job': 'Software engineer',
            'time': [
                ['2010-10', '2012-11']
            ],
            'desc': [
                'Led initiative of refactoring legacy system, focused on improving and preparing existing codebase for future development.',
                'Influenced re-design of architecture to improve its scalability so it meets high-traffic demands.'
            ]
        },
        {
            'firm': 'Malachowski',
            'job': 'Senior software engineer &amp; team leader',
            'time': [
                ['2009-04', '2010-01']
            ],
            'desc': [
                'Drove modeling and later architectural design of a system for tracking and managing tailoring production.',
                'Leading role in aligning multiple (remote) teams and initiatives.',
                'Influenced integration of external systems (accounting, warehousing, shops, sewing, and cutting machines) with the main platform.'
            ]
        },
        {
            'firm': 'Telekam',
            'job': 'Software engineer',
            'time': [
                ['2006-01', '2007-12']
            ],
            'desc': [
                'Designed and developed interconnected systems for accounting and managing access to broadband connection for local ISP.',
            ]
        },
        {
            'firm': 'TEB',
            'job': 'Lecturer',

            'time': [
                ['2000-09', '2001-02']
            ],
            'desc': [
                'Led course about basics of information and communications technologies.'
            ]
        }
    ],
    'education': [
        {
            'degree': 'Engineer\'s degree',
            'school': 'WISZ',
            'desc': [
                'Type of studies: full time, engineering, majoring in system administration.',
            ]
        },
        {
            'degree': 'Technician\'s degree',
            'school': 'ZSTiO',
            'desc': [
                'Received a technician\'s degree, specialization in electrotechnics, automatics, and industrial robotics.'
            ]
        }
    ]
}


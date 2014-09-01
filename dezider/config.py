INSTALLED_PLUGINS = (
    'brutal.plugins.basic',
    # 'brutal.plugins.logging',
)

BOTS = [
    # bot 1
    {
        'nick': 'dezider',
        'connections': [
            # connect to multiple networks
            # {
            #     'protocol': 'xmpp',
            #     'log_traffic': True,
            #     'server': 'localhost', # server to connect to
            #     'port': 5222, # default
            #     'use_ssl': True,  # default for jabber
            #     'keepalive_freq': '15', # default
            #     'jabber_id':'bot@server', # depends on the server...
            #     'password': '', # jabber_id password
            #     'room_nick': 'bot', # nick to use in rooms, if not given, defaults to bot nick
            #     'rooms': ['room@conference.server', ('private_room@conference.server', 'pass')]
            # },
            {
                'protocol': 'irc',
                'server': 'irc.freenode.net',
                'port': 6667,
                'use_ssl': False,
                'password': '',
                'channels': ['#xlcteam']
            }
        ],
        'enabled_plugins': {
            # 'plugin_one': {},
            # 'dezider.plugins.example': {
            #   'id': 1,
            #   'name': 'John',
            #   'surename': 'Doe',
            #   'nick': 'jdoe'
            # }
        },  # if this isn't set, load all
        'plugin_settings': {}
    },
    # bot 2
    # {
    #     'nick': 'tester',
    #     'connections': [
    #         {
    #             'protocol': 'irc',
    #             'server': 'irc.localhost',
    #             'port': 6667,
    #             'use_ssl': False, # default or irc
    #             'password': '',
    #             'channels': ['#room', ('#private_room', 'pass')]
    #         }
    #     ],
    #     'plugin_settings': {},
    #     'command_token': '.'
    # }
]

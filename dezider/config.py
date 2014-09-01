INSTALLED_PLUGINS = (
    'brutal.plugins.basic',
    # 'brutal.plugins.logging',
)

BOTS = [
    {
        'nick': 'dezider',
        'connections': [
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
]

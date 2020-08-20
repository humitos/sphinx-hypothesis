import json


def add_js_files(app, config, **kwargs):
    app.add_js_file(None, **{
        'type': 'application/json',
        'class': 'js-hypothesis-config',
        'body': json.dumps(app.config.hypothesis_config),
    })
    app.add_js_file('https://hypothes.is/embed.js', **{'async': 'async'})


def setup(app):
    app.add_config_value('hypothesis_config', {}, 'html')

    # Add the JS files inside ``config-inited`` event to have access to
    # ``hypothesis_config`` defined by the user
    app.connect('config-inited', add_js_files)

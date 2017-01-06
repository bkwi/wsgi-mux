import hug


@hug.get('/')
def hello():
    return {'hello': 'hug'}

from flask import Response, render_template, json, jsonify


def _to_json(obj):
    obj['permalink'] = '/{}/json'.format(obj.get('permalink'))
    return jsonify(**json.loads(json.htmlsafe_dumps(obj)))


def _to_text(message):
    return Response(message, content_type='text/plain')


def _to_html(obj):
    return render_template('index.html', **obj)


def create_response(rtype=None, **kwargs):
    options = {
        'json': _to_json(kwargs),
        'html': _to_html(kwargs),
        'txt': _to_text(kwargs.get('message'))
    }

    return options.get(rtype, options.get('html'))

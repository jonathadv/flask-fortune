from flask import Response, render_template, json, jsonify


def _to_json(obj):
    obj['permalink'] = '/{}/json'.format(obj.get('permalink'))
    return jsonify(**json.loads(json.htmlsafe_dumps(obj)))


def _to_text(obj):
    return Response(obj.get('message'), content_type='text/plain')


def _to_html(obj):
    print('########## called')
    return render_template('index.html', **obj)


def create_response(rtype=None, **kwargs):
    options = {
        'json': _to_json,
        'html': _to_html,
        'txt': _to_text
    }

    return options.get(rtype, options.get('html'))(kwargs)

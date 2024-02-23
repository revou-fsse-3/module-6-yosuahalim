from flask import jsonify


def api_response(data=None, status_code=200, message=""):
    return (
        jsonify(
            {
                "data": data,
                "status": {"message": message, "status_code": status_code},
            }
        ),
        status_code,
    )

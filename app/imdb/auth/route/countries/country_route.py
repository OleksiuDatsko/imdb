import logging
from http import HTTPStatus

from flask import Blueprint, Response, request, make_response

country_bp = Blueprint("countries", __name__, url_prefix="/countries/")


@country_bp.get("")
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response("smt", HTTPStatus.OK)

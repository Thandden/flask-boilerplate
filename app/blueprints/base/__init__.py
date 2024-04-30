from flask import Blueprint

base = Blueprint("base", __name__, url_prefix="/", template_folder="templates")

from . import routes  # type: ignore

from flask import Blueprint
from flask import redirect, request


bp = Blueprint('admin', __name__)

@bp.before_request
def restrict_bp_to_admins():
    print 'middle'
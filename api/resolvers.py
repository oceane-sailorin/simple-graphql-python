from ariadne import convert_kwargs_to_snake_case
from datetime import datetime
from api import create_app, db

from .models import Resident


def resolve_residents(obj, info):
    try:
        residents = [resident.resident_to_dict() for resident in Resident.query.all()]
        payload = {
            "success": True,
            "residents": residents
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_resident(obj, info, resident_id):
    try:
        resident = Resident.query.get(resident_id)
        payload = {
            "success": True,
            "resident": resident.resident_to_dict()
        }

    except AttributeError:  # resident not found
        payload = {
            "success": False,
            "errors": [f"Resident with id {resident_id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_create_resident(obj, info, name, age, installed, installation_date):
    try:
        installation_date = datetime.strptime(installation_date, '%d-%m-%Y').date()
        resident = Resident(
            name=name, age=age, installed=installed, installation_date=installation_date
        )
        db.session.add(resident)
        db.session.commit()
        payload = {
            "success": True,
            "resident": resident.resident_to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided."
                       f"Format = dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_installed_resident(obj, info, resident_id):
    try:
        resident = Resident.query.get(resident_id)
        resident.installed = True
        db.session.add(resident)
        db.session.commit()
        payload = {
            "success": True,
            "resident": resident.resident_to_dict()
        }
    except AttributeError:  # resident not found
        payload = {
            "success": False,
            "errors":  [f"Resident with id {resident_id} was not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_resident(obj, info, resident_id):
    try:
        resident = Resident.query.get(resident_id)
        db.session.delete(resident)
        db.session.commit()
        payload = {"success": True}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Resident with id {resident_id} not found"]
        }

    return payload



@convert_kwargs_to_snake_case
def resolve_update_age_resident(obj, info, resident_id, new_age):
    try:
        resident = Resident.query.get(resident_id)
        if resident:
            resident.age = new_age
        db.session.add(resident)
        db.session.commit()
        payload = {
            "success": True,
            "resident": resident.resident_to_dict()
        }

    except AttributeError:  # resident not found
        payload = {
            "success": False,
            "errors": [f"Resident with id {resident_id} not found"]
        }
    return payload

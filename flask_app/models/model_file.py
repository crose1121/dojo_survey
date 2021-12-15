from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_input(data):
        is_valid = True
        if len(data['name']) > 255:
            is_valid = False
            flash("Name is too long")
        if len(data['name']) < 2:
            is_valid = False
            flash("Name is too short")
        if data['location'] == "Value":
            flash("Select a location")
            is_valid = False
        if data['language'] == "Value":
            flash("Select a language!")
            is_valid = False

        return is_valid

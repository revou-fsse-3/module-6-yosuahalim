from flask import Blueprint

pokemon_blueprint = Blueprint("pokemon", __name__)


@pokemon_blueprint.route("/<pokemon_id>", methods=["GET"])
def pokemon(pokemon_id):
    return {"message": f"{pokemon_id}"}

from api import create_app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.resolvers import resolve_residents, resolve_resident, resolve_create_resident, \
    resolve_installed_resident, resolve_delete_resident, resolve_update_age_resident


query = ObjectType("Query")
query.set_field("residents", resolve_residents)
query.set_field("resident", resolve_resident)

mutation = ObjectType("Mutation")
mutation.set_field("createResident", resolve_create_resident)
mutation.set_field("installedResident", resolve_installed_resident)
mutation.set_field("deleteResident", resolve_delete_resident)
mutation.set_field("updateAgeResident", resolve_update_age_resident)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

app = create_app()
#app.app_context().push() 


@app.route('/')
def welcome():
    return 'Welcome to our residence!'


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

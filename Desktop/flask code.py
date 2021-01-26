from flask import Flask, jsonify

justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/justice-league")
def justice_league():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)


@app.route("/")
def welcome():
    return (
        f"Welcome to the Justice League API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/justice-league<br/>"
        f"/api/v1.0/justice-league/real-name/SUPERHERO_REAL_NAME<br/>"
        f"/api/v1.0/justice-league/superhero-name/SUPERHERO_NAME"
    )


@app.route("/api/v1.0/justice-league/real-name/<real_name>")
def justice_league_by_real_name(real_name):
    """Fetch the Justice League character whose real_name matches
       the path variable supplied by the user, or a 404 if not."""

    search_term = real_name.replace(" ", "").lower()
    for character in justice_league_members:
        real_name_lowered = character["real_name"].replace(" ", "").lower()

        if real_name_lowered == search_term:
            return jsonify(character)

    return jsonify({"error": f"Character with real_name {real_name} not found."}), 404


@app.route("/api/v1.0/justice-league/superhero-name/<superhero>")
def justice_league_by_superhero_name(superhero):
    """Fetch the Justice League character whose superhero matches
       the path variable supplied by the user, or a 404 if not."""

    search_term = superhero.replace(" ", "").lower()
    for character in justice_league_members:
        hero_name_lowered = character["superhero"].replace(" ", "").lower()

        if hero_name_lowered == search_term:
            return jsonify(character)

    return jsonify({"error": "Character not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)

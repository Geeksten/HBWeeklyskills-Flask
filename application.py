from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    #return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route("/application-form")
def show_form():
    """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name?
          <input type="text" name="person">
          <input type="submit">
        </form>
      </body>
    </html>
    """
    return render_template("application-form.html")


@app.route("/application-response")
def handle_submission():
    """Handles submission of a form in application-form.html to/application.

        Gets the first name, last name, salary, and job title from the request.

        Returns a response that acknowledges their application.
        This should repeat their name, title, and salary requirement, like:

        "Thank you, Jessica McHackbright, for applying to be a QA Engineer. Your
        minimum salary requirement is 89000 dollars."


    """
    applicant_firstname = request.args.get("firstname")
    applicant_lastname = request.args.get("lastname")
    salary_requirement = request.args.get("salary")
    position_applied_for = request.args.get("position")

    return render_template("application-response.html", firstname=applicant_firstname,
                           lastname=applicant_lastname, salary=salary_requirement,
                           position=position_applied_for)

if __name__ == "__main__":
    app.run(debug=True)

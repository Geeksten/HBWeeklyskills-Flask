from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    #return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    return render_template("index.html")


@app.route("/application-form")
def show_form():
    #return <"application-form.html">
    """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <!--<link rel="stylesheet" type="text/css" href="styles.css">-->
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}" />
        <title>Skills-HTML-CSS</title>

    </head>
    <body>
        <!-- your html goes here -->
        <div>
            <h1 class="brand">Melon Debuggers Inc</h1>
            <h2>Employment Application</h2>
        </div>
        <div id="testimg">
            <img src="http://previews.123rf.com/images/icetray/icetray1203/icetray120306962/12731424-Word-on-keyboard-made-in-3D-Stock-Photo-testing-software-computer.jpg" alt="Image of Test Button" width="128" height="350">
        </div>
        <div id="instruction">
            <p>Melon Debuggers is looking for Software designers to help write Doctests for our clients. </p>
            <p>The ideal candidate will be a selfstarter, not afraid to use Google or Stackoverflow and Python docs for reference and ready to live and breathe about melons.</p>
        </div>
        <br>
        <div id="jobapplication">
            <form action="/application-form" method="POST">
            <label for="firstname">First name *
                <input type="text" name="firstname" id="inputback">
            <br><br>
            <label for="lastname">Last name *
                <input type="text" name="lastname" class="lastname" id="inputback">
            <br><br>
            <label for="salary">Salary *
                <input type="text" pattern="[0-9]*" name="salary" id="inputback">
            <br><br>
            <label for="position">Position applied for? *
                 <select name="position" id="inputback">
                      <option value="software engineer">Software Engineer</option>
                      <option value="qa engineer">QA Engineer</option>
                      <option value="product manager">Product Manager</option>
                </select>
            <br><br>
            <input type="submit" name="submit" value="Submit" id="submit">
            </form>
        </div>
    </body>
</html>
    """
    return render_template("application-form.html")


@app.route("/application", methods=['GET', 'POST'])
def application_response_page():
    """Handles submission of a form in application-form.html to/application.

        Gets the first name, last name, salary, and job title from the request.

        Returns a response that acknowledges their application.
        This should repeat their name, title, and salary requirement, like:

        "Thank you, Jessica McHackbright, for applying to be a QA Engineer. Your
        minimum salary requirement is 89000 dollars."
    """
    applicant_firstname = request.args.get("firstname")
    applicant_lastname = request.args.get("lastname")
    position_applied_for = request.args.get("position")
    salary_requirement = request.args.get("salary")

    return render_template('application-response.html', firstname=applicant_firstname,
                           lastname=applicant_lastname, position=position_applied_for,
                           salary=salary_requirement)

    # applicant_firstname = request.args.get("firstname")
    # applicant_lastname = request.args.get("lastname")
    # salary_requirement = request.args.get("salary")
    # position_applied_for = request.args.get("position")

    # return render_template("application-response.html", firstname=applicant_firstname,
    #                        lastname=applicant_lastname, salary=salary_requirement,
    #                        position=position_applied_for)

if __name__ == "__main__":
    app.run(debug=True)

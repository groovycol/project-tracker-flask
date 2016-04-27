from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/newstudent")
def new_student():
    """Show a form for adding a new student"""

    return render_template("add_student.html")


@app.route("/studentadd", methods=["POST"])
def student_add():
    """Add a student to the database"""

    print "I am here!"
    first = request.form.get('fname')
    last  = request.form.get('lname')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

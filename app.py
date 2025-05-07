from flask import Flask, render_template

app = Flask(__name__)

name = "SMI Institute of Information Technology"


@app.route("/")
def index():
  return render_template("index.html",
                         title="Home",
                         year="2025",
                         designer=name)


@app.route("/about")
def about():
  return render_template("about.html",
                         title="About Us",
                         year="2025",
                         designer=name)


@app.route("/contact")
def contact():
  return render_template("contact.html",
                         title="Contact Us",
                         year="2025",
                         designer=name)


@app.route("/tech-updates")
def techupdates():
  return render_template("techupdate.html",
                         title="Tech Updates",
                         year="2025",
                         designer=name)


@app.route("/courses")
def all_courses():
  return render_template("courses.html",
                         title="Our Courses",
                         year="2025",
                         designer=name)


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5000)

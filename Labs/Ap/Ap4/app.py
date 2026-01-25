from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<h2>API Webform</h2>
<form method="POST">
  <label>Naam:</label><br>
  <input type="text" name="name"><br><br>

  <label>Email:</label><br>
  <input type="email" name="email"><br><br>

  <label>Opleiding:</label><br>
  <select name="course">
    <option value="DevNet">DevNet</option>
    <option value="Networking">Networking</option>
    <option value="Automation">Automation</option>
  </select><br><br>

  <label>Bericht:</label><br>
  <textarea name="message" rows="4" cols="40"></textarea><br><br>

  <input type="submit" value="Verstuur">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")
        message = request.form.get("message")

        return f"""
        <h3>Ontvangen gegevens</h3>
        Naam: {name}<br>
        Email: {email}<br>
        Opleiding: {course}<br>
        Bericht: {message}
        """

    return HTML_FORM

if __name__ == "__main__":
    app.run(debug=True)

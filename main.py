
from flask import Flask, render_template, request
from dfa import PasswordDFA
from password_rules import PasswordRules

app = Flask(__name__)

dfa = PasswordDFA()


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        password = request.form.get("password", "")

        result = dfa.validate(password)

        result["rules"] = PasswordRules.get_rules(password)

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)

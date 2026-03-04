from flask import Flask, render_template, jsonify
from content import DAYS

app = Flask(__name__)


@app.route("/")
def index():
    phases = [
        {"number": 1, "title": "Foundation", "days": "1-7", "goal": "Get comfortable with Python basics. Write retry logic from memory by Day 7."},
        {"number": 2, "title": "Core Patterns", "days": "8-14", "goal": "Learn DFS traversal and practice the full interview problem end to end."},
        {"number": 3, "title": "Interview Simulation", "days": "15-20", "goal": "Polish, speed up, and simulate real interview conditions."},
    ]
    return render_template("index.html", days=DAYS, phases=phases)


@app.route("/day/<int:day_num>")
def day(day_num):
    if day_num < 1 or day_num > 20:
        return "Day not found", 404
    day_data = DAYS[day_num - 1]
    prev_day = day_num - 1 if day_num > 1 else None
    next_day = day_num + 1 if day_num < 20 else None
    return render_template("day.html", day=day_data, prev_day=prev_day, next_day=next_day)


@app.route("/api/days")
def api_days():
    return jsonify([{"day": d["day"], "title": d["title"], "phase": d["phase"]} for d in DAYS])


if __name__ == "__main__":
    import os
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=debug, host="0.0.0.0", port=port)

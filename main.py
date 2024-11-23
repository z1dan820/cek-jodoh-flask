from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary pasangan zodiak yang cocok (semua huruf kecil untuk normalisasi)
compatibility = {
    "aries": ["Leo", "Sagittarius"],
    "taurus": ["Virgo", "Capricorn"],
    "gemini": ["Libra", "Aquarius"],
    "cancer": ["Scorpio", "Pisces"],
    "leo": ["Aries", "Sagittarius"],
    "virgo": ["Taurus", "Capricorn"],
    "libra": ["Gemini", "Aquarius"],
    "scorpio": ["Cancer", "Pisces"],
    "sagittarius": ["Aries", "Leo"],
    "capricorn": ["Taurus", "Virgo"],
    "aquarius": ["Gemini", "Libra"],
    "pisces": ["Cancer", "Scorpio"]
}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ambil input user dan normalisasi ke huruf kecil
        user_zodiac = request.form.get("zodiac").strip().lower()
        # Cari pasangan zodiak dengan kunci yang sesuai
        matches = compatibility.get(user_zodiac, ["Tidak ditemukan"])
        # Format ulang zodiak agar tampilannya tetap rapi (capitalize)
        formatted_zodiac = user_zodiac.capitalize() if user_zodiac in compatibility else user_zodiac
        return render_template("index.html", zodiac=formatted_zodiac, matches=matches)
    return render_template("index.html", zodiac=None, matches=None)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask 
import random

app = Flask(__name__)

tech_fact = ['Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja',
             'Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan',
             'Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka']
joke_show = ['What do you call an angry carrot? A setamed veggie🥕', 'What’s red and bad for your teeth? A brick🧱', 'Why was the fish’s grades bad? They were below sea level🐟', 'Why do seagulls fly over the sea? If they flew over the bay,they would be bagels🥯']

@app.route("/")
def hello_world():
    return '<h1>Hello, World! <a href="/joke_show">View funny jokes</a></h1>'
@app.route("/joke_show")
def jokeshow():
    return f'<p>{random.choice(joke_show)}</p>'

app.run(debug=True)


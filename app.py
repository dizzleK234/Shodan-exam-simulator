from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Technique lists
tachi_waza = [
    "Seoi-nage", "Ippon-seoi-nage", "Tai-otoshi", "Kata-guruma", "Sukui-nage",
    "Uki-otoshi", "Sumi-otoshi", "Uki-goshi", "O-goshi", "Koshi-guruma",
    "Tsurikomi-goshi", "Harai-goshi", "Tsuri-goshi", "Hane-goshi",
    "Utsuri-goshi", "Ushiro-goshi", "De-ashi-harai", "Hiza-guruma",
    "Sasae-tsurikomi-ashi", "O-soto-gari", "O-uchi-gari", "Ko-soto-gari",
    "Ko-uchi-gari", "Okuri-ashi-harai", "Uchi-mata", "Ko-soto-gake",
    "Ashi-guruma", "Harai-tsurikomi-ashi", "O-guruma", "O-soto-guruma",
    "Tomoe-nage", "Sumi-gaeshi", "Ura-nage", "Yoko-otoshi", "Tani-otoshi",
    "Hane-makikomi", "Soto-makikomi", "Uki-waza", "Yoko-wakare", "Yoko-guruma",
    "Yoko-gake"
]

ne_waza = [
    "Kesa-gatame", "Kata-gatame", "Kuzure-kami-shiho-gatame",
    "Yoko-shiho-gatame", "Tate-shiho-gatame", "Kuzure-kesa-gatame",
    "Kami-shiho-gatame", "Nami-juji-jime", "Gyaku-juji-jime", "Kata-juji-jime",
    "Hadaka-jime", "Okuri-eri-jime", "Kata-ha-jime", "Ude-garami",
    "Ude-hishigi-juji-gatame", "Ude-hishigi-ude-gatame",
    "Ude-hishigi-hiza-gatame", "Ude-hishigi-waki-gatame",
    "Ude-hishigi-hara-gatame"
]

tachi_links = {
    "Seoi-nage": "https://youtu.be/zIq0xI0ogxk",
    "Ippon-seoi-nage": "https://youtu.be/FQnOlCxo4oI",
    "Tai-otoshi": "https://youtu.be/4x6S3Q-Ktv8",
    "Kata-guruma": "https://youtu.be/cnHRhSy8yi4",
    "Sukui-nage": "https://youtu.be/vU6aJ2kFxoI",
    "Uki-otoshi": "https://youtu.be/6H5tmncOY4Q",
    "Sumi-otoshi": "https://youtu.be/lLU9wv52ni0",
    "Uki-goshi": "https://youtu.be/bPKwtB4lyOQ",
    "O-goshi": "https://youtu.be/yhu1mfy2vJ4",
    "Koshi-guruma": "https://youtu.be/SU7Id6uVJ44",
    "Tsurikomi-goshi": "https://youtu.be/McfzA0yRVt4",
    "Harai-goshi": "https://youtu.be/qTo8HlAAkOo",
    "Tsuri-goshi": "https://youtu.be/51Htlp7xEvE",
    "Hane-goshi": "https://youtu.be/M9_7De6A1kk",
    "Utsuri-goshi": "https://youtu.be/4pQd_bEnlf0",
    "Ushiro-goshi": "https://youtu.be/ORIYstuxYT8",
    "De-ashi-harai": "https://youtu.be/4BUUvqxi_Kk",
    "Hiza-guruma": "https://youtu.be/JPJx9-oAVns",
    "Sasae-tsurikomi-ashi": "https://www.youtube.com/watch?v=699i--pvYmE",
    "O-soto-gari": "https://www.youtube.com/watch?v=c-A_nP7mKAc",
    "O-uchi-gari": "https://youtu.be/0itJFhV9pDQ",
    "Ko-soto-gari": "https://youtu.be/jeQ541ScLB4",
    "Ko-uchi-gari": "https://youtu.be/3Jb3tZvr9Ng",
    "Okuri-ashi-harai": "https://youtu.be/nw1ZdRjrdRI",
    "Uchi-mata": "https://youtu.be/iUpSu5J-bgw",
    "Ko-soto-gake": "https://youtu.be/8b6kY4s4zH4",
    "Ashi-guruma": "https://youtu.be/ROeayhvom9U",
    "Harai-tsurikomi-ashi": "https://youtu.be/gGPXvWL8VbE",
    "O-guruma": "https://youtu.be/SnZciTAY9vc",
    "O-soto-guruma": "https://youtu.be/92KbCm6pQeI",
    "Tomoe-nage": "https://youtu.be/880WbHvHv6A",
    "Sumi-gaeshi": "https://youtu.be/5VhduA5xkbA",
    "Ura-nage": "https://youtu.be/Fgi9b8DJ5sQ",
    "Yoko-otoshi": "https://youtu.be/MnNG67pF_a0",
    "Tani-otoshi": "https://youtu.be/3b9Me3Fohpk",
    "Hane-makikomi": "https://youtu.be/6CRBGLGz9j8",
    "Soto-makikomi": "https://youtu.be/bWG9O1BVKtQ",
    "Uki-waza": "https://youtu.be/weVOpJ63gII",
    "Yoko-wakare": "https://youtu.be/bp1tscHlePI",
    "Yoko-guruma": "https://youtu.be/MehP6I5cY2c",
    "Yoko-gake": "https://youtu.be/tP1Sj1uDfSo",
}

ne_links = {
    "Kesa-gatame": "https://youtu.be/NDaQuJOFBYk",
    "Kata-gatame": "https://youtu.be/zQR3IOXxO_Q",
    "Kuzure-kami-shiho-gatame": "https://youtu.be/YUrogQWdwiY",
    "Yoko-shiho-gatame": "https://youtu.be/TT7XJVSEQxA",
    "Tate-shiho-gatame": "https://youtu.be/55-rFmBx53g",
    "Kuzure-kesa-gatame": "https://youtu.be/Q2fb9jaoUFQ",
    "Kami-shiho-gatame": "https://youtu.be/HFuMjOv0WN8",
    "Nami-juji-jime": "https://youtu.be/k2cHry9HByQ",
    "Gyaku-juji-jime": "https://youtu.be/t3tQriIPdlI",
    "Kata-juji-jime": "https://youtu.be/3VZVUAmiMD8",
    "Hadaka-jime": "https://youtu.be/9f0n8jez7iA",
    "Okuri-eri-jime": "https://youtu.be/EiqyoVcIAi8",
    "Kata-ha-jime": "https://youtu.be/yaTGgRjnwB8",
    "Ude-garami": "https://youtu.be/AIlTvZb4RlE",
    "Ude-hishigi-juji-gatame": "https://youtu.be/OWgSOlCuMXw",
    "Ude-hishigi-ude-gatame": "https://youtu.be/SBf0aTma1VI",
    "Ude-hishigi-hiza-gatame": "https://youtu.be/H2HtAJdiJcE",
    "Ude-hishigi-waki-gatame": "https://youtu.be/8F5p1zuJRG0",
    "Ude-hishigi-hara-gatame": "https://youtu.be/ZzEycg8R_9M",
}


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/choose', methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':
        return render_template('choose.html')
    return render_template('choose.html')


@app.route('/results', methods=['POST'])
def results():
    num_tachi = int(request.form['num_tachi'])
    num_ne = int(request.form['num_ne'])

    selected_tachi = random.sample(tachi_waza, num_tachi)
    selected_ne = random.sample(ne_waza, num_ne)
    tachi_with_links = [(tech, tachi_links.get(tech, "#"))
                        for tech in selected_tachi]
    ne_with_links = [(tech, ne_links.get(tech, "#")) for tech in selected_ne]

    return render_template('results.html',
                           tachi=tachi_with_links,
                           ne=ne_with_links)

@app.route('/flashcards', methods=['GET', 'POST'])
def flashcards():
    if request.method == 'POST':
        selected = request.form.getlist('techniques')
        return render_template('flashcards_play.html', techniques=selected)
    return render_template('flashcards_select.html', tachi=tachi_waza, ne=ne_waza)


@app.route('/flashcards/play', methods=['POST'])
def flashcards_play():
    techniques = request.form.getlist('techniques')
    if techniques:
        current = techniques[0]
        remaining = techniques[1:]
        
        # Find the correct link
        link = tachi_links.get(current) or ne_links.get(current)
        
        return render_template('flashcards_play.html',
                               current=current,
                               link=link,
                               techniques=remaining)
    else:
        return render_template('flashcards_play.html', techniques=[])


@app.route('/quiz')
def quiz():
    all_moves = list(tachi_links.keys()) + list(ne_links.keys())
    correct_move = random.choice(all_moves)
    options = random.sample(all_moves, 4) + [correct_move]
    random.shuffle(options)

    # find which link it belongs to
    if correct_move in tachi_links:
        video_link = tachi_links[correct_move]
    else:
        video_link = ne_links[correct_move]

    # get YouTube video ID
    video_id = video_link.split('v=')[-1]

    return render_template('quiz.html', video_id=video_id, correct_move=correct_move, options=options)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

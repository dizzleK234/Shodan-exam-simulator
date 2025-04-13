from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session tracking

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


# Categories for flashcards
categories = {
    "TE-WAZA": ["Seoi-nage", "Ippon-seoi-nage", "Tai-otoshi", "Kata-guruma", "Sukui-nage", "Uki-otoshi", "Sumi-otoshi"],
    "KOSHI-WAZA": ["Uki-goshi", "O-goshi", "Koshi-guruma", "Tsurikomi-goshi", "Harai-goshi", "Tsuri-goshi", "Hane-goshi", "Utsuri-goshi", "Ushiro-goshi"],
    "ASHI-WAZA": ["De-ashi-harai", "Hiza-guruma", "Sasae-tsurikomi-ashi", "O-soto-gari", "O-uchi-gari", "Ko-soto-gari", "Ko-uchi-gari", "Okuri-ashi-harai", "Uchi-mata", "Ko-soto-gake", "Ashi-guruma", "Harai-tsurikomi-ashi", "O-guruma", "O-soto-guruma"],
    "MASUTEMI-WAZA": ["Tomoe-nage", "Sumi-gaeshi", "Ura-nage"],
    "YOKO-SUTEMI-WAZA": ["Yoko-otoshi", "Tani-otoshi", "Hane-makikomi", "Soto-makikomi", "Uki-waza", "Yoko-wakare", "Yoko-guruma", "Yoko-gake"],
    "OSAEKOMI-WAZA": ["Kesa-gatame", "Kata-gatame", "Kuzure-kami-shiho-gatame", "Yoko-shiho-gatame", "Tate-shiho-gatame", "Kuzure-kesa-gatame", "Kami-shiho-gatame"],
    "SHIME-WAZA": ["Nami-juji-jime", "Gyaku-juji-jime", "Kata-juji-jime", "Hadaka-jime", "Okuri-eri-jime", "Kata-ha-jime"],
    "KANSETSU-WAZA": ["Ude-garami", "Ude-hishigi-juji-gatame", "Ude-hishigi-ude-gatame", "Ude-hishigi-hiza-gatame", "Ude-hishigi-waki-gatame", "Ude-hishigi-hara-gatame"]
}

# Flashcards Routes
@app.route('/flashcards', methods=['GET'])
def flashcards():
    return render_template('flashcards_select.html', categories=categories.keys())

@app.route('/flashcards/start', methods=['POST'])
def flashcards_start():
    selected_categories = request.form.getlist('categories')
    selected_techniques = []
    for category in selected_categories:
        selected_techniques.extend(categories.get(category, []))
    random.shuffle(selected_techniques)
    if selected_techniques:
        current = selected_techniques.pop(0)
        link = tachi_links.get(current) or ne_links.get(current) or "#"
        return render_template('flashcards_play.html', current=current, link=link, techniques=selected_techniques)
    else:
        return render_template('flashcards_play.html', techniques=[])

@app.route('/flashcards/play', methods=['POST'])
def flashcards_play():
    techniques = request.form.getlist('techniques')
    if techniques:
        current = techniques.pop(0)
        link = tachi_links.get(current) or ne_links.get(current) or "#"
        return render_template('flashcards_play.html', current=current, link=link, techniques=techniques)
    else:
        return render_template('flashcards_play.html', techniques=[])

@app.route('/flashcards/watch/<technique>')
def flashcards_watch(technique):
    format = request.args.get('format', 'video')  # default = video

    link = tachi_links.get(technique) or ne_links.get(technique)
    if not link:
        return "Technique not found.", 404

    if "v=" in link:
        video_id = link.split("v=")[-1].split("&")[0]
    else:
        video_id = link.split("/")[-1]

    gif_path = f"/static/shodan_techniques/{technique}.gif"

    return render_template('flashcards_watch.html',
                           technique=technique,
                           video_id=video_id,
                           gif_path=gif_path,
                           format=format)


# Welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Choose random throw
@app.route('/choose', methods=['GET', 'POST'])
def choose():
    return render_template('choose.html')

@app.route('/results', methods=['POST'])
def results():
    num_tachi = int(request.form['num_tachi'])
    num_ne = int(request.form['num_ne'])
    selected_tachi = random.sample(tachi_waza, num_tachi)
    selected_ne = random.sample(ne_waza, num_ne)
    tachi_with_links = [(tech, tachi_links.get(tech, "#")) for tech in selected_tachi]
    ne_with_links = [(tech, ne_links.get(tech, "#")) for tech in selected_ne]
    return render_template('results.html', tachi=tachi_with_links, ne=ne_with_links)

# --- Video Quiz Mode v2.0 ---

@app.route('/quiz')
def quiz():
    all_moves = list(tachi_links.keys()) + list(ne_links.keys())
    correct_move = random.choice(all_moves)
    options = random.sample(all_moves, 4)
    if correct_move not in options:
        options[random.randint(0, 3)] = correct_move
    random.shuffle(options)

    video_link = tachi_links.get(correct_move) or ne_links.get(correct_move)
    if "v=" in video_link:
        video_id = video_link.split("v=")[-1].split("&")[0]
    else:
        video_id = video_link.split("/")[-1]

    session['correct_move'] = correct_move
    session['video_id'] = video_id
    session['options'] = options

    return render_template('quiz.html',
                           video_id=video_id,
                           options=options)

@app.route('/quiz/answer', methods=['POST'])
def quiz_answer():
    selected = request.form.get('selected')
    correct_move = session.get('correct_move')

    if selected == correct_move:
        result = "Correct!"
    else:
        result = f"Wrong! It was: {correct_move}"

    return render_template('quiz_result.html', result=result)

# --- GIF Quiz Mode (from /static/shodan_techniques/) ---

gif_techniques = [
    "Ashi-guruma", "De-ashi-harai", "Gyaku-juji-jime", "Hadaka-jime", "Hane-goshi", "Hane-makikomi",
    "Harai-goshi", "Harai-tsurikomi-ashi", "Hiza-guruma", "Ippon-seoi-nage", "Kami-shiho-gatame",
    "Kata-gatame", "Kata-guruma", "Kata-juji-jime", "Kata-ha-jime", "Kesa-gatame", "Ko-soto-gake",
    "Ko-soto-gari", "Ko-uchi-gari", "Koshi-guruma", "Kuzure-kami-shiho-gatame", "Kuzure-kesa-gatame",
    "Nami-juji-jime", "O-goshi", "O-guruma", "O-soto-gari", "O-soto-guruma", "O-uchi-gari",
    "Okuri-ashi-harai", "Okuri-eri-jime", "Sasae-tsurikomi-ashi", "Seoi-nage", "Soto-makikomi",
    "Sukui-nage", "Sumi-gaeshi", "Sumi-otoshi", "Tai-otoshi", "Tani-otoshi", "Tate-shiho-gatame",
    "Tomoe-nage", "Tsuri-goshi", "Tsurikomi-goshi", "Uchi-mata", "Ude-garami", "Ude-hishigi-juji-gatame",
    "Ude-hishigi-ude-gatame", "Ude-hishigi-hiza-gatame", "Ude-hishigi-waki-gatame", "Ude-hishigi-hara-gatame",
    "Uki-goshi", "Uki-otoshi", "Uki-waza", "Ura-nage", "Ushiro-goshi", "Utsuri-goshi",
    "Yoko-gake", "Yoko-guruma", "Yoko-otoshi", "Yoko-shiho-gatame", "Yoko-wakare"
]


@app.route('/gifquiz')
def gifquiz_start():
    session['gif_remaining'] = gif_techniques.copy()
    random.shuffle(session['gif_remaining'])
    session['gif_score'] = 0
    session['gif_total'] = 0
    return redirect(url_for('gifquiz'))

@app.route('/gifquiz/play')
def gifquiz():
    if not session.get('gif_remaining'):
        return render_template('gifquiz_done.html', score=session.get('gif_score', 0), total=session.get('gif_total', 0))

    current = session['gif_remaining'].pop(0)
    correct = current

    options = random.sample(gif_techniques, 4)
    if correct not in options:
        options[random.randint(0, 3)] = correct
    random.shuffle(options)

    session['gif_current'] = current
    session['gif_correct'] = correct

    return render_template('gifquiz.html', gif_name=current, options=options, score=session['gif_score'], total=session['gif_total'])

@app.route('/gifquiz/answer', methods=['POST'])
def gifquiz_answer():
    selected = request.form.get('selected')
    correct = session.get('gif_correct')

    if selected == correct:
        session['gif_score'] += 1
        result = "Correct!"
    else:
        result = f"Wrong! It was: {correct}"

    session['gif_total'] += 1

    return render_template('gifquiz_result.html', result=result)



translations = {
    "Seoi-nage": "Shoulder throw",
    "Ippon-seoi-nage": "One-arm shoulder throw",
    "Tai-otoshi": "Body drop",
    "Kata-guruma": "Shoulder wheel",
    "Sukui-nage": "Scooping throw",
    "Uki-otoshi": "Floating drop",
    "Sumi-otoshi": "Corner drop",
    "Uki-goshi": "Floating hip throw",
    "O-goshi": "Major hip throw",
    "Koshi-guruma": "Hip wheel",
    "Tsurikomi-goshi": "Lifting pulling hip throw",
    "Harai-goshi": "Sweeping hip throw",
    "Tsuri-goshi": "Lifting hip throw",
    "Hane-goshi": "Springing hip throw",
    "Utsuri-goshi": "Switching hip throw",
    "Ushiro-goshi": "Rear throw",
    "De-ashi-harai": "Advanced foot sweep",
    "Hiza-guruma": "Knee wheel",
    "Sasae-tsurikomi-ashi": "Supporting lifting foot throw",
    "O-soto-gari": "Major outer reap",
    "O-uchi-gari": "Major inner reap",
    "Ko-soto-gari": "Minor outer reap",
    "Ko-uchi-gari": "Minor inner reap",
    "Okuri-ashi-harai": "Sliding foot sweep",
    "Uchi-mata": "Inner thigh throw",
    "Ko-soto-gake": "Minor outer hook",
    "Ashi-guruma": "Leg wheel",
    "Harai-tsurikomi-ashi": "Sweeping lifting foot throw",
    "O-guruma": "Major wheel",
    "O-soto-guruma": "Major outer wheel",
    "Tomoe-nage": "Circle throw",
    "Sumi-gaeshi": "Corner reversal",
    "Ura-nage": "Rear throw",
    "Yoko-otoshi": "Side drop",
    "Tani-otoshi": "Valley drop",
    "Hane-makikomi": "Springing wraparound throw",
    "Soto-makikomi": "Outer wraparound throw",
    "Uki-waza": "Floating technique",
    "Yoko-wakare": "Side separation",
    "Yoko-guruma": "Side wheel",
    "Yoko-gake": "Side hook",
    "Kesa-gatame": "Scarf hold",
    "Kata-gatame": "Shoulder hold",
    "Kuzure-kami-shiho-gatame": "Modified upper four corner hold",
    "Yoko-shiho-gatame": "Side four corner hold",
    "Tate-shiho-gatame": "Vertical four corner hold",
    "Kuzure-kesa-gatame": "Modified scarf hold",
    "Kami-shiho-gatame": "Upper four corner hold",
    "Nami-juji-jime": "Normal cross choke",
    "Gyaku-juji-jime": "Reverse cross choke",
    "Kata-juji-jime": "Single cross choke",
    "Hadaka-jime": "Rear naked choke",
    "Okuri-eri-jime": "Sliding collar choke",
    "Kata-ha-jime": "Single wing choke",
    "Ude-garami": "Entangled arm lock",
    "Ude-hishigi-juji-gatame": "Cross arm lock",
    "Ude-hishigi-ude-gatame": "Arm lock",
    "Ude-hishigi-hiza-gatame": "Knee arm lock",
    "Ude-hishigi-waki-gatame": "Armpit arm lock",
    "Ude-hishigi-hara-gatame": "Stomach arm lock"
}

@app.route('/translation', methods=['GET', 'POST'])
def translation_start():
    if request.method == 'POST':
        mode = request.form.get('mode')
        session['mode'] = mode
        session['remaining'] = list(translations.keys()) if mode == 'ja_to_en' else list(translations.values())
        random.shuffle(session['remaining'])
        session['score'] = 0
        session['total'] = 0
        return redirect(url_for('translation_quiz'))
    return render_template('translation_mode.html')

@app.route('/translation/quiz', methods=['GET'])
def translation_quiz():
    if not session.get('remaining'):
        return render_template('translation_done.html', score=session.get('score', 0), total=session.get('total', 0))
    
    mode = session['mode']
    question = session['remaining'].pop(0)
    correct_answer = translations[question] if mode == 'ja_to_en' else [k for k, v in translations.items() if v == question][0]

    # Build 4 random wrong answers
    pool = list(translations.values() if mode == 'ja_to_en' else translations.keys())
    pool = [item for item in pool if item != correct_answer]
    options = random.sample(pool, 4)
    options.append(correct_answer)
    random.shuffle(options)

    session['current_question'] = question
    session['current_correct'] = correct_answer

    return render_template('translation.html',
                           question=question,
                           options=options,
                           mode=mode,
                           score=session.get('score', 0),
                           total=session.get('total', 0))

@app.route('/translation/answer', methods=['POST'])
def translation_answer():
    selected = request.form.get('selected')
    correct = session['current_correct']

    if selected == correct:
        session['score'] += 1
        result = "Correct!"
    else:
        result = f"Wrong! Correct answer was: {correct}"

    session['total'] += 1

    return render_template('translation_result.html', result=result)

# --- Review Techniques Mode ---

@app.route('/review')
def review():
    format = request.args.get('format', 'video')  # default to video if not specified
    return render_template('review.html', categories=categories, format=format)

@app.route('/review/<technique>')
def review_play(technique):
    format = request.args.get('format', 'video')  # default to video here too

    # Find the YouTube link
    link = tachi_links.get(technique) or ne_links.get(technique)
    if not link:
        return "Technique not found.", 404

    # Extract YouTube video ID properly
    if "v=" in link:
        video_id = link.split("v=")[-1].split("&")[0]
    else:
        video_id = link.split("/")[-1]

    # Path to the gif (we assume the gif matches the technique name exactly)
    gif_path = f"/static/shodan_techniques/{technique}.gif"

    return render_template('review_play.html',
                           technique=technique,
                           video_id=video_id,
                           gif_path=gif_path,
                           format=format)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

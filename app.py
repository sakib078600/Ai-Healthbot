from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basic health replies
def get_health_reply(message):
    msg = message.lower()
    if "fever" in msg:
        return "Fever ke liye rest lo, paani zyada piyo aur doctor se consult karo agar 2 din se jyada ho."
    elif "sar dard" in msg:
        return "sar dard ke liye paani piyo, stress kam lo aur rest karo."
    elif "cold" in msg or "cough" in msg:
        return "Garam paani ya kadha lo, thanda food avoid karo."
    elif "diet" in msg or "food" in msg:
        return "Balanced diet lo — fruits, green vegetables, aur junk food kam karo."
    elif "sleep" in msg:
        return "Har din kam se kam 7-8 ghante ki neend lo."
    if "hi" in msg:
        return "bolna be saale jaldi."
    if "pimple" in msg:
        return "mutthi maarna chhod de bkl."  
    if "body pain" in msg:
        return "raat ko bathroom jana chhod de."
    if "ok" in msg:
        return "hmm or kuchh puchnna hai chomu."
    if "nahi" in msg:
        return "bhagg be jaake doctor se puchhle dalal." 
    if "pet dard" in msg:
        return "lahori zeera piyo be." 
    if "stress" in msg:
        return "agar raat me stress ho raha h to muttthi marke soja or agar morning me ho raha hai to mind relax rakh jyada soch mat or positive soch or agar jyada hee stress hai to fir bandi se baat karle."
    if "bandi" in msg: 
        return "shakal dekh le bkl fir bandi patana."
    if "aankh dard" in msg:
        return "chrome dekhna band karde."  
    if "chakkar" in msg:  
        return "ORSL Juice pi le, thik ho jayega."
    if "medicine" in msg:
        return "doctor se puchhke hee lena h apne se manforce mat lena. "
    if "bukhar" in msg:
        return "bukhar me jitna ho sakta hai rest le, suto mobile on karo 1gb me 1 ghanta chal jayega."
    if "nahi jaunga" in msg:
        return "to mat jaaao marao."
    if "typhod" in msg:
        return "saaf paani piyo, jangi wala roj jal piyo."
    if "nunni" in msg:
        return "chhotti lulli hai teri khada ho ya na ho pata kaise chalega."
    else:
        return "bsdk bolna kya kaam hai , bakchodi karne me to aage hai."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = get_health_reply(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/dictionary/<string:word>")
def dictionary(word):
    dict_english={"apple":"사과","banana":"바나나","melon":"멜론"}
    for i in dict_english:
        if word == i:
            word2 = dict_english[i]
            break
        else:
            word2 = "나만의 단어장에 없는 단어"
    
    
    return render_template("dictionary.html", word=word, word2=word2)
    


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)

# 참고코드
# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"
    
# @app.route("/dictionary/<string:word>")
# def dictionary(word):
#     dict_english={"apple":"사과","banana":"바나나","melon":"멜론"}
#     resut = dict_english.get(word)
#     if result:
#         result = f"{word}:{result}"
#     else:
#         result = f"{word}은(는) 단어장에 없는 단어"
        
#     return result

#FLASK_APP=app.py flask run --host=$IP --port=$PORT
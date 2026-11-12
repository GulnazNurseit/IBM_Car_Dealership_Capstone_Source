from flask import Flask,jsonify
app=Flask(__name__)
POS=('great','good','excellent','friendly','helpful','love','easy')
NEG=('bad','poor','slow','rude','terrible','awful')
@app.get('/analyze/<path:text>')
def analyze(text):
    s=text.lower(); p=sum(w in s for w in POS); n=sum(w in s for w in NEG)
    return jsonify({'sentiment':('positive' if p>n else 'negative' if n>p else 'neutral'),'method':'local demo heuristic; not IBM Watson NLU'})
@app.get('/health')
def health():return jsonify({'ok':True})
if __name__=='__main__':app.run(host='0.0.0.0',port=5000)

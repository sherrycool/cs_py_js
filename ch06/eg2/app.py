from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

texts = ['点绛唇\n金谷年年，乱生春色谁为主。馀花落处。满地和烟雨。又是离歌，一阕长亭暮。王孙去。萋萋无数。南北东西路。',
'霜天晓角\n冰清霜洁。昨夜梅花发。甚处玉龙三弄，声摇动、枝头月。梦绝。金兽。晓寒兰烬灭。要卷珠帘清赏，且莫扫、阶前雪。',
'瑞鹧鸪\n众芳摇落独鲜妍。占尽风情向小园。疏影横斜水清浅。暗香浮动月黄昏。寒禽俗下先偷眼，粉蝶如知合断魂。幸有微吟可相狎，不须檀板共金尊。']

@app.route("/first")
def first():
	return texts[0]

@app.route("/second")
def second():
	return texts[1]

@app.route("/third")
def third():
	return texts[2]
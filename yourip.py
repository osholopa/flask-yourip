from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def yourip():
	userAgent = request.user_agent.string
	remoteAddr = request.remote_addr
	return render_template("yourip.html", userIp=remoteAddr, userAgent=userAgent)

##app.run(debug=True)

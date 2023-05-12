from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

# Store the currently selected video URL
current_video_url = 'static/IMG_8070.mp4'

@app.route('/', methods=['GET', 'POST'])
# @app.route('/')
def index():
    global current_video_url

    if request.method == 'POST':
        # Retrieve the video URL from the form submission
        new_video_url = request.form.get('video_url')
        
        # Update the currently selected video URL
        current_video_url = new_video_url

    # Render the HTML template with the current video URL and a form to input a new video URL
    return render_template('index.html', current_video_url=current_video_url)

if __name__ == '__main__':
    # app.run(port = 5000, debug = True)
    app.run(host = "20.119.8.29", debug = True)

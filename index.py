from click import confirm
import configuration
from flask import *
import os
template_dir = os.path.abspath('frontend')
app = Flask(__name__, template_folder=template_dir)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
import flask.cli
flask.cli.show_server_banner = lambda *args: None
if configuration.enable_help == 'yes':
    print("Success! The Webserver is now listening on Port " + configuration.listen + ":" + configuration.port + ". The first step is done. Read more in the Docs: https://blutudlut.xyz/mchostingz/docs/mainactyl/config!")
else: 
    print("Success! The Webserver is now listening on Port " + configuration.listen + ":" + configuration.port + ".")


################
#              #
#              #
#    Pages.    #
#              #
#              #
################

@app.route("/")
def index():
    return render_template("index.html", name = configuration.application_name)







#Run
if configuration.version == '0.1_BETA' and configuration.config_version == '0.1':

    if __name__ == '__main__':
      app.run(host=configuration.listen, port=configuration.port)
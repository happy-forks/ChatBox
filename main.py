from flask import Flask, render_template, redirect, url_for, request, session, escape
#import flask_sijax
import datetime
app = Flask(__name__)
app.secret_key = 'boop'
import sqlite3
import configparser

# Behind the scenes stuff #

def saveConfig(configName):
    # Save any configuration changes
    with open(configName, "w") as configfile:
        config.write(configfile)
def config():
     # create the global config
     global config, log_user_messages, console_user_messages
     # create JUST the file if it does not exist or read he file for append, depending on if the file exists
     gereateFileIfNotExist = open("config.cfg","a")
     gereateFileIfNotExist.close()
     config = configparser.ConfigParser()
     config.read("config.cfg")
     # Check if the config exists
     try:
         config.read('config.cfg')
         shall_we_log = config.get("Settings", "Log User Messages").lower()
         shall_print_to_console = config.get("Settings", "Print Messages to Console").lower()         
         saveConfig("config.cfg")           
     except:
         # Generate config, because it does not exists
         config.add_section("Settings")
         config.set("Settings", "Log User Messages", "true")
         config.set("Settings", "Print Messages to Console", "false")
         saveConfig("config.cfg")
         shall_we_log = config.get("Settings", "Log User Messages").lower()
         shall_print_to_console = config.get("Settings", "Print Messages to Console").lower()   
     if (shall_we_log == "true"):
          log_user_messages = True
     else:
          log_user_message = False
     if (shall_print_to_console == "true"):
          console_user_messages = True
     else:
          console_user_messages = False
def init_log():
     #Clears all logs when program first runs.
     log_file = open("Log.log", 'w')
     log_file.close()
     message_file = open("Message_log.log", 'w')
     message_file.close()
     
def log(log_message):
     timeOfLog = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S" + " : ")
     print ("[Log] [" + log_message + "]")
     log = open("Log.log", 'a')
     #Add username logging here when usernames are sorted.
     log.write("[" + timeOfLog + "][" + log_message + "]; \n")
     log.close()
     
def message_log(log_message):
     if (log_user_messages):
          timeOfLog = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
          if (console_user_messages):
               print ("[MSG] [" + log_message + "]")
          message_log = open("Message_Log.log", 'a')
          #Add username logging here when usernames are sorted.
          message_log.write("[" + timeOfLog + "]:[" + log_message + "]; \n")
          message_log.close()
# End of behind the scenes #
config()     
init_log()
log("Program successfully launched")
message_log("~Start of message log~")

# Front of App #
@app.route("/", methods=['GET', 'POST'])
def index():
     log("wat")
     if request.method == 'POST':
          
          session['email'] = request.form['email']
          session['password'] = request.form['password']

          if 'email' in session:
               if session['email'] != "" or session['password'] != "":
                    return render_template('index.html', isLoggedIn=session['email'])
          return render_template('index.html')

     else:
          return render_template('index.html')
     
@app.route('/database')
def database():
     
     conn = sqlite3.connect("users.db")
     c = conn.cursor()
     c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn="user", nf="aidan", ft="TEXT"))
     return (conn.execute("SELECT aidan  from users"))
     conn.commit()
     conn.close()
     
@app.route('/login', methods=['GET', 'POST'])
def login():

     return render_template('login.html')

     error = None
     if request.method == "POST":
          if request.form["username"] != "admin" or request.form["password"] != "admin":
               error = "Invalid cridentials"
          else:
               return redirect(url_for("boop"))
          return render_template("/login.html", error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
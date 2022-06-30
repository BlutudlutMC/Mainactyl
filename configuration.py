#do not change
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ------- Required Settings -------
# ---------------------------------
# ---------------------------------
# ---------------------------------
version = '0.1_BETA'
theme = 'frontend'
#change
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ------- General Settings -------
# ---------------------------------
# ---------------------------------
# ---------------------------------
cookie_key = 'random string'
port = '3000'
listen = '0.0.0.0' #Only change this if you know what you are doing.
enable_help = 'yes'
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ------- Environment Config -------
# ---------------------------------
# ---------------------------------
# ---------------------------------
application_name = 'Mainactyl' #The name of your company
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ------- Pterodactyl Config -------
# ---------------------------------
# ---------------------------------
# ---------------------------------
pterodactyl_domain = 'https://client.blutudlut.xyz' #your ptero domain. with https:// or http:// !
pterodactyl_admin_api = 'ptla_lnUcZ9b0CZQyc8qIUm6GFe7mVKOjoSC0DW3XYtUhznl'
pterodactyl_client_api = 'ptlc_DBLKsTETOgnEpfuoEEiQIazLDEipKSM9PwShDuuoTsh' #If you want to send power-actions in the dashboard use this.
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ------- Authentication Config -------
# ---------------------------------
# ---------------------------------
# ---------------------------------
login_variant = 'credentials_sqlite' 
#Default: credentials_sqlite to store the credentials in a SQLite3 Database. No Discord OAuth2
#credentials_mysql to store the credentials in a MySQL Database. No Discord OAuth2
#discord_oauth normal discord login.
#mysql_discord for both options.
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ------- Location Settings -------
# ---------------------------------
# ---------------------------------
# ---------------------------------
all_nodes = '2' #How many nodes do you have?

#NODE NAMES:
node_1 = 'Germany 1' #If you want to add a node: add a variable: node_ and then the ID of the node. eg: node_3 = 'Germany 3'
node_2 = 'Germany 2'
#SETTINGS
stop_server_creation_on_overload = 'yes' #NOT TRUE/FALSE: yes/no

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ------- MySQL DB Settings -------
# ---------------------------------
# ---------------------------------
# ---------------------------------
db_drive = 'sql_3_' #DO NOT CHANGE!
db_password = 'your password'
db_user = 'mainactyl'
db_name = 'mainactyl_db'
db_host = '127.0.0.1:3306' #with port!
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ------- Copyright Settings -------
# ---------------------------------
# ---------------------------------
# ---------------------------------
show_powered_by_footer = 'yes' #if you want to support us, leave it enabled <3

#Made with <3 by Blutudlut
#Mainactyl (c)
#Mainactyl Configuration Version: 0.1
config_version = '0.1'

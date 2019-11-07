from application import app, manager,db
from flask_script import Server
import www

manager.add_command("runserver", Server(host="0.0.0.0", port= 5000, use_debugger= True, use_reloader= True))



def main():
    db.create_all()
    manager.run()



if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
        pass
    except Exception as e:
        import traceback
        traceback.print_exc()
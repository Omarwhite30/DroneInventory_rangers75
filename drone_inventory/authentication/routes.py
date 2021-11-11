from flask import blueprints, render_template

auth = blueprint('auth' ,__name__, template_folder='auth_templates')

@auth.route('/signup' ,methods = ['GET' , 'POST'])
def signup():
    return render_template('signup.hmtl')

    @auth.route('/singin' ,methods = ['GET' , 'POST'])
    def signin():
        return render_template('signin.html')
         
import boto3
import json
from flask import Flask, request, render_template,url_for, flash, redirect
from forms import stackcreationForm

app = Flask(__name__,template_folder='templates')
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'content': 'First post content'
    }
]

@app.route("/")

@app.route("/about")
def about():
    return render_template('about.html', title=' ')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/creation")
def creation():
    
        return render_template('creation.html', posts=posts)
    

@app.route("/stack", methods=['GET', 'POST'])
def stack():
    form = stackcreationForm()
    if form.validate_on_submit():
        flash(f'Stack created for {form.DBuser.data} completed', 'success')
        return redirect(url_for('creation'))
    return render_template('stackcreation.html', title=' ', form=form)

@app.route('/', methods =["GET", "POST"])
def hello():
    if request.method == "POST":
        with open("v1.json") as f:
            data = json.load(f)
                
        data['Parameters']['KeyName']['Default'] = request.form.get("KeyPair")
        data['Parameters']['InstanceType']['Default'] = request.form.get("InstanceType")
        data['Parameters']['DBName']['Default'] = request.form.get("DBname")
        data['Parameters']['DBUser']['Default'] = request.form.get("DBuser")
        data['Parameters']['DBPassword']['Default'] = request.form.get("DBpassword")
        data['Parameters']['DBRootPassword']['Default'] = request.form.get("DBRootPassword")

        # print(data['Parameters']['KeyName']['Default'])
        client = boto3.client('cloudformation',
            region_name = 'ap-south-1',
            aws_access_key_id='AKIAVT2VQBKFBVSDPGVR',
            aws_secret_access_key='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')
        
        response = client.create_stack(
            StackName="stack",
            TemplateBody=json.dumps(data),
            DisableRollback=False,
        )
        return render_template("")

if __name__ == '__main__':
    app.run()




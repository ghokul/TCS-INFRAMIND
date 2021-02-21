from flask import Flask, render_template, url_for, flash, redirect
from forms import stackcreationForm

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


if __name__ == '__main__':
    app.run(debug=True)
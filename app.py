from flask import Flask, url_for, render_template
from book_info_extractor import get_info_book_picks, display_table


app=Flask(__name__)

@app.route('/')
def index():
	tabs = ['Home','Blog','Events','Newsletter','FAQ','About','Contact']
	return render_template("index.html")
	# return ("Quills Library Home page")

@app.route('/books')
def books():
	filepath = "../static/images/1984'.jpg"
	book_name = "1984'.jpg"
	# print (get_info_book_picks())
	df = display_table()
	return render_template("books.html", filepath=filepath, book_picks_info=get_info_book_picks(), tables=[df.to_html(classes='data', header="true")])


@app.route('/fake')
def fake():
	return render_template("fake.html", book_picks_info=get_info_book_picks())

@app.route('/blog')
def blog():
	return render_template("blog.html")

@app.route('/events')
def events():
	return("Upcoming events")

# debatable. should come with blog?
@app.route('/Newsletter')
def newsletter():
	return("Sign in to receive bi-monthly Newsletter\nView previous Newsletters here")

@app.route('/faq')			
def faq():
	return "FAQ: Membership, timing, late fee, donations, etc"

@app.route('/about')	
def about():
	return "Founders. Communal space. Library. Learning environment"

@app.route('/contact')	
def contact():
	return render_template('contact.html')





if __name__ == '__main__':
	app.run(host="0.0.0.0", port="5400", debug=True)
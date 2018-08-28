from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine



@app.route('/')
@app.route('/hello')
def HelloWorld():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ""
    for i in items:
        output += i.name
        output += '</br>'

    return  output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)

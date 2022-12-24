import os
from flask import Flask, request, abort, jsonify,json
from sqlalchemy.ext.mutable import Mutable
# from models import setup_db, Question, Category 
from sqlalchemy.dialects import postgresql
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:youssef@localhost:5432/opera'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
CORS(app)

class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(120))
    lname = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    address = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))

class Customer(db.Model):
    __tablename__ = 'customer'
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def kolo(self):
        x = {
            "id": self.id,
            "fname": self.fname ,
            "lname": self.lname,
            "phone": self.phone,
            "address": self.address,
            "email": self.email
        }
        return x

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(120))
    lname = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    address = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    Book_ID = db.relationship('Book', backref='Customer', lazy=True)

class MutableList(Mutable, list):

    def __setitem__(self, key, value):
        list.__setitem__(self, key, value)
        self.changed()

    def __delitem__(self, key):
        list.__delitem__(self, key)
        self.changed()

    def append(self, value):
        list.append(self, value)
        self.changed()

    def pop(self, index=0):
        value = list.pop(self, index)
        self.changed()
        return value

    @classmethod
    def coerce(cls, key, value):
        if not isinstance(value, MutableList):
            if isinstance(value, list):
                return MutableList(value)
            return Mutable.coerce(key, value)
        else:
            return value

class Book(db.Model):
    __tablename__ = 'book'
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    id = db.Column(db.Integer, primary_key=True)
    seats = db.Column(db.Integer)
    booked_seats= db.Column(postgresql.ARRAY(db.Integer))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    total_price = db.Column(db.Integer)

class Event(db.Model):
    tablename = 'event'

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def format(self):
        artist_ids = Present.query.with_entities(Present.artist_id).filter(Present.event_id==self.id).all()
        artist_names = []
        for id in artist_ids:
            artist = Artist.query.with_entities(Artist.fname).filter(Artist.id==id).all()
            artist_names.append(artist[0][0])
        
        x = {
            "id": self.id,
            "name": self.name ,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "image_link": self.image_link,
            "description": self.description,
            "price": self.price,
            "artist_ids": artist_ids,            
            "mapped_free_seats": self.mapped_free_seats,
            "artist_names": artist_names,
            "category": self.category
        }
        return x
    
    def data(self):
        artist_ids = Present.query.with_entities(Present.artist_id).filter(Present.event_id==self.id).all()
        artist_names = []
        for id in artist_ids:
            artist = Artist.query.with_entities(Artist.fname).filter(Artist.id==id).all()
            artist_names.append(artist[0][0])
        x = {
            "id": self.id,
            "name": self.name ,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "image_link": self.image_link,
            "description": self.description,
            "price": self.price,
            "artist_ids": artist_ids,            
            "free_seats": self.free_seats,
            "artist_names": artist_names
        }
        return x

    def short(self):
        x = {
            "name": self.name 
        }
        return x

    def book(self):
        x = {
            "price": self.price,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "free_seats": self.free_seats
        }
        return x


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    start_time = db.Column(db.String(500), nullable=False)
    end_time = db.Column(db.String(500), nullable=False)
    image_link = db.Column(db.String(500))
    description = db.Column(db.String(1000))
    free_seats = db.Column(db.Integer)
    mapped_free_seats= db.Column(MutableList.as_mutable(postgresql.ARRAY(db.Boolean,  zero_indexes=False)))
    price = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    Book_ID = db.relationship('Book', backref='Event', lazy=True)
    present_ID = db.relationship('Present', backref='Event', lazy=True)
    location_Id = db.relationship('Location', backref='Event', lazy=True)

class Present(db.Model):
    __tablename__ = 'present'

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

class Artist(db.Model):
    __tablename__ = 'artist'

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def format(self):
        x = {
            "id": self.id,
            "fname": self.fname ,
            "lname": self.lname,
            "address": self.address,
            "phone": self.phone,
            "description": self.description,
            "image_link": self.image_link 
        }
        return x

    def intro(self):
        x = {
            "id": self.id,
            "fname": self.fname ,
            "lname": self.lname,
            "description": self.description,
            "phone": self.phone,
            "image_link": self.image_link 
        }
        return x

    def short(self):
        x = {
            "name": self.name 
        }
        return x
    
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    description = db.Column(db.String(1000))
    present_ID = db.relationship('Present', backref='Artist', lazy=True)


class Location(db.Model):
    __tablename__ = 'location'

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    id = db.Column(db.Integer, primary_key=True)
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)


class Theatre(db.Model):
    __tablename__ = 'theatre'

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def kol(self):
        x = {
            "name": self.name,
            "image_link": self.image_link,
            "seat_capacity": self.seat_capacity,
            "seat_map": self.seat_map
        }
        return x
    
    def format(self):
        x = {
            "name": self.name,
            "image_link": self.image_link,  
            "id": self.id

        }
        return x

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_link = db.Column(db.String(500))
    seat_map = db.Column(db.String(1000))
    seat_capacity = db.Column(db.Integer)
    location_ID = db.relationship('Location', backref='Theatre', lazy=True)

class Category(db.Model):
    __tablename__ = 'category'

    def format(self):
        x = {
            "name": self.name,
            "image_link": self.image_link
        }
        return x

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_link = db.Column(db.String(500))

db.create_all()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers','GET, POST, PATCH, DELETE, OPTIONS')
    return response
        

@app.route('/admin_login', methods=['POST'])
def admin_login():
    take=request.get_json()
    if not (take.get('email') and take.get('password')):
        abort(422)
    email = take.get('email', "")
    password = take.get('password',"")
    try:
        user = Admin.query.filter_by(email=email).all()
        if len(user) < 1:
            abort(422)
        if password != user[0].password:
            return jsonify({'success': False})
        else:
            get_id = user[0].id
            return jsonify({'success': True,'admin_id':get_id})

    except:
        abort(422)

@app.route('/login', methods=['POST'])
def Login():
    take=request.get_json()
    if not (take.get('email') and take.get('password')):
        abort(422)
    email = take.get('email', "")
    password = take.get('password',"")
    try:
        user = Customer.query.filter_by(email=email).all()
        if len(user) < 1:
            abort(422)
        if password != user[0].password:
            return jsonify({'success': False})
        else:
            get_id = user[0].id
            return jsonify({'success': True,'customer_id':get_id})

    except:
        abort(422)


@app.route('/landing', methods=['GET'])
def landing():
    try:
        all_events = Event.query.filter_by()
        events = []
        date = str(datetime.now()).split(' ')[0]
        for event in all_events:
            if(event.start_time.split(' ')[0] > date):
                events.append(event.format())
        return jsonify({"events": events})
    except:
        abort(500)

@app.route('/category_event/<category_id>', methods=['GET'])
def category_event(category_id):
    try:
        category_event = Event.query.filter_by(category=category_id).all()
        events = []
        date = str(datetime.now()).split(' ')[0]
        for event in category_event:
            if(event.start_time.split(' ')[0] > date):
                events.append(event.data())
        return jsonify({"events": events})
    except:
        abort(500)

@app.route('/show_categorys', methods=['GET'])
def show_categorys():
    try:
        all_categorys = Category.query.all()
        categorys = []
        for category in all_categorys:
            categorys.append(category.format())
        return jsonify({"categorys": categorys})

    except:

        abort(500)

@app.route('/show_event/<event_id>', methods=['GET'])
def show_event(event_id):
    try:
        id_events = Event.query.get(event_id)
        return jsonify({"events": [id_events.format()]})
    except:
        abort(500)


@app.route('/show_artist', methods=['GET'])
def show_artist():
    try:
        all_artist = Artist.query.all()
        artists = []
        for artist in all_artist:
            artists.append(artist.intro())
        return jsonify({"artists": artists})

    except:
        abort(500)


@app.route('/show_artist/<artist_id>', methods=['GET'])
def show_artists(artist_id):
    try:
        all_artist = Artist.query.get(artist_id)
        return jsonify({"artists": [all_artist.format()]})

    except:

        abort(500)

@app.route('/show_theatre', methods=['GET'])
def show_theatre():
    try:
        all_theatre = Theatre.query.all()
        theatree = []
        for theatre in all_theatre:
            theatree.append(theatre.format())
        return jsonify({"theatre": theatree})

    except:

        abort(500)

@app.route('/show_theatre/<theatre_id>', methods=['GET'])
def show_theatres(theatre_id):
    try:
        all_theatre = Theatre.query.get(theatre_id)
        return jsonify({"theatre": [all_theatre.kol()]})

    except:

        abort(500)

@app.route('/show_customer/<customer_id>', methods=['GET'])
def show_customer(customer_id):
    try:
        all_Customer = Customer.query.get(customer_id)
        return jsonify({"custumer": [all_Customer.kolo()]})

    except:

        abort(500)

    
@app.route('/search', methods=['GET'])
def search():
    try:
        take=request.get_json()
        Key_Word = take.get("searchTerm")
        res = Event.query.filter(Event.name.ilike(f"%{Key_Word}%")).all()
        events = [event.short() for event in res]
        res = Artist.query.filter(Artist.fname.ilike(f"%{Key_Word}%")).all()
        artists = [artist.short() for artist in res]
        res = Theatre.query.filter(Theatre.name.ilike(f"%{Key_Word}%")).all()
        theatres = [theatre.format() for theatre in res]
        if len(artists) == 0 and len(theatres) == 0 and len(events) == 0:
            abort(422)
        return jsonify({"artists": artists, "events" : events, "theatres" : theatres})
    except:
        abort(404)


@app.route('/customer_forget_password/<customer_id>', methods=['PATCH'])
def customer_forget_password(customer_id):
    try:
        take=request.get_json()
        update = Customer.query.get(customer_id)
        if not update:
            abort(404)
        update.password= take['new_password']
        update.update()
        return jsonify({"success": True})

    except:

        abort(422)


@app.route('/update_customer/<customer_id>', methods=['PATCH'])
def update_customer(customer_id):
    try:
        take=request.get_json()
        update = Customer.query.get(customer_id)
        if not update:
            abort(404)
        update.fname= take['new_fname']
        update.lname= take['new_lname']
        update.address= take['new_address']
        update.phone= take['new_phone']
        update.email= take['new_email']
        update.update()
        return jsonify({"success": True})

    except:

        abort(422)


@app.route('/update_event/<id>', methods=['PATCH'])
def update_event(id):
    try:
        take=request.get_json()
        update_present = Present.query.filter_by(event_id=id).all()
        if not update_present:
            abort(404)
        artists_id = take.get ('artist_id',[])
        for artist in artists_id:
            data1= Present(artist_id=artist)
            data1.update()

        update_theatre = Location.query.filter_by(event_id=id).first()
        if not update_theatre:
            abort(404)
        update_theatre.theatre_id= take['new_theatre_id']
        update_theatre.update()

        update = Event.query.get(id)
        if not update:
            abort(404)
        update.name= take['new_name']
        update.start_time= take['new_start_time']
        update.end_time= take['new_end_time']
        update.image_link= take['new_image_link']
        update.description= take['new_description']
        update.price= take['new_price']
        update.category= take['new_category']
        # update.free_seats = take['free_seats']
        # update.mapped_free_seats = take['mapped_free_seats']

        update.update()
        return jsonify({"success": True, "update": id})

    except:

        abort(422)       


@app.route('/update_artist/<artist_id>', methods=['PATCH'])
def update_artist(artist_id):
    try:
        take=request.get_json()
        update = Artist.query.get(artist_id)
        if not update:
            abort(404)
        update.fname= take['new_fname']
        update.lname= take['new_lname']
        update.address= take['new_address']
        update.phone= take['new_phone']
        update.image_link= take['new_image_link']
        update.description= take['new_description']
        update.update()
        return jsonify({"success": True, "update": artist_id})

    except:

        abort(422)


@app.route('/update_theatre/<theatre_id>', methods=['PATCH'])
def update_theatre(theatre_id):
    try:
        take=request.get_json()
        update = Theatre.query.get(theatre_id)
        if not update:
            abort(404)
        update.name= take['new_name']
        update.seat_capacity= take['new_capacity']
        update.image_link= take['new_image']
        update.seat_map= take['new_seat_map']
        update.update()
        return jsonify({"success": True, "update": theatre_id})

    except:

        abort(422)

@app.route('/customer/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        delete=Customer.query.get(customer_id)
        delete.delete()
        return jsonify({"success": True, "delete": customer_id})
        
    except:

        abort(401)



@app.route('/event/<id>', methods=['DELETE'])
def delete_event(id):
    try:
        delete_present = Present.query.filter_by(event_id=id).all()
        for deletes in delete_present:
            deletes.delete()
        delete_theatre_ev = Location.query.filter_by(event_id=id).all()
        for deletes in delete_theatre_ev:
            deletes.delete()
        delete=Event.query.get(id)
        delete.delete()
        return jsonify({"success": True, "delete": id})
        
    except:

        abort(401)


@app.route('/artist/<id>', methods=['DELETE'])
def delete_artist(id):
    try:
        delete_present = Present.query.filter_by(artist_id=id).all()
        for deletes in delete_present:
            deletes.delete()
        delete=Artist.query.get(id)
        delete.delete()
        return jsonify({"success": True, "delete": id})
        
    except:

        abort(401)


@app.route('/theatre/<id>', methods=['DELETE'])
def delete_theatre(id):
    try:
        delete_theatre = Location.query.filter_by(theatre_id=id).all()
        for deletes in delete_theatre:
            deletes.delete()
        delete=Theatre.query.get(id)
        delete.delete()
        return jsonify({"success": True, "delete": id})
        
    except:

        abort(401)


@app.route('/submission_customer', methods=['POST'])
def create_customer():
    take=request.get_json()
    if not (take.get('Customer_Fname') and take.get('Customer_Lname') and take.get('Customer_password') and take.get('Customer_email') and take.get('Customer_number') and take.get('Customer_address')):
        abort(422)
    Fname = take.get('Customer_Fname', "")
    Lname = take.get('Customer_Lname', "")
    address = take.get('Customer_address',"")
    password = take.get('Customer_password', "")
    email = take.get('Customer_email', "")
    number = take.get('Customer_number', "")
    customer_email_verifacation = Customer.query.filter_by(email=email).first()
    try:
        if not customer_email_verifacation:  
            fill_table = Customer(fname=Fname,lname=Lname ,address=address, phone=number,email=email,password=password )
            fill_table.insert()
            return jsonify({'success':True})
        else:
            return jsonify({'success':False ,'comment':"email already used"})

    except:

        abort(422)

@app.route('/submission_artist', methods=['POST'])
def create_Artist():
    take=request.get_json()

    if not (take.get('Artist_Fname') and take.get('Artist_Lname') and take.get('Artist_image') and take.get('Artist_number') and take.get('Artist_address') and take.get('Artist_description')):
        abort(422)
    Fname = take.get('Artist_Fname', "")
    Lname = take.get('Artist_Lname', "")
    address = take.get('Artist_address',"")
    image = take.get ('Artist_image',"")
    number = take.get('Artist_number', "")
    description = take.get('Artist_description',"")
    try:
        fill_table = Artist(fname=Fname, lname=Lname ,address=address, phone=number,description=description,image_link=image )
        fill_table.insert()
        return jsonify({'success':True})

    except:

        abort(422)


@app.route('/create_teatre', methods=['POST'])
def create_teatre():
    take=request.get_json()
    if not (take.get('teatre_name') and take.get('teatre_capacity')):
        abort(422)
    name = take.get('teatre_name', "")
    theatre_image = take.get('theatre_image',"")
    theatre_mape_image = take.get('theatre_mape_image',"")
    capacity = take.get('teatre_capacity',"")
    try:
        fill_table = Theatre(name=name,image_link=theatre_image,seat_map= theatre_mape_image,seat_capacity=capacity)
        fill_table.insert()
        return jsonify({'success':True})
    except:

        abort(422)


@app.route('/submission_event', methods=['POST'])
def create_event():
    try:   
        take=request.get_json()
        if not (take.get('event_name') and take.get('event_start') and take.get('event_end') and take.get('event_image') and take.get('event_price') and take.get('event_description') and take.get('artist_id') and take.get('loc_event_id')):
            abort(422)
        name = take.get('event_name', "")
        start = take.get('event_start',"")
        end = take.get('event_end', "")
        image = take.get ('event_image',"")
        price = take.get('event_price', "")
        category_id = take.get('event_category', "")
        description = take.get('event_description',"")
        artist_id = take.get ('artist_id',[])
        location_id = take.get ('loc_event_id',"")
        free_seats = Theatre.query.filter_by(id=location_id).first().seat_capacity
        mapped_free_seats = [False]*free_seats

        if len(artist_id)<1:
            abort (422)

        fill_table = Event(name=name, start_time=start, end_time=end,image_link=image,
                            description=description,category=category_id,price=price,mapped_free_seats=mapped_free_seats,free_seats=free_seats )
        fill_table.insert()
        event_id = Event.query.filter_by(name=name).first().id

        for artist in artist_id:
            data1= Present(artist_id=artist, event_id=event_id)
            data1.insert()
        data = Location (theatre_id=location_id, event_id=event_id)
        data.insert()
        return jsonify({'success':True})

    except:

        abort(422)


@app.route('/booking_event/<event_id>', methods=['GET'])
def booking_event(event_id):
    try:
        selected_events = Event.query.filter_by(id=event_id)
        EVENT = []
        date = str(datetime.now()).split(' ')[0]
        for event in selected_events:
            if(event.start_time.split(' ')[0] > date):
                EVENT.append(event.format())
        return jsonify({"events": EVENT})
    except:
        abort(500)


@app.route('/free_seats/<event_id>', methods=['GET'])
def free_seets(event_id):
    try:
        free_seat = Event.query.get(event_id)
        seats = free_seat.mapped_free_seats
        seats_with_index = []
        for i,seat in enumerate(seats):
            seats_with_index.append({"seat":i+1, "state":seat })

        price = Event.query.filter_by(id=event_id).first().price
        return jsonify({"mapped_free_seats":seats_with_index,"price":price})
    except:
        abort(500)
    
    
@app.route('/booking', methods=['POST'])
def book_event():
    try:
        take=request.get_json()
        if not (take.get('event_id') and take.get('customer_id') and take.get('customer_seats')):
            abort(422)
        event_id = take.get('event_id', "")
        customer_id = take.get('customer_id', "")
        Category = take.get('Category', "")
        price = take.get('price', "")
        seats = take.get('customer_seats', [])
        varifcation = Book.query.filter_by(event_id=event_id,customer_id=customer_id).all()
        if not varifcation:
            Theatre_id = Location.query.filter_by(event_id=event_id).first().theatre_id
            Theatre_seats_map = Theatre.query.filter_by(id=Theatre_id).first().seat_map
            if len(seats) < 1:
                abort(422)
            current_event = Event.query.get(event_id)
            for seat in seats:
                if(current_event.mapped_free_seats[seat-1]):
                    return jsonify({'success':False , 'comment':"seat(s) already taken"})
            
            fill_table = Book(customer_id=customer_id, event_id=event_id, booked_seats=seats , seats=len(seats),total_price=price)
            fill_table.insert()
            
            current_event.free_seats -= len(seats)
            for seat in seats:
                current_event.mapped_free_seats.__setitem__(seat-1, True)
            current_event.update()
            
            current_customer = Customer.query.filter_by(id=customer_id).first()
            first_name = current_customer.fname
            last_name = current_customer.lname
            event_name = current_event.name
            start_time = current_event.start_time
            end_time = current_event.end_time
            booking_id = Book.query.filter_by(event_id=event_id,customer_id=customer_id).first().id
            Theatre_name = Theatre.query.filter_by(id=Theatre_id).first().name

            return jsonify({'first_name':first_name,'last_name':last_name,'event_name':event_name,
                            'start_time':start_time,'end_time':end_time,'seats':seats,
                            'booking_id':booking_id,'Theatre_name':Theatre_name, "price":price})
        else:
            return jsonify({'success':False , 'comment':"you can't book more then one time"})
    except:
        abort(422)


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422


@app.errorhandler(404)
def handle404(error):
    return jsonify({"success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404


@app.errorhandler(401)
def handle401(error):
    return jsonify({"success": False, 
                    "error": 401,
                    "message": "authentication error"
                    }), 401

@app.errorhandler(400)
def handle400(error):
    return jsonify({"success": False, 
                    "error": 400,
                    "message": "bad request"
                    }), 400

if __name__ == '__main__':
    app.run()

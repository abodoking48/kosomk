from flask import Flask, Blueprint, redirect, render_template, request, flash, session, redirect
from cs50 import SQL
import requests

sell_router = Blueprint('sell_router', 
                        __name__,
                        static_folder='static', template_folder='templates')
db = SQL('sqlite:///home.db')


@sell_router.route('/sell', methods=['POST', 'GET'])
def sell():
    if request.method == 'GET':
        return render_template('sell.html')

    photo = request.files.get('image')
    res = requests.post(
        'https://api.imgbb.com/1/upload',
        params={'key': '39dc978ddb298c7d892ef79dc97135ea'},
        files={'image': photo}
    )
    if res.ok:
        path = res.json()['data']['url']
        print(path)
        return (path)

    catogary = ('house', 'apartment', 'land')

    if catogary == 'house':
        address = request.form.get('address')
        price = request.form.get('price')
        rooms = request.form.get('rooms')
        space = request.form.get('space')
        descrp = request.form.get('descrpation')
        phone = request.form.get('phone')

    house = db.execute('INSERT INTO houses (user_id,price,rooms,space,descrpition,address,phone_number) VALUES (?,?,?,?,?,?,?)',
                       session["user_id"], price, rooms, space, descrp, phone, address)

    house_photo = db.execute('INSERT INTO photo (user_id,houses_id,path) VALUES (?,?,?)',
                             session["user_id"], house, path)

    if catogary == 'apartment':
        address = request.form.get('address')
        price = request.form.get('price')
        rooms = request.form.get('rooms')
        space = request.form.get('space')
        descrp = request.form.get('descrpation')
        phone = request.form.get('phone')

    apar = db.execute('INSERT INTO APARTMENT (user_id,price,rooms,space,descrpition,address,phone_number) VALUES (?,?,?,?,?,?,?)',
                      session["user_id"], price, rooms, space, descrp, phone, address)

    apar_photo = db.execute('INSERT INTO photo (user_id,apartmanet_id,path) VALUES (?,?,?)',
                            session["user_id"], apar, path)

    if catogary == 'land':
        address = request.form.get('address')
        price = request.form.get('price')
        rooms = request.form.get('rooms')
        space = request.form.get('space')
        descrp = request.form.get('descrpation')
        phone = request.form.get('phone')

    lan = db.execute('INSERT INTO LAND (user_id,price,rooms,space,descrpition,address,phone_number) VALUES (?,?,?,?,?,?,?)',
                     session["user_id"], price, rooms, space, descrp, phone, address)

    apar_photo = db.execute('INSERT INTO photo (user_id,land_id,path) VALUES (?,?,?)',
                            session["user_id"], lan, path)

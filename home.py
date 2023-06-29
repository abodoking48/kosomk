from flask import Flask, Blueprint,redirect, render_template, request, flash,session,redirect
from cs50 import SQL

home_page_router = Blueprint('home_page_router',__name__, static_folder='static', template_folder='templates')
db = SQL('sqlite:///home.db')

@home_page_router.route('/')
def index():
    # for featured 
    HOUSES_F = db.execute('SELECT houses.id,address, price, path FROM houses, PHOTO where houses.id = PHOTO.houses_id limit 2;')
    APARTMEN_F = db.execute('SELECT APARTMENT.id,address,price, path FROM APARTMENT, PHOTO where APARTMENT.id = PHOTO.APARTMENT_id  limit 2;')
    LAND_F = db.execute('SELECT land.id,address,price, path FROM LAND, PHOTO where LAND.id = PHOTO.LAND_id limit 2;')
    
    # for latest added
    
    HOUSES_L = db.execute('SELECT houses.id,address, price, path FROM houses, PHOTO where houses.id = PHOTO.houses_id ORDER BY 1 DESC limit 2;')
    APARTMEN_L = db.execute('SELECT APARTMENT.id,address, price, path FROM APARTMENT, PHOTO where APARTMENT.id = PHOTO.APARTMENT_id  ORDER BY 1 DESC limit 2;')
    LAND_L = db.execute('SELECT land.id,address, price, path FROM land, PHOTO where LAND.id = PHOTO.LAND_id  ORDER BY 1 DESC limit 2;')
    print(HOUSES_F[0]['path'])
    return render_template ('index.html', HOUSES_F = HOUSES_F, APARTMEN_F = APARTMEN_F, LAND_F =LAND_F,
                            HOUSES_l = HOUSES_L, APARTMEN_l = APARTMEN_L, LAND_l = LAND_L)

    
    
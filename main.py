# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect
from contact_model import Contact
app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True




@app.route(r'/', methods=['GET'])
def contact_book():
    contacts = Contact.query().fetch()
    return render_template('contact_book.html', contacts=contacts)

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    try:

        if request.method == "POST":
            contact = Contact(name=request.form['name'],
                              phone=request.form['phone'],
                              email=request.form['email']  )
            contact.put()
            flash('¡Se añadio el contacto!')
        return render_template('add_contact.html')


    except Exception as e:
        print('Error')

@app.route(r'/contacts/<uid>', methods=['GET'])
def contact_details(uid):

    contact = Contact.get_by_id(int(uid))
    if not contact:
        return redirect('/',code=301)
    return render_template('contact.html',contact=contact)

@app.route(r'/delete', methods=['POST'])
def delete_contact():
    contact = Contact.get_by_id(int(request.form['uid']))
    contact.key.delete()
    return redirect('/contacts/{}'.format(contact.key.id()))






if __name__ == '__main__':

    app.run()

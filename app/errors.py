#Mostra una pagina di errore personalizzata
from flask import render_template
from app import app, db

#Pagina che non esiste
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

#Gestione errori interno del server
@app.errorhandler(500)
def internal_error(error):
    #In caso di err su operazioni db, annulla operazione per preservare il db
    db.session.rollback()
    return render_template('500.html'), 500
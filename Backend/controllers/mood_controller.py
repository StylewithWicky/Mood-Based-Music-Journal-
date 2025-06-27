from flask import Flask,Blueprint,jsonify,request
from models import db,MoodLog
from datetime import datetime

mood_bp=Blueprint('mood_bp',__name__)

@mood_bp.route('/moods' ,methods=['POST'])
def create_moods():
    data=request.get_json()
    mood=data.get('mood')
    journal=data.get('journal_entry')

    if not mood:
        return jsonify({ 'error':'Mood required'}),400
    
    new_log=MoodLog(mood=mood, journal_entry=journal)

    db.session.add(new_log)
    db.session.commit()
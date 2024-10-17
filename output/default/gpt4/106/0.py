from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database setup
DATABASE_URL = 'sqlite:///users.db'  # Change to your database URL
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('email', String))

metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')
    if not email:
        return jsonify({"message": "Email parameter is required."}), 400
        
    session = Session()
    user = session.query(users_table).filter_by(email=email).first()
    
    if user:
        session.delete(user)
        session.commit()
        session.close()
        return jsonify({"message": "Successfully unsubscribed."}), 200
    else:
        session.close()
        return jsonify({"message": "User is not subscribed."}), 404

if __name__ == '__main__':
    app.run(debug=True)
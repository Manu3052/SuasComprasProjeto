class Pet(db.Model):
    _tablename_ = 'pets'
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db. Column(db.String(100), nullable = False)
    pet_type = db.Column(db.String(100), nullable = False)
    pet_age = db.Column(db.Integer(), nullable = False)
    pet_description = db.Column(db.String(100), nullable = False)

    def _repr_(self):
        return "<Pet %r>" % self.pet_name
        
    @app.route('/getpets', methods = ['GET'])
    def getpets():
        all_pets = []
        pets = Pet.query.all()
        for pet in pets:
            results = {
                        "pet_id":pet.id,
                        "pet_name":pet.pet_name,
                        "pet_age":pet.pet_age,
                        "pet_type":pet.pet_type,
                        "pet_description":pet.pet_description, }
            all_pets.append(results)

        return jsonify(
                {
                    "success": True,
                    "pets": all_pets,
                    "total_pets": len(pets),
                }
            )
    @app.route('/pets', methods = ['POST'])
    def create_pet():
        pet_data = request.json

        pet_name = pet_data['pet_name']
        pet_type = pet_data['pet_type']
        pet_age = pet_data['pet_age']
        pet_description = pet_data['pet_description']

        pet_description = pet_data['pet_description']
        pet = Pet(pet_name =pet_name , pet_type = pet_type, pet_age = pet_age, pet_description =pet_description )
        db.session.add(pet)
        db.session.commit()
        

        return jsonify({"success": True,"response":"Pet added"})

if _name_ == '_main_':
    app.run(debug=True)
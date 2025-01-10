const stateSchema = {
    type:'object',
    required: ['nom', 'isoCode'],
    properties: {
        nom: { type:'string' },
        isoCode: { type:'string', minLength: 2, maxLength: 2 }
    }
}

const addressSchema = {
        required: ['rue', 'numero', 'ville', 'pays'],
        properties: {
            rue: { type: 'string' },
            numero: { type: 'string' },
            ville: { type: 'string' },
            pays:  stateSchema
        }
    }
const personSchema={
    type:'object',
    required:['nom','prenom','dateDeNaissance','adresse','competences','titre'],
    properties:{
        nom:{type:'string'},
        prenom:{type:'string'},
        dateDeNaissance:{bsonType:'date'},
        adresse:addressSchema,
        competences:{ type:'array', maxItems:10, items:{type:'string'}},
        titre:{enum:['Melle','Mme','Mr','X']}

    }

}

db.createCollection('Personnes',{
    validator:{
        $jsonSchema:personSchema,
        },
    }
);


db.Personnes.insertOne({
    nom: 'Doe',
    prenom: 'John',
    dateDeNaissance: new Date('1990-05-15'),
    adresse: {
        rue: '123 Main St',
        numero: 'A',
        ville: 'New York',
        pays: {
            nom: 'États-Unis',
            isoCode: 'US'
        }
    },
    competences: ['JavaScript', 'Node.js', 'MongoDB'],
    titre: 'Mr'
});





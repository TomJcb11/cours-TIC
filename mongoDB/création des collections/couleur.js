const colorSchema = {
    type:'object',
    required: ['name','R', 'G', 'B'],
    properties: {
        R: {bsonType:'int'},
        G: {bsonType:'int'},
        B: {bsonType:'int'},
        A: {
            bsonType: 'double',
            minimum: 0,
            maximum: 1,
            multipleOf: 0.1,
            description: 'doit être un double compris entre 0 et 1 par paliers de 0.1 et est obligatoire'
        } 
    }
};
db.createCollection('Couleurs',{
    validator: {
        $jsonSchema: colorSchema,
    }
})
db.runCommand({
    collMod: 'Couleurs',
    validator: {
        $jsonSchema:  colorSchema,
        }
});
        
db.Couleurs.insertOne({
    name:'couleur mystère',
    R: 255,
    G: 0,
    B: 0,
    A: 0.7
})

db.Couleurs.insertOne({
    name:'rouge',
    R: 255,
    G: 0,
    B: 0,
})
//ajout d'un donneé hors limite pour $A ne doit pas passer 
db.Couleurs.insertOne({
    name:'vert',
    R: 0,
    G: 255,
    B: 0,
    A: 10
})



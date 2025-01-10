
const statSchema = {
    type: 'object',
    required: ['nbPages', 'nbChapitres'],
    properties: { nbPages: { bsonType: 'int' }, nbChapitres: { bsonType: 'int' } }

}
const livreSchema = {
    type: 'object',
    required: ['titre', 'auteurs', 'annee', 'dateDeCreation', 'estEnFrancais', 'categories', 'stats'], //champs non nulls
    properties: {
        titre: {
            type: 'string',
            minLength: 3,
            pattern: '[a-zA-Z0-9 ]+$'
        },
        auteurs: {
            type: 'array',
            uniqueItems: true,
            maxItems: 10,
            items: {
                type: 'string',
            }
        },
        annee: {
            bsonType: 'int',
            maximum: 9999,
            minimum: 0
        },
        dateDeCreation: {
            bsonType: 'date' // le format date n'existe pas en json mais il existe en bson
        },
        estEnFrancais: {
            type: 'boolean'
        },
        categories: {
            type: 'array',
            items: {
                enum: ['Horreur', 'Roman', 'Policier', 'Aventure']
            },
            uniqueItems: true
        },
        stats: statSchema
    }
}
db.createCollection('livres', {
    validator: {
        $jsonSchema: livreSchema
    }
})


db.livres.insertOne({
    titre:'le seigneur des agneaux',
    auteurs:['JKK Tolkien'],
    annee:2001,
    categories:['Roman','Aventure'],
    dateDeCreation: new Date(),
    estEnFrancais: false,
    stats:{
        nbPages:100,
        nbChapitres:10
    }
})
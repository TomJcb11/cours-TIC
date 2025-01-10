//créer une collection event qui a un nom unique , date début, date fin , ville
// il faut que la date de fin soit forcément supérieure à la date de début.

const eventSchema = {
    type : 'object',
    required: ['name','startDate','endDate','city'],
    properties: {
        name: {
            type: 'string',
            minLength: 3,
            unique : true
        },
        start: {
            type: 'date'
        },
        end: {
            type: Date,
    },
        city: {
            type: 'string',
            minLength: 3
        }
    },
    additionalProperties: false
};

db.createCollection('Events',{
    validator:{
        $jsonSchema:eventSchema,
        $expr: {
            $gt: ["$endDate", "$startDate"]
        }
    }
    
},
db.Events.createIndex(
    {name:1},
    {unique:true}
))

db.Events.insertOne({
    name: 'Concert',
    startDate: ISODate('2022-06-15'),
    endDate: ISODate('2022-06-17'),
    city: 'Paris'
})

db.Events.insertOne({
    name: 'Concert2',
    startDate: ISODate('2024-06-15'),
    endDate: ISODate('2024-06-11'),
    city: 'Paris'
})

db.Events.insertOne({
    name:'Concert',
    startDate: ISODate('2024-06-15'),
    endDate: ISODate('2024-06-17'),
    city:'Paris'
})


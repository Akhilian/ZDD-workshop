const faker = require('faker')
const cities = require('./cities')
 
module.exports = {
    generateTravelDetails: generateTravelDetails,
}

function generateTravelPositions(number_of_intermediate_positions) {

    const start_city_index = Math.floor(Math.random() * cities.length)

    arrival_city_index = (start_city_index + 1 < cities.length) ? start_city_index + 1 : 0;

    start_city = cities[start_city_index]
    arrival_city = cities[arrival_city_index]
    diff_lat = (arrival_city.coordinates.lat - start_city.coordinates.lat) / (number_of_intermediate_positions + 1)
    diff_long = (arrival_city.coordinates.long - start_city.coordinates.long) / (number_of_intermediate_positions + 1)

    const positions = []
    positions.push({
        lat: start_city.coordinates.lat,
        long: start_city.coordinates.long
    })

    for (let index = 1; index <= number_of_intermediate_positions; index++) {
        positions.push({
            lat: start_city.coordinates.lat + index * diff_lat,
            long: start_city.coordinates.long + index * diff_long
        })
    }

    positions.push({
        lat: arrival_city.coordinates.lat,
        long: arrival_city.coordinates.long
    })

    return positions;
}

function generateTravelDetails(context, events, done) {
    context.vars['now'] = new Date()
    context.vars['plane'] = {
        identifier: `${faker.random.number(999)}-${faker.random.number(999)}`,
        number_of_places: faker.random.number(999)
    }
    context.vars['flight'] = {
        identifier: `${faker.random.number(999)}-${faker.random.number(999)}`,
    }

    context.vars['positions'] = generateTravelPositions(10)
    
    return done()
}
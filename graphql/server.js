const express = require('express')
const graphqlHTTP = require('express-graphql')
var { buildSchema } = require('graphql')

const app = express()

// GraphQL schema
var schema = buildSchema(`
    type Query {
        domainName(id: Int): Owner
    }
    type Owner {
      id: Int!,
      name: String,
      block: String!,
      address: String!,
    }
`)

var domainData = [
  {
    id: 1,
    name: 'jefflau.eth',
    block: '1',
    address: '0x000'
  }
]
var getDomain = function(args) {
  var id = args.id
  console.log(args)
  return domainData
}

// Root resolver
var root = {
  domainName: getDomain
}

app.use(
  '/graphql',
  graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true
  })
)

app.listen(4000, () =>
  console.log('Express GraphQL Server Now Running On localhost:4000/graphql')
)

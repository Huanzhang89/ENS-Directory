const express = require('express')
const graphqlHTTP = require('express-graphql')
var { buildSchema } = require('graphql')

const app = express()

// GraphQL schema
var schema = buildSchema(`
    type Query {
        domainName(name: String): OwnerHistory
        address(hash: String): Address
    }

    type OwnerHistory {
      hash: String!,
      history: [Owner],
      owner: Owner,
    }

    type Owner {
      block: String!,
      address: String!,
    }
`)

// Root resolver
var root = {
  message: () => 'Hello World!'
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

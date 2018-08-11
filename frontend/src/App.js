import React, { Component } from 'react'
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from 'react-apollo'
import logo from './logo.svg'
import './App.css'

const client = new ApolloClient({
  uri: 'localhost:4000'
})

const App = () => (
  <ApolloProvider client={client}>
    <div>
      <h2>ENS Directory</h2>
    </div>
  </ApolloProvider>
)
// class App extends Component {
//   render() {
//     return (
//       <div className="App">
//         <header className="App-header">
//           <img src={logo} className="App-logo" alt="logo" />
//           <h1 className="App-title">Welcome to React</h1>
//         </header>
//         <p className="App-intro">
//           To get started, edit <code>src/App.js</code> and save to reload.
//         </p>
//       </div>
//     )
//   }
// }

export default App

import React, { Component } from 'react'
import request from 'superagent'
import Owners from './Owners'

export default class Layout extends Component {
  constructor(props) {
    super(props)
    this.state = {
      responseData: []
    }
  }

  fetchData(input) {
    const api = 'http://localhost:5000/'
    const endpoint = input.length === 66 ? 'node/' : 'address/'

    request.get(api + endpoint + input).end((err, res) => {
      this.setState({
        responseData: JSON.parse(res.text)
      })
    })
  }

  submitQuery(query) {
    this.fetchData(query)
  }
  render() {
    return (
      <div>
        <div className="search-bar">
          <h2>ENS Directory</h2>
          <div className="search-bar-2">
            <input
              className="search-input"
              ref="inputData"
              type="text"
              placeholder="search for ENS name or Ethereum address"
            />
            <button
              type="submit"
              onClick={() => this.submitQuery(this.refs.inputData.value)}
              value="Get Details"
            >
              Get Details
            </button>
          </div>
        </div>

        <Owners ownerHistory={this.state.responseData} />
      </div>
    )
  }
}

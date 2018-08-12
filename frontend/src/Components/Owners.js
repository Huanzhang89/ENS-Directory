import React from 'react'
import { Query } from 'react-apollo'
import gql from 'graphql-tag'

import Owner from './Owner'

class Owners extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    console.log(this.props.ownerHistory)
    return (
      <div>
        <div className="owner-list-container">
          <div className="labels">
            <div className="label bold">From Block</div>
            <div className="label bold">Event</div>
          </div>
        </div>
        {this.props.ownerHistory.history &&
          this.props.ownerHistory.history.map(owner => (
            <Owner ownerData={owner} />
          ))}
      </div>
    )
  }
}

export default Owners
